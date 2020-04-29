import sqlite3
import pandas as pd
import requests
import simplejson as json


con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

id_pw = {'os_username' : user_info[0][0], 'os_password' : user_info[0][1]}

#project category table에서 category 선별해서 프로젝트 key를 가져 옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_key WHERE category = '1.SOC 개발' or category = '2.SOC 검증' or category = '3.SDK 개발' or category = '4.요소/기반 기술' or category = '5.사업자/선행/국책' or category = '6.HW개발' ", con)
project_key = project.values.tolist()
con.close()

#프로젝트 role data 생성
project_role = []
for i in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/projectconfig/1/roles/' + project_key[i][0] , id_pw)
    data = json.loads(url.text)
    rit = ''
    sub = ''
    for j in range(0, len(data['roles'])):
        if data['roles'][j]['id'] == 10500 and data['roles'][j]['total'] != 0:
            for k in range(0, len(data['roles'][j]['users'])):
                rit += data['roles'][j]['users'][k]['displayName'].replace('(', ' ').split()[0] + ', '
        if data['roles'][j]['id'] == 10400 and data['roles'][j]['total'] != 0:
            for k in range(0, len(data['roles'][j]['users'])):
                sub += data['roles'][j]['users'][k]['displayName'].replace('(', ' ').split()[0] + ', '
    project_role.append([project_key[i][0], sub[:-2], rit[:-2]])

data = pd.DataFrame(project_role, columns = ['project_key', 'Sub_PL', 'RIT']) #DataFrame 생성

#project_role DB 생성
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('project_role', con, if_exists='replace', index = False)
con.close()