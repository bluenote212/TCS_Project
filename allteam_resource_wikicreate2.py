from atlassian import Confluence
import sqlite3
from datetime import datetime
import pandas as pd
 
#Wiki auth
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
 
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])
 
#현재 년도, 월을 출력
day = datetime.now()
year = day.year
month = day.month

 
#worklog data를 가져옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
worklog = pd.read_sql("SELECT * FROM RND_worklog_" + str(month), con)
con.close()

#team_code data를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
team_code = pd.read_sql("SELECT * FROM team_code", con)
con.close()
team_code = team_code.values.tolist()
 
#각 팀원이 기록한 worklog를 확인하여 분류
team_resource = []
for i in range(len(team_code)):
    total_time = 0
    team_time = 0
    total_time = worklog[worklog['team'] == team_code[i][0]]['time_spent'].sum()
    team_time = worklog[(worklog['team'] == team_code[i][0]) & (worklog['project_key'] == team_code[i][2])]['time_spent'].sum()
    tims_time = worklog[(worklog['team'] == team_code[i][0]) & (worklog['project_key'] == 'TIMS')]['time_spent'].sum()
    group_time = worklog[(worklog['team'] == team_code[i][0]) & (worklog['project_category'] == 'RnD-Group 프로젝트')]['time_spent'].sum()
    team_resource.append([team_code[i][0], '<p>'+ str(round(((total_time-team_time-group_time-tims_time)/total_time)*100, 1)) + '%</p>(' + str(round(total_time-team_time-group_time-tims_time, 1)) + 'h)',\
                          '<p>'+ str(round((tims_time/total_time)*100, 1)) + '%</p>(' + str(round(tims_time, 1)) + 'h)',\
                          '<p>'+ str(round(((team_time + group_time)/total_time)*100, 1)) + '%</p>(' + str(round(team_time + group_time, 1)) + 'h)'])
    

