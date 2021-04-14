import requests
import simplejson as json
import pymongo

conn = pymongo.MongoClient("192.168.3.237", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}


col = db.project_key_category
project_key = list(col.find(
            {"$or": [
                        {'projectcategory':'1.SOC 개발'},
                        {'projectcategory':'2.SOC 검증'},
                        {'projectcategory':'3.SDK 개발'},
                        {'projectcategory':'4.요소/기반 기술'},
                        {'projectcategory':'5.사업자/선행/국책'},
                        {'projectcategory':'6.HW개발'},
                    ]
            },
            {
                    "_id":0,
            }
        ))

#프로젝트 role data 생성
project_role = []
for i in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/projectconfig/1/roles/' + project_key[i]['key'] , id_pw)
    data = json.loads(url.text)
    rit = ''
    sub = ''
    for j in range(0, len(data['roles'])):
        if data['roles'][j]['id'] == 10500 and data['roles'][j]['total'] != 0:
            for k in range(0, len(data['roles'][j]['users'])):
                rit += data['roles'][j]['users'][k]['displayName'].replace('(', ' ').split()[0] + ', '
        if data['roles'][j]['id'] == 10400 and data['roles'][j]['total'] != 0:
            for k in range(0, len(data['roles'][j]['users'])):
                sub += data['roles'][j]['users'][k]['displayName'].replace('(', ' ').split()[0] + ', '
    project_role.append({'project_key': project_key[i]['key'], 'Sub_PL': sub[:-2], 'RIT': rit[:-2]})
 
col = db.project_role
col.insert_many(project_role)
conn.close()
