import requests
import sqlite3
import simplejson as json
import pandas as pd
from atlassian import Confluence

#userdata를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
userData = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}


confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

#project category table에서 category 선별해서 프로젝트 key를 가져 옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_key WHERE category = '1.SOC 개발' or category = '2.SOC 검증' or category = '3.SDK 개발' or category = '4.요소/기반 기술' or category = '5.사업자/선행/국책' or category = '6.HW개발' ", con)
project_key = project.values.tolist()
con.close()

#project_role table을 가져옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_role", con)
project_role = project.values.tolist()
con.close()

data = []
for i in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/profields/api/2.0/values/projects/' + str(project_key[i][0]) + '?calculated=true', userData)
    data.append(json.loads(url.text))

project_data = []
for i in range(0, len(data)):
    a=[]
    for j in range(len(data[i])):
        if data[i][j]['field']['id'] == -2:#Name
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])
        
        if data[i][j]['field']['id'] == -1:#Key
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])
        
        if data[i][j]['field']['id'] == -5:#PL
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['displayName'].replace('(', ' ').split()[0])
        
        if data[i][j]['field']['id'] == -7:#Category
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['name'])

        if data[i][j]['field']['id'] == 48:#종료보고
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])

        if data[i][j]['field']['id'] == 43:#Chip
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['value'])
        
        if data[i][j]['field']['id'] == 35:#due_date
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])

        if data[i][j]['field']['id'] == 47:#kick_off
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])

        if data[i][j]['field']['id'] == 30:#time_spent
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['formatted'])

        if data[i][j]['field']['id'] == 34:#start_date
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])
        
        if data[i][j]['field']['id'] == 33:#Status
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['text'])
        
        if data[i][j]['field']['id'] == 36:#Wiki
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])

    project_data.append(a)


#project_data에 project_role 추가
for i in range(0, len(project_data)):
    for j in range(0, len(project_role)):
        if project_data[i][1] == project_role[j][0]:
            project_data[i].append(project_role[j][1])
            project_data[i].append(project_role[j][2])


#Wiki 페이지에 Project Data page 생성
wiki_data_top = '<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="70b8954e-f54e-46e7-8b34-a176d7c406ee">\
<ac:parameter ac:name="name">project_data</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><table><colgroup><col /><col /><col /><col /><col /><col />\
<col /><col /><col /><col /><col /><col /><col /><col /></colgroup><tbody><tr><th>Name</th><th>Key</th><th>PL</th><th>Category</th><th>종료보고</th><th>Chip</th><th>due_date</th>\
<th>kick_off</th><th>time_spent</th><th>start_date</th><th>Status</th><th>Wiki</th><th>Sub_PL</th><th>RIT</th></tr>'
wiki_data_middle = ''
wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p><br /></p>'

#project_data 돌면서 table 생성
for i in range(0, len(project_data)):
    data_row = '<tr>'
    for j in range(0,14):
        if j == 0: #Name에 link
            data_row += '<td><a href="https://tcs.telechips.com:8443/projects/' + project_data[i][1] + '/summary/statistics">' + project_data[i][j] + '</a></td>'
        elif j == 2 and project_data[i][j] != '': #PL 이름 입력
            data_row += '<td>' + project_data[i][j] + '</td>'
        elif j == 4 and project_data[i][j] != '': #종료보고에 link
            data_row += '<td><a href="' + project_data[i][j] + '">' + project_data[i][1] + '</a></td>'
        elif j == 7 and project_data[i][j] != '': #kick_off에 link
            data_row += '<td><a href="' + project_data[i][j] + '">' + project_data[i][1] + '</a></td>'
        elif j == 11 and project_data[i][j] != '': #Wiki에 link
            data_row += '<td><a href="' + project_data[i][j] + '">' + project_data[i][1] + '</a></td>'
        elif (j == 12 or 13) and project_data[i][j] != '': #role 입력
            temp = ''
            for k in range(0, len(project_data[i][j])):
                temp += project_data[i][j][k]
            data_row += '<td>' + temp + '</td>'
            temp = ''
        else: #나머지 항목은 값만 입력
            data_row += '<td>' + project_data[i][j] + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row

wiki = wiki_data_top + wiki_data_middle + wiki_data_bottom
wiki = wiki.replace("&","<p>&amp;</p>") #특수문자 & 치환

confluence.update_page(
        parent_id = 95455710,
        page_id = 120297594,
        title = 'project_data',
        body = wiki,
        type='page',
        representation='storage'
    )
