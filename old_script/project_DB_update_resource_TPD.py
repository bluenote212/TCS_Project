from atlassian import Jira
import datetime
import simplejson as json
import sqlite3
import requests
#from datetime import timedelta

# 프로젝트 Key
project_list2 = 'CD8030'

# ID, PW 정보
username = 'b180093'
password = 'infra4938hc!'
userData = {'os_username': username, 'os_password': password}

# jira auth
jira = Jira(
    url='https://tcs.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

#현재 날짜 생성
date = datetime.datetime.now()
nowdate = date.strftime('%Y-%m-%d')

# Bigpicture에서 프로젝트에 기록된 Worklog data를 추출하여 Json 파일로 저장
project_list1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog/1.0/timesheet/project?targetKey='
resource = requests.get(project_list1 + project_list2, userData)
resource = json.loads(resource.text)

'''
# Write JSON
with open('C:/Users/B180093/Desktop/resource.json', 'w', encoding="utf-8") as make_file:
    json.dump(resource, make_file, ensure_ascii=False, indent='\t')



with open('C:/Users/B180093/Desktop/resource.json', encoding='utf-8') as json_file:
    resource = json.load(json_file)
'''
Member = ''
Timespent = 0

for i in range(0, len(resource['worklogAuthors'])):
    if i == 0:
        Member = Member + resource['worklogAuthors'][i]['fullName']
    else:
        Member = Member + ', ' + resource['worklogAuthors'][i]['fullName']
#print(Member)

for i in range(0, len(resource['projects'][0]['issues'])):
    Timespent = Timespent + resource['projects'][0]['issues'][i]['timeSpent']

#print((Timespent/60/60))

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
cur = con.cursor()
cur.execute('UPDATE project_info SET member=?, totalTime=? WHERE projectKey = "' + project_list2 + '"', (Member, (Timespent/60/60)))
con.commit()
cur.close()
con.close()