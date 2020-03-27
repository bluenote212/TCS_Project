#!/usr/bin/env python  
from atlassian import Jira
import requests
import simplejson as json
import pandas as pd
import sqlite3
import datetime
#from datetime import timedelta

con = sqlite3.connect('C:/Users/telechips/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

userData = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

# jira auth
jira = Jira(
    url='https://tcs.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

#현재 날짜 생성
date = datetime.datetime.now()
nowdate = date.strftime('%Y-%m-%d')
#print(nowdate)

#TCS에 등록된 모든 프로젝트의 ID를 key, 프로젝트 이름을 value로 정리
project_data = jira.projects(included_archived=None)
#print(project_data)

gantt = requests.get('https://tcs.telechips.com:8443/rest/softwareplant-bigpicture/1.0/ppm/program', userData)
gantt = json.loads(gantt.text)
#print(gantt)


data_project = {}
for i_1 in range(0, len(project_data)):
    r1 = {}
    r1.setdefault('projedtId', project_data[i_1]['id'])
    r1.setdefault('projectKey', project_data[i_1]['key'])
    r1.setdefault('projectcategory', project_data[i_1]['projectCategory']['name'])
    for i_2 in range(0, len(gantt)):
        if project_data[i_1]['name'] == gantt[i_2]['name']:
            r1.setdefault('startDate', gantt[i_2]['startDate'])
            r1.setdefault('endDate', gantt[i_2]['endDate'])
            r1.setdefault('projectLead', gantt[i_2]['projectLead']['data']['displayName'])
    r1.setdefault('member', 0)
    r1.setdefault('member_List', '')
    r1.setdefault('lastTime', 0)
    r1.setdefault('totalTime', 0)

    data_project.setdefault(project_data[i_1]['name'], r1)
#print(data_project)

data = pd.DataFrame.from_dict(data_project, orient='index')

#data_version의 값을 DB에 저장
con = sqlite3.connect('C:/Users/telechips/database/tcs.db')
data.to_sql('project_info', con, if_exists='replace', index_label = 'projectName')
con.close()
