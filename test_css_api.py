import requests
import simplejson as json
import pymongo
from datetime import datetime


# -------------------- patch/save
url = 'https://219.240.43.89/api/patch/save'
headers = {
    'accept' : 'application/json;charset=UTF-8',
    'x-token' : '123qwe123'
}

files = open('C:/Users/B180093/Downloads/test_qwdqwdqw.patch', 'rb')
files2 = open('C:/Users/B180093/Downloads/test_dddd_asdf_wefw_0005_dfdfdfef.pdf', 'rb')

upload = {"patchCode" : files,"releaseNote": files2}
data = {
        'comment': '테스트 테스트!@#',
        'imIssueId': "123456",
        'internal': True,
        'pageIdx': "62",
        'patchDeploymentType': "2",
        'patchDescription': "bug 1 patch_14:51~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        'patchNumber': "0008",
        'patchQaIssueId': "18",
        'patchTcsIdx': 11908,
        'patchTcsProjectKey': "QSD805XR",
        'patchType': "2",
        'regDept': "RND Innovation Team",
        'regId': "b180093",
        'regName': "신호찬 (Chance H Shin)",
        'sdkIdx': "35",
        'timsIdx': 10501
}

r = requests.post(url, headers=headers, files = upload, data=data, verify=False)
print(r.status_code, r.text)

files.close()
files2.close()
# -------------------------------
'''

# ---------------------- CSS API Test
headers = {"accept" : "application/json;charset=UTF-8", "x-token" : "123qwe123"}
request_tims = requests.get('https://css.telechips.com/api/tims/list?pjtKey=IM929A', headers=headers)

data1 = json.loads(request_tims.text)
print(data1['list'][0]['pjtId'])    
# ------------------------
'''

