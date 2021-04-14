import requests
import sqlite3
import simplejson as json
import pandas as pd
from datetime import datetime
from atlassian import Confluence

#userdata를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#project category table에서 category 선별해서 프로젝트 key를 가져 옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_key WHERE category = '1.SOC 개발' or category = '2.SOC 검증' or category = '3.SDK 개발' or category = '4.요소/기반 기술' or category = '5.사업자/선행/국책' or category = '6.HW개발' ", con)
project_key = project.values.tolist()
con.close()

#현재 년도, 월을 출력
day = datetime.now()

project_issue_data = []

for i in range(0, len(project_key)):
    print(project_key[i][0])
    total_issue_url = requests.get('https://tcs.telechips.com:8443/rest/api/2/search?jql=project%20%3D%20' + project_key[i][0] + '&maxResults=1&fields=j', id_pw)
    total_issue_text = json.loads(total_issue_url.text)
    if 'total' in total_issue_text.keys():
        total_issue = total_issue_text['total']
    else:
        total_issue = 'Error'
    
    week_issue_url = requests.get('https://tcs.telechips.com:8443/rest/api/2/search?jql=issueFunction%20not%20in%20hasSubtasks()%20AND%20issueFunction%20in%20dateCompare(%22%22%2C%20%22Start%20date%20%2B14d%20%3C%20dueDate%22)%20and%20statusCategory%20in%20(%22To%20Do%22%2C%22In%20Progress%22)And%20Issuetype%20not%20in%20(%22Epic%22)%20and%20project%20%3D%20' + project_key[i][0] + '&maxResults=1&fields=j', id_pw)
    week_issue_text = json.loads(week_issue_url.text)
    if 'total' in week_issue_text.keys():
        week_issue = week_issue_text['total']
    else:
        week_issue = 'Error'
    
    pending_issue_url = requests.get('https://tcs.telechips.com:8443/rest/api/2/search?jql=status%20%3D%20Pending%20and%20project%20%3D%20' + project_key[i][0] + '&maxResults=1&fields=j', id_pw)
    pending_issue_text = json.loads(pending_issue_url.text)
    if 'total' in pending_issue_text.keys():
        pending_issue = pending_issue_text['total']
    else:
        pending_issue = 'Error'
    
    project_issue_data.append([project_key[i][0], str(day.year) + '-' + str(day.strftime("%m")) + '-' + str(day.strftime("%d")), total_issue, week_issue, pending_issue])


#Wiki 페이지에 version Data page 생성
wiki_data_top = '<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="161913ea-7275-49ec-89af-a4e8e775825c"><ac:parameter ac:name="name">WBS</ac:parameter><ac:rich-text-body><p><br /></p><table class="wrapped"><colgroup><col /><col /><col /><col /><col /></colgroup><tbody><tr><th>Key</th><th><div class="content-wrapper"><p class="auto-cursor-target">date</p></div></th><th>total</th><th>2weeks</th><th>pending</th></tr>'
wiki_data_middle = ''
wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>'

for i in range(0, len(project_issue_data)):
    row = '<tr><td class="confluenceTd">' + str(project_issue_data[i][0]) + '</td><td class="confluenceTd">' + str(project_issue_data[i][1]) + '</td><td class="confluenceTd">' + str(project_issue_data[i][2]) + '</td><td class="confluenceTd">' + str(project_issue_data[i][3]) + '</td><td class="confluenceTd">' + str(project_issue_data[i][4]) + '</td></tr>'
    wiki_data_middle += row

wiki = wiki_data_top + wiki_data_middle + wiki_data_bottom
wiki = wiki.replace("&","<p>&amp;</p>") #특수문자 & 치환


confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1]
    )

'''
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('RND_worklog_' + str(month_1) + '_draft_ttt', con, if_exists='replace', index = False)
con.close()
'''

confluence.update_page(
        parent_id = 95455710,
        page_id = 175327739,
        title = 'Project issue status',
        body = wiki,
        type='page',
        representation='storage'
    )