wiki_body = '<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="4c919a65-51eb-4eab-bf47-6ddce442c602">\
<ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="7bd8143d-208e-45e0-a2af-ed511d514b67"><ac:parameter ac:name="width">33%</ac:parameter><ac:rich-text-body><p class="auto-cursor-target">\
<strong>SOCG</strong></p><table class="fixed-table"><colgroup><col style="width: 150.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /></colgroup><tbody>\
<tr><th style="text-align: center;">Team</th><th style="text-align: center;">개발</th><th style="text-align: center;">지원</th><th style="text-align: center;">경상</th></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10779">' + team_resource[2][0] + '</a></td><td style="text-align: center;">' + team_resource[2][1] + '</td><td style="text-align: center;">' + team_resource[2][2] + '</td><td style="text-align: center;">' + team_resource[2][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=11169">' + team_resource[22][0] + '</a></td><td style="text-align: center;">' + team_resource[22][1] + '</td><td style="text-align: center;">' + team_resource[22][2] + '</td><td style="text-align: center;">' + team_resource[22][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10783">' + team_resource[3][0] + '</a></td><td style="text-align: center;">' + team_resource[3][1] + '</td><td style="text-align: center;">' + team_resource[3][2] + '</td><td style="text-align: center;">' + team_resource[3][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10784">' + team_resource[4][0] + '</a></td><td style="text-align: center;">' + team_resource[4][1] + '</td><td style="text-align: center;">' + team_resource[4][2] + '</td><td style="text-align: center;">' + team_resource[4][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10786">' + team_resource[5][0] + '</a></td><td style="text-align: center;">' + team_resource[5][1] + '</td><td style="text-align: center;">' + team_resource[5][2] + '</td><td style="text-align: center;">' + team_resource[5][3] + '</td></tr>\
</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="96dc3e3f-aac3-472f-91ba-61e6ccc59dc5"><ac:parameter ac:name="width">33%</ac:parameter><ac:rich-text-body><p>\
<strong>PLG</strong></p><table class="fixed-table"><colgroup><col style="width: 150.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /></colgroup><tbody>\
<tr><th style="text-align: center;">Team</th><th style="text-align: center;">개발</th><th style="text-align: center;">지원</th><th style="text-align: center;">경상</th></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10792">' + team_resource[9][0] + '</a></td><td style="text-align: center;">' + team_resource[9][1] + '</td><td style="text-align: center;">' + team_resource[9][2] + '</td><td style="text-align: center;">' + team_resource[9][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=11136">' + team_resource[19][0] + '</a></td><td style="text-align: center;">' + team_resource[19][1] + '</td><td style="text-align: center;">' + team_resource[19][2] + '</td><td style="text-align: center;">' + team_resource[19][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=11137">' + team_resource[20][0] + '</a></td><td style="text-align: center;">' + team_resource[20][1] + '</td><td style="text-align: center;">' + team_resource[20][2] + '</td><td style="text-align: center;">' + team_resource[20][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10793">' + team_resource[10][0] + '</a></td><td style="text-align: center;">' + team_resource[10][1] + '</td><td style="text-align: center;">' + team_resource[10][2] + '</td><td style="text-align: center;">' + team_resource[10][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10796">' + team_resource[11][0] + '</a></td><td style="text-align: center;">' + team_resource[11][1] + '</td><td style="text-align: center;">' + team_resource[11][2] + '</td><td style="text-align: center;">' + team_resource[11][3] + '</td></tr>\
</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="23c672d8-ce32-40e2-a338-12ec5c43db45"><ac:parameter ac:name="width">33%</ac:parameter><ac:rich-text-body><p>\
<strong>BSPG</strong></p><table class="fixed-table"><colgroup><col style="width: 150.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /></colgroup><tbody>\
<tr><th style="text-align: center;">Team</th><th style="text-align: center;">개발</th><th style="text-align: center;">지원</th><th style="text-align: center;">경상</th></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10788">' + team_resource[7][0] + '</a></td><td style="text-align: center;">' + team_resource[7][1] + '</td><td style="text-align: center;">' + team_resource[7][2] + '</td><td style="text-align: center;">' + team_resource[7][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10789">' + team_resource[8][0] + '</a></td><td style="text-align: center;">' + team_resource[8][1] + '</td><td style="text-align: center;">' + team_resource[8][2] + '</td><td style="text-align: center;">' + team_resource[8][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10787">' + team_resource[6][0] + '</a></td><td style="text-align: center;">' + team_resource[6][1] + '</td><td style="text-align: center;">' + team_resource[6][2] + '</td><td style="text-align: center;">' + team_resource[6][3] + '</td></tr>\
</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="34e5e1d9-d5bc-45ad-a987-516d84cd5578"><ac:rich-text-body><p class="auto-cursor-target"><br /></p>\
<ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="0462ccd7-8238-4347-b4d2-4e33076aa017"><ac:parameter ac:name="width">33%</ac:parameter><ac:rich-text-body><p>\
<strong>MMG</strong></p><table class="fixed-table"><colgroup><col style="width: 150.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /></colgroup><tbody>\
<tr><th style="text-align: center;">Team</th><th style="text-align: center;">개발</th><th style="text-align: center;">지원</th><th style="text-align: center;">경상</th></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=11133">' + team_resource[16][0] + '</a></td><td style="text-align: center;">' + team_resource[16][1] + '</td><td style="text-align: center;">' + team_resource[16][2] + '</td><td style="text-align: center;">' + team_resource[16][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=11134">' + team_resource[17][0] + '</a></td><td style="text-align: center;">' + team_resource[17][1] + '</td><td style="text-align: center;">' + team_resource[17][2] + '</td><td style="text-align: center;">' + team_resource[17][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=11135">' + team_resource[18][0] + '</a></td><td style="text-align: center;">' + team_resource[18][1] + '</td><td style="text-align: center;">' + team_resource[18][2] + '</td><td style="text-align: center;">' + team_resource[18][3] + '</td></tr></tbody></table><p><br /></p><p>\
<strong>RPG</strong></p><table class="fixed-table"><colgroup><col style="width: 150.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /></colgroup><tbody>\
<tr><th style="text-align: center;">Team</th><th style="text-align: center;">개발</th><th style="text-align: center;">지원</th><th style="text-align: center;">경상</th></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10801">' + team_resource[0][0] + '</a></td><td style="text-align: center;">' + team_resource[0][1] + '</td><td style="text-align: center;">' + team_resource[0][2] + '</td><td style="text-align: center;">' + team_resource[0][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=11138">' + team_resource[21][0] + '</a></td><td style="text-align: center;">' + team_resource[21][1] + '</td><td style="text-align: center;">' + team_resource[21][2] + '</td><td style="text-align: center;">' + team_resource[21][3] + '</td></tr></tbody></table><p class="auto-cursor-target">\
<br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>\
<ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="c6fb20bf-e840-4bf0-81a5-d0d866e63e64"><ac:parameter ac:name="width">33%</ac:parameter><ac:rich-text-body><p>\
<strong>CTG</strong></p><table class="fixed-table"><colgroup><col style="width: 150.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /></colgroup><tbody>\
<tr><th style="text-align: center;">Team</th><th style="text-align: center;">개발</th><th style="text-align: center;">지원</th><th style="text-align: center;">경상</th></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10800">' + team_resource[13][0] + '</a></td><td style="text-align: center;">' + team_resource[13][1] + '</td><td style="text-align: center;">' + team_resource[13][2] + '</td><td style="text-align: center;">' + team_resource[13][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10798">' + team_resource[1][0] + '</a></td><td style="text-align: center;">' + team_resource[1][1] + '</td><td style="text-align: center;">' + team_resource[1][2] + '</td><td style="text-align: center;">' + team_resource[1][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=10797">' + team_resource[12][0] + '</a></td><td style="text-align: center;">' + team_resource[12][1] + '</td><td style="text-align: center;">' + team_resource[12][2] + '</td><td style="text-align: center;">' + team_resource[12][3] + '</td></tr>\
</tbody></table><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="4cfc10a1-68c3-4ba3-ad63-ed91f2d9d700"><ac:parameter ac:name="width">33%</ac:parameter><ac:rich-text-body><p>\
<strong>HWG</strong></p><table class="fixed-table"><colgroup><col style="width: 150.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /><col style="width: 80.0px;" /></colgroup><tbody>\
<tr><th style="text-align: center;">Team</th><th style="text-align: center;">개발</th><th style="text-align: center;">지원</th><th style="text-align: center;">경상</th></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=11130">' + team_resource[14][0] + '</a></td><td style="text-align: center;">' + team_resource[14][1] + '</td><td style="text-align: center;">' + team_resource[14][2] + '</td><td style="text-align: center;">' + team_resource[14][3] + '</td></tr>\
<tr><td><a href="https://tcs.telechips.com:8443/secure/Dashboard.jspa?selectPageId=11131">' + team_resource[15][0] + '</a></td><td style="text-align: center;">' + team_resource[15][1] + '</td><td style="text-align: center;">' + team_resource[15][2] + '</td><td style="text-align: center;">' + team_resource[15][3] + '</td></tr>\
</tbody></table><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>'
 
 
#Wiki 페이지 생성
confluence.update_page(
        parent_id = 95455710,
        page_id = 93389637,
        title = 'Resource_backdata',
        body = wiki_body,
        type='page',
        representation='storage'
    )
