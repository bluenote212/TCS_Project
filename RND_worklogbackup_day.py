import requests
import sqlite3
import simplejson as json
from datetime import date, timedelta, datetime
import pandas as pd

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#team code를 DB에서 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
team_code = pd.read_sql("SELECT * FROM team_code", con)
con.close()
team_code = team_code.values.tolist()

#project info를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
key = pd.read_sql("SELECT * FROM project_key", con)
con.close()
project_key = key.values.tolist()

#현재 년도, 월을 출력
day = date.today()
yesterday = date.today() - timedelta(1)
year = yesterday.year
month = yesterday.month

data_resource = []
#각 팀 리소스 data 생성
for h in range(0, len(team_code)): #각 팀 반복
    url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog/1.0/timesheet/team?startDate='
    url2 = '&endDate='
    url3 = '&targetKey=' + team_code[h][1] + '&extraField=customfield_11101&extraIssueFilter=issuetype%20not%20in%20(Schedule%2C%22Meeting%20Minutes%22)'
    # 현재 월의 워크로그 data를  data_resource에 저장
    url = url1 + str(year) + '-' + str(month) + '-' + str(yesterday.day) + url2 + str(year) + '-' + str(month) + '-' + str(yesterday.day) + url3
    #월간 팀별 프로젝트 리소스
    data1 = requests.get(url, id_pw)
    data2 = json.loads(data1.text)
    for j in range(0, len(data2['projects'])):
        for k in range(0, len(data2['projects'][j]['issues'])):
            issue_key = data2['projects'][j]['issues'][k]['key']
            issue_type = data2['projects'][j]['issues'][k]['type']
            issue_summary = data2['projects'][j]['issues'][k]['summary']#summary추가
            
            if len(data2['projects'][j]['issues'][k]['customFields']) == 0:
                issue_chip = ''
            else:
                issue_chip = data2['projects'][j]['issues'][k]['customFields']['customfield_11101']['values'][0]#chip추가

            issue_subtask = data2['projects'][j]['issues'][k]['subtask']
            
            if data2['projects'][j]['issues'][k]['subtask']:
                issue_parent_key = data2['projects'][j]['issues'][k]['parentIssue']['key']
                issue_parent_type = data2['projects'][j]['issues'][k]['parentIssue']['type']
            else:
                issue_parent_key = ''
                issue_parent_type = ''

            issue_reporter = data2['projects'][j]['issues'][k]['reporter']['fullName']#reporter 추가
            issue_assignee = data2['projects'][j]['issues'][k]['assignee']['fullName']#assignee 추가
            issue_dueDate = data2['projects'][j]['issues'][k]['dueDate'] #duedate 추가
            issue_created = data2['projects'][j]['issues'][k]['created'] #created 추가
            issue_timeSpent = round(data2['projects'][j]['issues'][k]['timeSpent']/60/60,2) #timeSpent 추가
            
            for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                issue_worklogCreated = datetime.fromtimestamp(data2['projects'][j]['issues'][k]['workLogs'][l]['worklogCreated']/1000).strftime('%Y-%m-%d')#create시간 추가
                issue_worklogUpdated = datetime.fromtimestamp(data2['projects'][j]['issues'][k]['workLogs'][l]['worklogUpdated']/1000).strftime('%Y-%m-%d')#update시간 추가
                issue_resource = 0
                issue_resource += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']
                worklog_author = data2['projects'][j]['issues'][k]['workLogs'][l]['authorName']
                worklog_comment = data2['projects'][j]['issues'][k]['workLogs'][l]['comment']#worklog comment추가
                if len(data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes']) != 0:
                    for m in range(0, len(data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes'])):
                        if data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes'][m]['attrTypeId'] == 2:
                            worklog_Attr = data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes'][m]['attrTypeId']#attr ID추가
                            worklog_Attr_value = data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes'][m]['attrValue']#attr value추가
                        else:
                            worklog_Attr = ''
                            worklog_Attr_value = ''
                else:
                    worklog_Attr = ''
                    worklog_Attr_value = ''
                date_yesterday = str(year) + '-' + str(month) + '-' + str(yesterday.day)
                a = [date_yesterday ,data2['projects'][j]['name'], data2['projects'][j]['key'], issue_key, issue_type, issue_summary, issue_chip, issue_subtask, issue_parent_key,\
                    issue_parent_type, issue_reporter, issue_assignee, issue_created, issue_dueDate, issue_timeSpent, issue_worklogCreated, issue_worklogUpdated, round(issue_resource/60/60,2),\
                    team_code[h][0], worklog_author, worklog_comment, worklog_Attr, worklog_Attr_value]
                data_resource.append(a)


for i in range(0,len(data_resource)): #project category 추가
    for j in range(0, len(project_key)):
        if data_resource[i][2] == project_key[j][0]:
            data_resource[i].insert(3, project_key[j][1])
            continue

data = pd.DataFrame(data_resource, columns = ['date','project_name', 'project_key', 'project_category', 'issue_key', 'issue_type', 'issue_summary', 'issue_chip', 'issue_subtask', 'issue_parent_key',\
                                              'issue_parent_type', 'issue_reporter', 'issue_assignee', 'issue_created', 'issue_dueDate', 'issue_timeSpent', 'issue_worklogCreated',\
                                              'issue_worklogUpdated', 'worklog_timespent', 'team', 'worklog_author', 'worklog_comment', 'worklog_Attr', 'worklog_Attr_value'])

if yesterday.day == 1: #매달 1일이면 새 table 생성
    con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
    data.to_sql('RND_worklogbackup_' + str(month), con, if_exists='replace', index = False)
    con.close()
else:#1일이 아니면 추가
    con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
    data.to_sql('RND_worklogbackup_day_' + str(month), con, if_exists='append', index = False)
    con.close()
