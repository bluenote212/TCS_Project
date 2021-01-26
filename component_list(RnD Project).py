import requests
import sqlite3
import simplejson as json
import pandas as pd

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project_list = pd.read_sql("SELECT * FROM project_key WHERE category in ('1.SOC 개발','2.SOC 검증','3.SDK 개발','4.요소/기반 기술','5.사업자/선행/국책','6.HW개발')", con)
project_info = project_list.values.tolist()
con.close()

project_component = []
for i in range(0, len(project_info)):
    url = requests.get('https://tcs.telechips.com:8443/rest/api/2/project/'+ project_info[i][0] + '/components', id_pw)
    data = json.loads(url.text)
    for j in range(0, len(data)):
        project_component.append([project_info[i][0], data[j]['id'], data[j]['name']])

print(project_component)
