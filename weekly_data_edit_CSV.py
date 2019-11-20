#!/usr/bin/env python3

from atlassian import Jira
import requests
import simplejson as json
import pandas as pd
from datetime import datetime

#from datetime import timedelta

# 프로젝트 Key
project_list = ['TPD', 'CDD']

# 해당 버전의 전체 이슈 API
allissue1 = 'https://tcs.telechips.com:8443/rest/api/2/version/'
allissue2 = '/relatedIssueCounts'

# 해당 버전의 미해결 이슈 API
unresolvedissue1 = 'https://tcs.telechips.com:8443/rest/api/2/version/'
unresolvedissue2 = '/unresolvedIssueCount'

# ID, PW 정보
username = 'b180093'
password = 'infra4938hc!'
userData = {'os_username': username, 'os_password': password}

# jira auth
jira = Jira(
    url='https://tcs.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

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
        
        if 'releaseDate' in version_base[i]:
            str_releaseDate1 = str(version_base[i]['releaseDate'])
            r.setdefault('duedate', str_releaseDate1)
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
        
        r.setdefault('projectId', str(version_base[i]['projectId']))
        r.setdefault('projectName', data_project[str(version_base[i]['projectId'])]['name'])
        r.setdefault('projectKey', data_project[str(version_base[i]['projectId'])]['key'])
        
        # key는 버전의 id, value는 버전의 name, link, projectId, releaseDate, duedate, status, allissue, unsolvedissue를 저장
        data_version.setdefault(version_base[i]['id'], r)

#data_version의 값을 DataFrame 형태로 변경
data = pd.DataFrame.from_dict(data_version, orient='index')
#print(data)

#현재 날짜 생성
now = datetime.now()
nowdate = ('%s-%s-%s' % (now.year, now.month, now.day))
#print(nowdate)

#data_version의 값을 CSV 파일로 저장
data.to_csv('C:/Users/B180093/Desktop/2019-7-2_test.csv', encoding = 'utf-8')

# CSV 파일을 오픈하여 원하는 데이터만 출력
data_open = pd.read_csv('C:/Users/B180093/Desktop/2019-7-2_test.csv', index_col = 0)
data_filter = data_open[data_open['projectKey'] == 'TPD']
print(data_filter)

data_index = data_filter.index.tolist()
#print(data_filter.loc[data_index[0], ['status']])

'''
# Wiki 차트 colors parameter 색상 데이터 추출
chart_color = ''

for i in range(0, len(data_version_key)):
    if data_version[data_version_key[len(data_version_key) - 1 - i]]['status'] == '완료':
        r_color = ',#000000'
    if data_version[data_version_key[len(data_version_key) - 1 - i]]['status'] == '진행중':
        r_color = ',#3572b0'
    if data_version[data_version_key[len(data_version_key) - 1 - i]]['status'] == '지연':
        r_color = ',#cc1010'
    chart_color = chart_color + r_color

# Wiki 차트  colors parameter 색상 코드 출력
#print(chart_color)
'''




