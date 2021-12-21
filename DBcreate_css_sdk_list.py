import requests
import simplejson as json
import pymongo

conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs

headers = {"accept": "application/json;charset=UTF-8", "x-token": "123qwe123"}

r_css_sdk = requests.get('https://css.telechips.com/api/sdk/name/list', headers=headers)
data_sdk_list = json.loads(r_css_sdk.text)

sdk_list = []

for i in range(0, len(data_sdk_list['list'])):
    params = {"sdkIdx": data_sdk_list['list'][i]['idx']}
    r_css_patch = requests.get('https://css.telechips.com/api/patch/number/list', headers=headers, params=params)
    temp = json.loads(r_css_patch.text)

    sdk_patch_list = []
    for j in range(0, len(temp['list'])):
        sdk_patch_list.append([temp['list'][j]['subject'], temp['list'][j]['patchNumber']])

    sdk_list.append({"sdk_name": data_sdk_list['list'][i]['subject'], "sdk_idx": data_sdk_list['list'][i]['idx'], "parent_idx": data_sdk_list['list'][i]['pageIdx'], "patch_list": sdk_patch_list})

col = db.css_sdk_list
col.delete_many({})
col.insert_many(sdk_list)

conn.close()
