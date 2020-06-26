import sqlite3
import pandas as pd
import requests
import simplejson as json
from atlassian import Confluence
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

version_data = []
for i in range(0, len(project_key)):
    #프로젝트에 등록된 버전 get request
    url = requests.get('https://tcs.telechips.com:8443/rest/projects/1.0/project/' + project_key[i][0] + '/release/allversions', id_pw)
    version = json.loads(url.text)
    print(project_key[i][0])
    if len(version) != 0:
        for j in range(0, len(version)):
            #각 version에 등록된 issue를 구하는 request
            url3 = requests.get('https://tcs.telechips.com:8443/rest/api/2/search?maxResults=2000&fields=1&jql=fixVersion%3D' + version[j]['id'], id_pw)
            version_key = json.loads(url3.text)
            print(version[j]['name'])
            member = []
            timespent = 0
            for k in range(0, len(version_key['issues'])):
                url4 = requests.get('https://tcs.telechips.com:8443/rest/api/2/issue/' + version_key['issues'][k]['key'] + '/worklog', id_pw) #버전에 등록된 Issue로 worklog를 구하는 request
                worklog = json.loads(url4.text)
                for l in range(0, len(worklog['worklogs'])):
                    if worklog['worklogs'][l]['author']['displayName'].replace('(', ' ').split()[0] not in member:
                        member.append(worklog['worklogs'][l]['author']['displayName'].replace('(', ' ').split()[0])
                    timespent += worklog['worklogs'][l]['timeSpentSeconds']


