import requests
import simplejson as json
import pymongo

# -------------------- patch/save
url = 'http://219.240.43.89/api/patch/save'
headers = {
    'accept' : 'application/json;charset=UTF-8',
    'x-token' : '123qwe123'
}

files = open('C:/Users/B180093/Downloads/TCC802x_Linux_IVI__1.8.0_0056_qwdqwdqw.patch', 'rb')
files2 = open('C:/Users/B180093/Downloads/dddd_dddd_asdf_wefw_0005_dfdfdfef.pdf', 'rb')

upload = {"patchCode" : files,"releaseNote": files2}
data = {
            "pageIdx":"112",
            "patchDeploymentType" : "1",
            "patchDescription" : "test_chance2",
            "patchNumber" : "0057", #중복되면 안됨
            "patchType" : "6",
            "regDept" : " ",
            "regId" : "admin2",
            "regName" : "admin2",
            "sdkIdx" : "13",
        }

r = requests.post(url, headers=headers, files = upload, data=data, verify=False)
print(r.status_code, r.text)

files.close()
files2.close()
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
