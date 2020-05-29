import requests
import simplejson as json
import sqlite3
import pandas as pd

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

url = 'https://tcs.telechips.com:8443/rest/api/2/search?jql=project%3DTIMS&maxResults=1000&fields=customfield_11200'

data = requests.get(url, id_pw)
data = json.loads(data.text)

customer = []

for i in range(0, len(data['issues'])):
    customer.append(data['issues'][i]['fields']['customfield_11200'])

data1 = pd.DataFrame(customer, columns = ['customer'])
data1.to_csv('C:/Users/B180093/Downloads/customer.csv', index=False, encoding = 'utf-8-sig')
