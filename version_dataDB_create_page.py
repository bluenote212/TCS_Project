import sqlite3
import pandas as pd
import requests
import simplejson as json
from atlassian import Confluence
from datetime import datetime

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()

id_pw = {'os_username' : user_info[0][0], 'os_password' : user_info[0][1]}

#project category table에서 category 선별해서 프로젝트 key를 가져 옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_key WHERE category = '1.SOC 개발' or category = '2.SOC 검증' or category = '3.SDK 개발' or category = '4.요소/기반 기술' or category = '5.사업자/선행/국책' or category = '6.HW개발' ", con)
project_key = project.values.tolist()
con.close()

#현재 년도, 월을 출력
day = datetime.now()
year = day.year
month = day.month

status_release = '<ac:structured-macro ac:name="status" ac:schema-version="1" ac:macro-id="ef71acd3-1ae0-4eda-99b2-11e0aee72d0e"><ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">release</ac:parameter><ac:parameter ac:name="" /></ac:structured-macro>'
status_unrelease = '<ac:structured-macro ac:name="status" ac:schema-version="1" ac:macro-id="7570780e-a96c-465c-8f7e-acf4245eb381"><ac:parameter ac:name="colour">Blue</ac:parameter><ac:parameter ac:name="title">unlease</ac:parameter><ac:parameter ac:name="" /></ac:structured-macro>'
status_archived = '<ac:structured-macro ac:name="status" ac:schema-version="1" ac:macro-id="6242d969-7110-49d8-9898-cf5e37aa02e4"><ac:parameter ac:name="colour">Grey</ac:parameter><ac:parameter ac:name="title">archived</ac:parameter><ac:parameter ac:name="" /></ac:structured-macro>'

version_data = []
for i in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/projects/1.0/project/' + project_key[i][0] + '/release/allversions', id_pw)
    version = json.loads(url.text)
    if len(version) != 0:
        for j in range(0, len(version)):
            temp = []
            if version[j]['released'] == True:
                status = status_release
            elif version[j]['archived'] == True:
                status = status_archived
            else:
                status = status_unrelease
            #duedate가 지난 지연중인 이슈 개수를 구하는 request
            url2 = requests.get('https://tcs.telechips.com:8443/rest/api/2/search?jql=duedate%3Cnow()%20and%20fixVersion%3D'+ version[j]['id'] +'&maxResults=1&fields=1', id_pw)
            duedate = json.loads(url2.text)
            #해당 fixversion의 worklog를 구하는 request
            url3 = requests.get('https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/jql?startDate=' + str(year-1) + '-' + str(month) + '-' + str(day.day) + '&endDate=' + str(year) + '-' + str(month) + '-' + str(day.day) + '&jql=fixVersion%3D' + version[j]['id'] + '&targetKey=72', id_pw)
            resource = json.loads(url3.text)
            timespent = 0
            for k in range(0, len(resource['projects'])):
                for l in range(0, len(resource['projects'][k]['issues'])):
                    for m in range(0, len(resource['projects'][k]['issues'][l]['workLogs'])):
                        timespent += resource['projects'][k]['issues'][l]['workLogs'][m]['timeSpent']
            member = ''
            for o in range(0, len(resource['worklogAuthors'])):
                if o == len(resource['worklogAuthors'])-1:
                    member += resource['worklogAuthors'][o]['fullName'].replace('(', ' ').split()[0]
                else:
                    member += resource['worklogAuthors'][o]['fullName'].replace('(', ' ').split()[0] + ','
            
            url4 = requests.get('https://tcs.telechips.com:8443/rest/api/2/search?jql=duedate<now()%20and%20status%20not%20in(Resolved%2CClosed)%20and%20fixVersion%3D'+ version[j]['id'] +'&maxResults=1&fields=1', id_pw)
            duedate_over = json.loads(url4.text)
            
            temp = [
                    project_key[i][2],
                    project_key[i][0],
                    version[j]['id'],
                    version[j]['name'],
                    version[j]['description'],
                    version[j]['startDate']['formatted'],
                    version[j]['releaseDate']['formatted'],
                    status,
                    duedate['total'],
                    version[j]['status']['complete']['count'],
                    version[j]['status']['unmapped']['count'] + version[j]['status']['toDo']['count'] + version[j]['status']['inProgress']['count'] + version[j]['status']['complete']['count'],
                    duedate_over['total'],
                    round(timespent/60/60, 2),
                    member
                    ]
            version_data.append(temp)

data = pd.DataFrame(version_data, columns = ['project_name', 'project_key', 'id', 'name', 'description', 'start_date', 'release_date', 'status', 'duedate_over_issue', 'resolved_issue', 'total_issue', 'duedate_over', 'timespent', 'member'])
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('version_data', con, if_exists='replace', index = False)
con.close()

#Wiki 페이지에 version Data page 생성
wiki_data_top = '<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="70b8954e-f54e-46e7-8b34-a176d7c406ee">\
<ac:parameter ac:name="name">version_data</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><table><colgroup><col /><col /><col /><col /><col /><col /><col /><col /><col /><col />\
<col /><col /><col /><col /><col /></colgroup><tbody><tr><th>Project_name</th><th>Key</th><th>Milestone_id</th><th>Milestone_name</th><th>Description</th><th>Milestone_start</th><th>Milestone_close</th><th>Release</th>\
<th>Plan_issue</th><th>Resolved_issue</th><th>Total_issue</th><th>Duedate_over</th><th>timespent</th><th>Member</th></tr>'
wiki_data_middle = ''
wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p><br /></p>'

#version data 돌면서 table 생성
for i in range(0, len(version_data)):
    data_row = '<tr>'
    for j in range(0, len(version_data[i])):
        if j == 3: #version name에 link
            data_row += '<td><a href="https://tcs.telechips.com:8443/projects/' + str(version_data[i][1]) + '/versions/' + str(version_data[i][2]) + '">' + str(version_data[i][j]) + '(' + str(version_data[i][2]) + ')' + '</a></td>'
        else: #나머지 항목은 값만 입력
            data_row += '<td>' + str(version_data[i][j]) + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row

wiki = wiki_data_top + wiki_data_middle + wiki_data_bottom
wiki = wiki.replace("&","<p>&amp;</p>") #특수문자 & 치환

confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1]
    )

confluence.update_page(
        parent_id = 95455710,
        page_id = 121733850,
        title = 'version_data',
        body = wiki,
        type='page',
        representation='storage'
    )
