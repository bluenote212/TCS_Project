from atlassian import Jira
import datetime
import simplejson as json
import sqlite3
import requests
import pandas as pd
#from datetime import timedelta

#project Key 입력
project_list = ['ECC']

# ID, PW 정보
con = sqlite3.connect('C:/Users/telechips/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

userData = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

# jira auth
jira = Jira(
    url='https://tcs.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

#현재 날짜 생성
date = datetime.datetime.now()
nowdate = date.strftime('%Y-%m-%d')


# Bigpicture에서 프로젝트에 기록된 Worklog data를 추출
resource = requests.get('https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog/1.0/timesheet/project?targetKey=' + project_list[0], userData)
resource = json.loads(resource.text)

# 리소스, 
Member_list = ''
Timespent = 0
if len(resource['worklogAuthors']) == 0:
    Member_list = '없음'
    Timespent = 0

if len(resource['worklogAuthors']) != 0:
    for i in range(0, len(resource['worklogAuthors'])):
        if i == 0:
            Member_list = Member_list + resource['worklogAuthors'][i]['fullName']
        else:
            Member_list = Member_list + ', ' + resource['worklogAuthors'][i]['fullName']
    for i in range(0, len(resource['projects'][0]['issues'])):
            Timespent = Timespent + resource['projects'][0]['issues'][i]['timeSpent']

con = sqlite3.connect('C:/Users/telechips/database/tcs.db')
cur = con.cursor()
cur.execute('UPDATE project_info SET member_List=?, member=?, totalTime=? WHERE projectKey = ' + '"' + project_list[0] + '"', (Member_list, len(resource['worklogAuthors']), round(Timespent/60/60,1)))
con.commit()
cur.close()
con.close()
