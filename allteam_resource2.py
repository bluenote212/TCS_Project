import requests
import sqlite3
import simplejson as json
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import calendar

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

userData = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#team code 참고

team_code = [
        ['RND Innovation Team', '2', 'TMTPD'],
        ['Wireless Team', '3', 'TMWT'],
        ['SOC Advanced Team', '4', 'TMSAT'],
        ['SOC Design Team', '5', 'TMSDT'],
        ['SOC Verification Team', '6', 'TMSVT'],
        ['SOC Implementation Team', '8', 'TMSIT'],
        ['Security Solution Team', '9', 'TMSEC'],
        ['System BSP Team', '10', 'TMBSP'],
        ['Application BSP Team', '11', 'TMABT'],
        ['SW Architecture Team', '14', 'TMSAT2'],
        ['Automotive Platform Team', '15', 'TMAPT'],
        ['Driver Assistance Platform Team', '18', 'TMAPT2'],
        ['Bluetooth Team', '19', 'TMBT'],
        ['Automotive MCU Team', '22', 'TMST'],
        ['HW Platform Team', '87', 'TMHWT'],
        ['HW Verification Team', '88', 'TMHVT'],
        ['Media Android Team', '89', 'TMMT'],
        ['Media Linux Team', '90', 'TMMLT'],
        ['Media HAL Team', '91', 'TMMHT'],
        ['Project Management Team', '92', 'TMPMT'],
        ['STB Platform Team', '93', 'TMCAT'],
        ['Technical Writing Team', '94', 'TMTWT'],
        ['SOC IP Design Team', '95', 'TMIDT']
        ]

#현재 년도, 월을 출력
day = datetime.now()
year = day.year
month = day.month

#전 월을 출력
day_before = datetime.now() - relativedelta(months=1)
year_1 = day_before.year #전 월의 년도
month_1 = day_before.month
day_last = calendar.monthrange(year_1,month_1)[1]

data_resource = []

for h in range(0, len(team_code)): #각 팀 반복
    url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog/1.0/timesheet/team?startDate='
    url2 = '&endDate='
    url3 = '&targetKey=' + team_code[h][1] + '&extraIssueFilter=issuetype%20not%20in%20(Schedule%2C%22Meeting%20Minutes%22)'    
    # 현재 월의 워크로그 data를  data_resource에 저장
    for i in range(1, day.day):
        url = url1 + str(year) + '-' + str(month) + '-' + str(i) + url2 + str(year) + '-' + str(month) + '-' + str(i) + url3
        #월간 팀별 프로젝트 리소스
        data1 = requests.get(url, userData)
        data2 = json.loads(data1.text)
        for j in range(0, len(data2['projects'])):
            for k in range(0, len(data2['projects'][j]['issues'])):
                issue_key = data2['projects'][j]['issues'][k]['key']
                issue_type = data2['projects'][j]['issues'][k]['type']
                issue_subtask = data2['projects'][j]['issues'][k]['subtask']
                if data2['projects'][j]['issues'][k]['subtask']:
                    issue_parent_key = data2['projects'][j]['issues'][k]['parentIssue']['key']
                    issue_parent_type = data2['projects'][j]['issues'][k]['parentIssue']['type']
                else:
                    issue_parent_key = ''
                    issue_parent_type = ''
                for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                    issue_resource = 0
                    issue_resource = issue_resource + data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']
                    worklog_author = data2['projects'][j]['issues'][k]['workLogs'][l]['authorName']
                    date = str(year) + '-' + str(month) + '-' + str(i)
                    a = [date ,data2['projects'][j]['name'], data2['projects'][j]['key'], issue_key, issue_type, issue_subtask, issue_parent_key, issue_parent_type, team_code[h][0],\
                         worklog_author, round(issue_resource/60/60,2)]
                    data_resource.append(a)

data = pd.DataFrame(data_resource, columns = ['date','project_name', 'project_key', 'issue_key', 'issue_type', 'subtask', 'parent_key', 'issue_parent_type','team',\
                                              'worklog_author', 'time_spent'])

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('RND_worklog_' + str(month), con, if_exists='replace', index = False)
con.close()
