import requests
import sqlite3
import simplejson as json
import pandas as pd

#userdata를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
userData = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#profield data 
url = requests.get('https://tcs.telechips.com:8443/rest/profields/api/2.0/layouts/projects', userData)
data = json.loads(url.text)

a=[]
for i in range(0, len(data)):
    for j in range(len(data[i]['fields'])):
        if data[i]['fields'][j]['field']['id'] == -2:
            a.append(data[i]['fields'][j]['value']['value'])
        
        if data[i]['fields'][j]['field']['id'] == -1:
            a.append(data[i]['fields'][j]['value']['value'])
        
        if data[i]['fields'][j]['field']['id'] == -4:
            a.append(data[i]['fields'][j]['value']['value'])
        
        if data[i]['fields'][j]['field']['id'] == -5:
            a.append(data[i]['fields'][j]['value']['value']['displayName'])
        
        if data[i]['fields'][j]['field']['id'] == -7:
            a.append(data[i]['fields'][j]['value']['value']['name'])
        
        if data[i]['fields'][j]['field']['id'] == 43:
            a.append(data[i]['fields'][j]['value'])

