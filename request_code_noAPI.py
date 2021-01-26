import requests
import json
import sqlite3
import pandas as pd

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

username = user_info[0][0]
password = user_info[0][1]


#version Comment update 코
data = {
        "id": 39705294,
        "title": "4. 업무 로드맵",
        "space": {"key": "TA3"},"type": "page",
        "version": {
                "message": "version comment",
                "number": 7
                }
        }
headers = {'Content-Type': 'application/json'}

r1 = requests.put('https://wiki.telechips.com:8443/rest/api/content/39705294', data=json.dumps(data), headers=headers, auth=(username, password))
print(r1.status_code)
print(r1)