import requests
import sqlite3
import simplejson as json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd

username = 'b180093'
password = 'infra4938hc!'
userData = {'os_username': username, 'os_password': password}

'''
#team code 참고
Technology Planning Dept. : 2
Wireless Team : 3
SOC Advanced Team : 4
SOC Design Team : 5
SOC Verification Team : 6
RF Design Team : 7
SOC Implementation Team : 8
Security Team : 9
System BSP Team : 10
Application BSP Team : 11
HW Team : 13
SW Architecture Team : 14
Automotive Platform Team : 15
CE-Linux Team : 16
CE-Android Team : 17
Advanced Platform Team : 18
Bluetooth Team : 19
Multimedia Team : 21
Safety Team : 22
'''
#현재 월을 출력
month = datetime.now()
year = month.strftime('%Y') #현재월의 년도
month = '{:02d}'.format(month.month)

#전 월을 출력
month_1 = datetime.now() - relativedelta(months=1)
year_1 = month_1.strftime('%Y') #전 월의 년도
month_1 = '{:02d}'.format(month_1.month)

#현재 날짜, 일주일 전 날짜 생성
date = datetime.now()
date_1 = date + timedelta(days=-7)
nowdate = date.strftime('%Y-%m-%d')
nowdate_1 = date_1.strftime('%Y-%m-%d')

url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog/1.0/timesheet/team?startDate='
url2 = '&endDate='
url3 = '&targetKey=11&extraIssueFilter=issuetype%20not%20in%20(Schedule%2C%22Meeting%20Minutes%22)'

data_resource = []

# 전 월의 워크로그 data를  data_resource에 저장
for i in range(1, 31):
    url = url1 + year_1 + '-' + month_1 + '-' + '{:02d}'.format(1) + url2 + year_1 + '-' + month_1 + '-' + '{:02d}'.format(1) + url3
    #월간 팀별 프로젝트 리소스
    data1 = requests.get(url, userData)
    data2 = json.loads(data1.text)
    for j in range(0, len(data2['projects'])):
        issue_resource = 0
        for k in range(0, len(data2['projects'][j]['issues'])):
            for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                issue_resource = issue_resource + data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']
        a = [year_1 + '-' + month_1 + '-' + '{:02d}'.format(i),data2['projects'][j]['name']+'(' + data2['projects'][j]['key'] + ')',round(issue_resource/60/60,1)]
        data_resource.append(a)

# 현재 월의 워크로그 data를  data_resource에 저장
for i in range(1, date.day):
    url = url1 + year + '-' + month_1 + '-' + '{:02d}'.format(1) + url2 + year + '-' + month_1 + '-' + '{:02d}'.format(1) + url3
    #월간 팀별 프로젝트 리소스
    data1 = requests.get(url, userData)
    data2 = json.loads(data1.text)
    for j in range(0, len(data2['projects'])):
        issue_resource = 0
        for k in range(0, len(data2['projects'][j]['issues'])):
            for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                issue_resource = issue_resource + data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']
        a = [year + '-' + month + '-' + '{:02d}'.format(i),data2['projects'][j]['name']+'(' + data2['projects'][j]['key'] + ')',round(issue_resource/60/60,1)]
        data_resource.append(a)

data = pd.DataFrame(data_resource, columns = ['date','project','time'])

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('Application BSP Team', con, if_exists='replace', index = False)
con.close()
