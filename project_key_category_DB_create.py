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

#모든 프로젝트의 카테고리 data 생성
url = requests.get('https://tcs.telechips.com:8443/rest/api/2/project', id_pw)
data = json.loads(url.text)

projectCategory_list = []
for i in range(0, len(data)):
    key = data[i]['key']
    if 'projectCategory' in data[i]:
        projectCategory = data[i]['projectCategory']['name']
    else:
        projectCategory = 'None'
    data1 = [key, projectCategory]
    projectCategory_list.append(data1)
    
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data1 = pd.DataFrame(projectCategory_list, columns = ['project_key','category'])
data1.to_sql('project_key', con, if_exists='replace', index = False)
con.close()