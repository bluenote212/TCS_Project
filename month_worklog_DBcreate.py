import requests
import sqlite3
import simplejson as json
from datetime import datetime
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
data2 = pd.read_sql("SELECT * FROM project_key", con)
con.close()
project_key = data2.values.tolist()

#현재 날짜 출력
day = datetime.now()

# 자동 전 월의 년도, 월, 첫째날, 마지막 날을 출력
#first_day1 = day - relativedelta(months=1)
#year_1 = first_day1.year #전 월의 년도
#month_1 = first_day1.month
#last_day = calendar.monthrange(year_1,month_1)[1] #전월의 마지막 날짜를 출력

# 자동 전 월의 년도, 월, 첫째날, 마지막 날을 출력
year_1 = 2020 #전 월의 년도
month_1 = 5
last_day = 30 #전월의 마지막 날짜를 출력


#각 팀 리소스 data 생성
data_resource = []
for h in range(0, len(team_code)): #각 팀 반복
    url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog/1.0/timesheet/team?startDate='
    url2 = '&endDate='
    url3 = '&targetKey=' + team_code[h][1] + '&extraField=customfield_11101&extraIssueFilter=issuetype%20not%20in%20(Schedule%2C%22Meeting%20Minutes%22)'
    for i in range(1, last_day+1): #하루의 워크로그를 구함, 한달 worklog를 한꺼번에 request하면 모두 response되지않음
        url = url1 + str(year_1) + '-' + str(month_1) + '-' + str(i) + url2 + str(year_1) + '-' + str(month_1) + '-' + str(i) + url3
        data1 = requests.get(url, id_pw)
        data2 = json.loads(data1.text)
        for j in range(0, len(data2['projects'])): #data2에서 project 반복
            for k in range(0, len(data2['projects'][j]['issues'])): #data2의 project에서 issue 반복
                issue_key = data2['projects'][j]['issues'][k]['key']
                issue_type = data2['projects'][j]['issues'][k]['type']
                summary = data2['projects'][j]['issues'][k]['summary']#summary추가
                
                if len(data2['projects'][j]['issues'][k]['customFields']) == 0: #customfield chip 항목을 구하기 위한 조건
                    issue_chip = ''
                else:
                    issue_chip = data2['projects'][j]['issues'][k]['customFields']['customfield_11101']['values'][0]#chip추가
    
                subtask = data2['projects'][j]['issues'][k]['subtask']
                
                if data2['projects'][j]['issues'][k]['subtask']: #worklog가 기록된 issue가 sub-task인지 확인하여 부모의 key와 type을 저장
                    parent_key = data2['projects'][j]['issues'][k]['parentIssue']['key']
                    parent_type = data2['projects'][j]['issues'][k]['parentIssue']['type']
                else:
                    parent_key = ''
                    parent_type = ''
    
                reporter = data2['projects'][j]['issues'][k]['reporter']['fullName']#reporter 추가
                assignee = data2['projects'][j]['issues'][k]['assignee']['fullName']#assignee 추가
                duedate = data2['projects'][j]['issues'][k]['dueDate'] #duedate 추가
                issue_created = data2['projects'][j]['issues'][k]['created'] #created 추가
                issue_timeSpent = data2['projects'][j]['issues'][k]['timeSpent'] #timeSpent 추가
             
                for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                    workstart = datetime.fromtimestamp(data2['projects'][j]['issues'][k]['workLogs'][l]['workStart']/1000).strftime('%Y-%m-%d')#worklog 기록 시간 추가
                    worklogcreated = datetime.fromtimestamp(data2['projects'][j]['issues'][k]['workLogs'][l]['worklogCreated']/1000).strftime('%Y-%m-%d')#worklog Created 시간 추가
                    worklog_timespent = 0
                    worklog_timespent += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']
                    worklog_author = data2['projects'][j]['issues'][k]['workLogs'][l]['authorName']
                    worklog_comment = data2['projects'][j]['issues'][k]['workLogs'][l]['comment']#worklog comment추가
                    if data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes'] != 0:
                        for m in range(0, len(data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes'])):
                            if data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes'][m]['attrTypeId'] == 2:
                                worklog_attr = str(data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes'][m]['attrTypeId'])#attr ID추가
                                worklog_attr_value = str(data2['projects'][j]['issues'][k]['workLogs'][l]['workLogAttributes'][m]['attrValue'])#attr value추가
                            else:
                                worklog_attr = ''
                                worklog_attr_value = ''
                    a = [data2['projects'][j]['name'], data2['projects'][j]['key'], issue_key, issue_type, summary, issue_chip, subtask, parent_key, parent_type, reporter,\
                        assignee, issue_created, duedate, round(issue_timeSpent/60/60, 2), workstart, worklogcreated, round(worklog_timespent/60/60, 2), team_code[h][0],\
                        worklog_author, worklog_comment, worklog_attr, worklog_attr_value]
                    data_resource.append(a) #data_resource에 각 워크로그 a를 추가

#project category 추가
for i in range(0,len(data_resource)):
    for j in range(0, len(project_key)):
        if data_resource[i][1] == project_key[j][0]:
            data_resource[i].insert(2, project_key[j][1])
            continue

#worklog attribute를 구하기 위한 request
url = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/attr/2'
data3 = requests.get(url, id_pw)
data4 = json.loads(data3.text)
worklog_attr_value_dic = {}

# 모든 worklog(chip) 항목을 worklog_attr_value_dic 딕셔너리에 저장
for i in range(0, len(data4['attributeValues'])):
        worklog_attr_value_dic.setdefault(str(data4['attributeValues'][i]['id']), str(data4['attributeValues'][i]['name']))

#data_resource에 모든 worklog_attr_value_dic 항목을 attribute name으로 변환
for i in range(0, len(data_resource)):
    if data_resource[i][21] == '2':
        data_resource[i][22] = worklog_attr_value_dic[data_resource[i][22]]
        del data_resource[i][21] #worklog_attr 삭제
    else:
        del data_resource[i][21]

#dataframe 형식으로 변환
data = pd.DataFrame(data_resource, columns = ['project_name', 'project_key', 'project_category', 'issue_key', 'issue_type', 'summary', 'issue_chip', 'subtask', 'parent_key',\
                                              'parent_type', 'reporter', 'assignee', 'issue_created', 'duedate', 'issue_timespent', 'workstart', 'worklogcreated',\
                                              'worklog_timespent', 'team', 'worklog_author', 'worklog_comment', 'worklog_chip'])

#table 생성
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('RND_worklog_' + str(month_1), con, if_exists='replace', index = False)
con.close()