#!/usr/bin/env python3

from atlassian import Jira
import requests
import simplejson as json
import pandas as pd
import datetime
import sqlite3
#from datetime import timedelta

#------------------------------ 해당 버전에서 필요한 data를 추출하여 DB에 저장-------------------#
# 프로젝트 Key
project_list = ['SC']

# 해당 버전의 전체 이슈 API
allissue1 = 'https://tcs.telechips.com:8443/rest/api/2/version/'
allissue2 = '/relatedIssueCounts'

# 해당 버전의 미해결 이슈 API
unresolvedissue1 = 'https://tcs.telechips.com:8443/rest/api/2/version/'
unresolvedissue2 = '/unresolvedIssueCount'

delayIssue1 = 'https://tcs.telechips.com:8443/rest/api/2/search?jql=status%20not%20in(Closed%2C%20Resolved)\
%20and%20duedate%20%3C%20now()%20and%20fixVersion%20%3D%20'
delayIssue2 = '&maxResults=500&fields=None'

#현재 날짜 생성
date = datetime.datetime.now()
nowdate = date.strftime('%Y-%m-%d')
#print(nowdate)

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

#TCS에 등록된 모든 프로젝트의 ID를 key, 프로젝트 이름을 value로 정리
project_data = jira.projects(included_archived=None)
#print(project_data[0])

data_project = {}
for i in range(0, len(project_data)):
    r1 = {}
    r1.setdefault('name', project_data[i]['name'])
    r1.setdefault('key', project_data[i]['key'])
    r1.setdefault('projectcategory', project_data[i]['projectCategory']['name'])
    data_project.setdefault(project_data[i]['id'], r1)

#print(data_project)

data_version = {}
for i in range(0, len(project_list)):
    # TCS 버전정보 Get
    version_base = jira.get_project_versions(project_list[i], expand=None)
    
    # Project에 등록된 version의 정보들을 추출
    for i in range(0, len(version_base)):
        r = {}
        r.setdefault('name', version_base[i]['name'])
        r.setdefault('link', version_base[i]['self'])
        r.setdefault('createDate', nowdate)
        
        if 'releaseDate' in version_base[i]:
            releaseDate1 = version_base[i]['releaseDate']
            r.setdefault('duedate', releaseDate1)
        else:
            r.setdefault('duedate', '종료일 없음')
    
        if 'overdue' in version_base[i]:
            if version_base[i]['overdue'] is True:
                r.setdefault('status', '지연')
            else:
                r.setdefault('status', '진행중')
    
        if version_base[i]['released'] is True:
            r.setdefault('status', '완료')
        else:
            r.setdefault('status', '진행중')
        
        # TCS 버전에서 전체 이슈 개수 Get
        tcs_r1 = requests.get(allissue1 + version_base[i]['id'] + allissue2, userData)
        allissue = json.loads(tcs_r1.text)
        r.setdefault('allissue', str(allissue['issuesFixedCount']))
        
        # TCS 버전에서 unresolved 이슈 개수 Get
        tcs_r2 = requests.get(unresolvedissue1 + version_base[i]['id'] + unresolvedissue2, userData)
        unsolvedissue = json.loads(tcs_r2.text)
        r.setdefault('unsolvedissue', str(unsolvedissue['issuesUnresolvedCount']))
        
        #TCS 버전에서 지연중인 이슈 개수 Get
        tcs_r1 = requests.get(delayIssue1 + version_base[i]['id'] + delayIssue2, userData)
        delayissue = json.loads(tcs_r1.text)
        r.setdefault('delayIssue', str(delayissue['total']))
        
        r.setdefault('projectId', str(version_base[i]['projectId']))
        r.setdefault('projectName', data_project[str(version_base[i]['projectId'])]['name'])
        r.setdefault('projectKey', data_project[str(version_base[i]['projectId'])]['key'])
        
        # key는 버전의 id, value는 버전의 name, link, projectId, releaseDate, duedate, status, allissue, unsolvedissue를 저장
        data_version.setdefault(version_base[i]['id'], r)

#data_version의 값을 DataFrame 형태로 변경
data = pd.DataFrame.from_dict(data_version, orient='index')
#print(data)


#data_version의 값을 DB에 저장
con = sqlite3.connect('C:/Users/telechips/database/tcs.db')
data.to_sql(project_list[0], con, if_exists='replace', index_label = 'versionId')
con.close()
