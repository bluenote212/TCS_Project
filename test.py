import sqlite3
import pandas as pd
import requests
import simplejson as json

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

userData = {'os_username' : user_info[0][0], 'os_password' : user_info[0][1]}

#project category table에서 category 선별해서 프로젝트 key를 가져 옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_key WHERE category = '1.SOC 개발' or category = '2.SOC 검증' or category = '3.SDK 개발' or category = '4.요소/기반 기술' or category = '5.사업자/선행/국책' or category = '6.HW개발' ", con)
project_key = project.values.tolist()
con.close()

'''
url = requests.get('https://tcs.telechips.com:8443/rest/projects/1.0/project/TMTPD/release/allversions', userData)
data1 = json.loads(url.text)

url2 = requests.get('https://tcs.telechips.com:8443/rest/api/2/search?jql=duedate%3Cnow()%20and%20fixVersion%3D10804&maxResults=1&fields=1', userData)
data2 = json.loads(url2.text)
'''

#프로젝트 role data 생성
project_role = []
for i in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/projectconfig/1/roles/' + project_key[i][0] , userData)
    data = json.loads(url.text)
    for j in range(0, len(data['roles'])):
        if data['roles'][j]['id'] == 10500 and data['roles'][j]['total'] != 0:
            rit = ''
            for k in range(0, len(data['roles'][j]['users'])):
                rit += data['roles'][j]['users'][k]['displayName']
        if data['roles'][j]['id'] == 10400 and data['roles'][j]['total'] != 0:
            sub = ''
            for k in range(0, len(data['roles'][j]['users'])):
                sub += data['roles'][j]['users'][k]['displayName']
        project_role.append([project_key[i][0], rit, sub])

