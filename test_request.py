import requests
import simplejson as json
import pymongo

# -------------------- patch/save
url = 'http://219.240.43.89/api/patch/save'
headers = {
    'accept' : 'application/json;charset=UTF-8',
    'x-token' : '123qwe123'
}

files = open('C:/Users/B180093/Downloads/wp-excelservlet.xls', 'rb')

data = {
            "pageIdx":103,
            "patchDeploymentType" : "1",
            "patchDescription" : "test_chance",
            "patchNumber" : "0055",
            "patchType" : "6",
            "regDept" : "",
            "regId" : "admin2",
            "regName" : "admin2",
            "sdkIdx" : "1911",
            "patchCode" : files
        }

r = requests.post(url, headers=headers, data=data, verify=False)
print(r.status_code, r.text)

files.close()
# -------------------------------

'''
# ---------------------- CSS API Test
conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}


data = {
        "x-token" : "123qwe123"
        }
headers = {"accept" : "application/json;charset=UTF-8", "x-token" : "123qwe123"}

r1 = requests.get('https://219.240.43.89/api/patch/list?pageIdx=97', headers = headers, verify=False)
data1 = json.loads(r1.text)
print(data1)
# ------------------------
'''
