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

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_info WHERE category = '1.SOC 개발' or category = '2.SOC 검증' or category = '3.SDK 개발' or category = '4.요소/기반 기술' or category = '5.사업자/선행/국책' or category = '6.HW개발' ", con)
project_key = project.values.tolist()
con.close()

data = []

for h in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/profields/api/2.0/values/projects/' + str(project_key[h][0]) + '?calculated=true', userData)
    data.append(json.loads(url.text))

print(data)

'''
#profield data에서 project data만 추출
url = requests.get('https://tcs.telechips.com:8443/rest/profields/api/2.0/layouts/projects', userData)
data = json.loads(url.text)


project_data = []
for i in range(0, len(data)):
    a=[]
    for j in range(len(data[i]['fields'])):
        if data[i]['fields'][j]['field']['id'] == -2:
            if data[i]['fields'][j]['value'] is None:
                a.append('None')
            else:
                a.append(data[i]['fields'][j]['value']['value'])
        
        if data[i]['fields'][j]['field']['id'] == -1:
            if data[i]['fields'][j]['value'] is None:
                a.append('None')
            else:
                a.append(data[i]['fields'][j]['value']['value'])
        
        if data[i]['fields'][j]['field']['id'] == -5:
            if data[i]['fields'][j]['value'] is None:
                a.append('None')
            else:
                a.append(data[i]['fields'][j]['value']['value']['displayName'])
        
        if data[i]['fields'][j]['field']['id'] == -7:
            if data[i]['fields'][j]['value'] is None:
                a.append('None')
            else:
                a.append(data[i]['fields'][j]['value']['value']['name'])
        
        if data[i]['fields'][j]['field']['id'] == 43:
            if data[i]['fields'][j]['value'] is None:
                a.append('None')
            else:
                a.append(data[i]['fields'][j]['value']['value']['value'])
        
        if data[i]['fields'][j]['field']['id'] == 35:
            if data[i]['fields'][j]['value'] is None:
                a.append('None')
            else:
                a.append(data[i]['fields'][j]['value']['value'])

        if data[i]['fields'][j]['field']['id'] == 34:
            if data[i]['fields'][j]['value'] is None:
                a.insert(5, 'None')
            else:
                a.insert(5, data[i]['fields'][j]['value']['value'])
        
        if data[i]['fields'][j]['field']['id'] == 33:
            if data[i]['fields'][j]['value'] is None:
                a.append('None')
            else:
                a.append(data[i]['fields'][j]['value']['value']['text'])
        
        if data[i]['fields'][j]['field']['id'] == 36:
            if data[i]['fields'][j]['value'] is None:
                a.append('None')
            else:
                a.append(data[i]['fields'][j]['value']['value'])

    project_data.append(a)

#Wiki 페이지에 Project Data page 생성
wiki_data_top = '<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="70b8954e-f54e-46e7-8b34-a176d7c406ee">\
<ac:parameter ac:name="name">project_data</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><table><colgroup><col /><col /><col /><col />\
<col /><col /><col /><col /><col /></colgroup><tbody><tr><th>Name</th><th>Key</th><th>PL</th><th>Category</th><th>Chip</th><th>start_date</th>\
<th>due_date</th><th>Status</th><th>Wiki</th></tr>'
wiki_data_middle = ''
wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p><br /></p>'

for i in range(0, len(project_data)):
    data_row = '<tr>'
    for j in range(0, 9):
        if j == 0:
            data_row += '<td><a href="https://tcs.telechips.com:8443/projects/' + project_data[i][1] + '/summary/statistics">' + project_data[i][j] + '</a></td>'
        elif j== 8 and project_data[i][8] != 'None':
            data_row += '<td><a href="' + project_data[i][8] + '">Wiki</a></td>'
        else:
            data_row += '<td>' + project_data[i][j] + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row

wiki = wiki_data_top + wiki_data_middle + wiki_data_bottom
wiki = wiki.replace("&","<p>&amp;</p>")

confluence.update_page(
        parent_id = 95455710,
        page_id = 120297594,
        title = 'project_data',
        body = wiki,
        type='page',
        representation='storage'
    )
'''

