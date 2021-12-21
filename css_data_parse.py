import requests
import simplejson as json
import pymongo


conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}


headers = {"accept" : "application/json;charset=UTF-8", "x-token" : "123qwe123"}
params = {"pageIdx": 97}

r1 = requests.get('https://css.telechips.com/api/page/list', headers=headers)
data1 = json.loads(r1.text)

page_list = []


for i in range(0, len(data1['list'])):
    if len(data1['list'][i]['child']) == 0:
        page_list.append([data1['list'][i]['idx'], data1['list'][i]['subject']])
    else:
        for j in range(0, len(data1['list'][i]['child'])):
            if len(data1['list'][i]['child'][j]['child']) == 0 and data1['list'][i]['child'][j]['pageType'] != 'Document':
                page_list.append([data1['list'][i]['child'][j]['idx'], data1['list'][i]['subject'] + '/' + data1['list'][i]['child'][j]['subject']])
            else:
                for k in range(0, len(data1['list'][i]['child'][j]['child'])):
                    if len(data1['list'][i]['child'][j]['child'][k]['child']) == 0 and data1['list'][i]['child'][j]['child'][k]['pageType'] != 'Document':
                        page_list.append([data1['list'][i]['child'][j]['child'][k]['idx'], data1['list'][i]['subject'] + '/' + data1['list'][i]['child'][j]['subject'] + '/' + data1['list'][i]['child'][j]['child'][k]['subject']])

print(page_list)
