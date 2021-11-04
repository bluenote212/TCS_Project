import requests, json
import pymongo

conn = pymongo.MongoClient("192.168.3.237",27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': 'b180093', 'os_password': 'infra4938hC!'}



url = "https://tcs.telechips.com:8443/rest/api/2/field"
r = requests.get(url, id_pw)
data = json.loads(r.text)

data_final = []
for i in range(0, len(data)):
    data_final.append([data[i]['name'], data[i]['id']])

conn.close()
print(data_final)
