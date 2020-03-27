import requests
import sqlite3
import simplejson as json
import pandas as pd

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

userData = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

url = 'https://tcs.telechips.com:8443/rest/api/2/project'


url = requests.get(url, userData)
data = json.loads(url.text)

projectCategory_list = []


for i in range(0, len(data)):
    key = data[i]['key']
    if 'projectCategory' in data[140]:
        projectCategory = data[i]['projectCategory']['name']
    else:
        projectCategory = 'None'
    data1 = [key, projectCategory]
    projectCategory_list.append(data1)

print(projectCategory_list)
