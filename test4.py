import sqlite3
import pandas as pd
import requests
import simplejson as json
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


day = datetime.now()
year = day.year
month = day.month


url3 = requests.get('https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/jql?startDate=2019-1-1&endDate=' + str(year) + '-' + str(month) + '-' + str(day.day) + '&jql=fixVersion%3D' + '10804' + '&targetKey=72', id_pw)
resource = json.loads(url3.text)

worklog_timespent = 0
for j in range(0, len(resource['projects'])):
    for k in range(0, len(resource['projects'][j]['issues'])):
        for l in range(0, len(resource['projects'][j]['issues'][k]['workLogs'])):
            worklog_timespent += resource['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']

print(round(worklog_timespent/60/60, 2))

member = ''
for i in range(0, len(resource['worklogAuthors'])):
    if i == len(resource['worklogAuthors'])-1:
        member += resource['worklogAuthors'][i]['fullName'].replace('(', ' ').split()[0]
    else:
        member += resource['worklogAuthors'][i]['fullName'].replace('(', ' ').split()[0] + ','

print(member)