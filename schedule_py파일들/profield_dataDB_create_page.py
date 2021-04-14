import requests
import simplejson as json
from atlassian import Confluence
import pymongo


#id_pw를 가져와서 리스트로 변환
conn = pymongo.MongoClient("192.168.3.237", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}
 
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = pw_data[1]['id'],
    password = pw_data[1]['pw'])
 
#project category table에서 category 선별해서 프로젝트 key를 가져 옴
col = db.project_key_category
project_key = list(col.find(
            {"$or": [
                        {'projectcategory':'1.SOC 개발'},
                        {'projectcategory':'2.SOC 검증'},
                        {'projectcategory':'3.SDK 개발'},
                        {'projectcategory':'4.요소/기반 기술'},
                        {'projectcategory':'5.사업자/선행/국책'},
                        {'projectcategory':'6.HW개발'},
                    ]
            },
            {
                    "_id":0,
            }
        ))

#project_role table을 가져옴
col = db.project_role
project_role = list(col.find({},{'_id':0}))

data = []
for i in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/profields/api/2.0/values/projects/' + str(project_key[i]['key']) + '?calculated=true', id_pw)
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
         
        if data[i][j]['field']['id'] == 49:#Platform
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['value'])
         
        if data[i][j]['field']['id'] == 50:#Application
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['value'])
 
    project_data.append(a)

#project_data에 project_role 추가
for i in range(0, len(project_data)):
    for j in range(0, len(project_role)):
        if project_data[i][1] == project_role[j]['project_key']:
            if project_role[j]['Sub_PL']:
                project_data[i].append(project_role[j]['Sub_PL'])
            else:
                project_data[i].append('')
            if project_role[j]['RIT']:
                project_data[i].append(project_role[j]['RIT'])
            else:
                project_data[i].append('')

 
#Wiki 페이지에 Project Data page 생성
wiki_data_top = '<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="70b8954e-f54e-46e7-8b34-a176d7c406ee">\
<ac:parameter ac:name="name">project_data</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><table><colgroup><col /><col /><col /><col /><col /><col /><col /><col />\
<col /><col /><col /><col /><col /><col /><col /><col /></colgroup><tbody><tr><th>Project_name</th><th>Key</th><th>PL</th><th>Category</th><th>종료보고</th><th>Application</th><th>Chip</th><th>Project_close</th>\
<th>Kick_off</th><th>Platform</th><th>Time_spent</th><th>Project_start</th><th>Status</th><th>Wiki</th><th>Sub_PL</th><th>RIT</th></tr>'
wiki_data_middle = ''
wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p><br /></p>'
 
#project_data 돌면서 table 생성
for i in range(0, len(project_data)):
    data_row = '<tr>'
    for j in range(0, 16):
        if j == 0: #Name에 link
            data_row += '<td><a href="https://tcs.telechips.com:8443/projects/' + project_data[i][1] + '/summary/statistics">' + project_data[i][j] + '</a></td>'
        elif j == 2 and project_data[i][j] != '': #PL 이름 입력
            data_row += '<td>' + project_data[i][j] + '</td>'
        elif j == 4 and project_data[i][j] != '': #종료보고에 link
            data_row += '<td><a href="' + project_data[i][j] + '">' + project_data[i][1] + '</a></td>'
        elif j == 8 and project_data[i][j] != '': #kick_off에 link
            data_row += '<td><a href="' + project_data[i][j] + '">' + project_data[i][1] + '</a></td>'
        elif j == 13 and project_data[i][j] != '': #Wiki에 link
            data_row += '<td><a href="' + project_data[i][j] + '">' + project_data[i][0] + '</a></td>'
        elif (j == 14 or 15) and project_data[i][j] != '': #role 입력
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

conn.close()

r = confluence.update_page(
        parent_id = 95455710,
        page_id = 120297594,
        title = 'project_data',
        body = wiki,
        type='page',
        representation='storage'
    )
print(r)