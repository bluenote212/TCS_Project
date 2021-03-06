import pandas as pd
import sqlite3
from atlassian import Confluence
import datetime

#Wiki auth
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

#현재 날짜 생성
date = datetime.datetime.now()
nowdate = date.strftime('%Y-%m-%d')
team_list = [
        'RND Innovation Team',
        'Wireless Team',
        'SOC Advanced Team',
        'SOC Design Team',
        'SOC Verification Team',
        'SOC Implementation Team',
        'Security Solution Team',
        'System BSP Team',
        'Application BSP Team',
        'SW Architecture Team',
        'Automotive Platform Team',
        'Driver Assistance Platform Team',
        'Bluetooth Team',
        'Automotive MCU Team',
        'HW Platform Team',
        'HW Verification Team',
        'Media Android Team',
        'Media Linux Team',
        'Media HAL Team',
        'Project Management Team',
        'STB Platform Team',
        'Technical Writing Team'
        ]

#------------------------------ DB에서 원하는 값을 추출-------------------#
allteam_resource = {}
#DB 연결하여 data import
for i in range(0, len(team_list)):
    con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
    resource = pd.read_sql("SELECT date, project, time FROM " + '"' + team_list[i] + '"' + " WHERE date > date('now', '-30 days')", con)
    con.close()
    project_list = list(resource['project'].drop_duplicates())
        
    project_resource = []
    for j in range(0, len(project_list)):
        project_1 = resource[resource['project'].isin([project_list[j]])]
        sum1 = project_1.sum(axis = 0)
        project_resource.append([project_list[j], round(sum1['time'], 1)])
        
    project_resource = sorted(project_resource, key=lambda x:x[1], reverse = True)
    allteam_resource.setdefault(team_list[i], project_resource)

allteam_resource_key = list(allteam_resource.keys())

table_total = ''
for i in range(0, len(allteam_resource.keys())):    
    for j in range(0, len(allteam_resource[allteam_resource_key[i]])):
        table_team = '<tr><td colspan="1">' + allteam_resource_key[i] + '</td><td colspan="1">' + allteam_resource[allteam_resource_key[i]][j][0] + \
        '</td><td style="text-align: center;" colspan="1">' + str(allteam_resource[allteam_resource_key[i]][j][1]) + '</td></tr>'
        table_total = table_total + table_team

wiki_body = '본 페이지는 여러 페이지에서 활용되는 backdata이니 절대 삭제하시면 안됩니다!!!!<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="28872881-a72f-49bf-9ef6-85afdcaf9ae0">\
<ac:parameter ac:name="name">전체팀리소스</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p>\
<table><colgroup><col /><col /><col /></colgroup><tbody><tr><th colspan="1">팀</th><th style="text-align: center;">Project</th>\
<th style="text-align: center;">Resource(Hours)</th></tr>' + table_total + \
'</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>'

# Wiki 페이지 생성
confluence.update_page(
        parent_id = 95455710,
        page_id = 93389637,
        title = 'Resource_backdata',
        body = wiki_body,
        type='page',
        representation='storage'
    )
