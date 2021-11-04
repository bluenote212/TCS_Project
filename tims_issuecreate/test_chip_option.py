import requests
import simplejson as json
import pymongo

conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}


insert_data = []

#TCS chip Field customfield_11101 저장
r = requests.get('https://tims.telechips.com:8443/rest/api/2/issue/createmeta?projectKeys=IS001A&expand=projects.issuetypes.fields',auth=(id_pw['os_username'], id_pw['os_password']))
data = json.loads(r.text)

for i in range(0, len(data['projects'][0]['issuetypes'][0]['fields']['customfield_10300']['allowedValues'])):
    insert_data.append(data['projects'][0]['issuetypes'][0]['fields']['customfield_10300']['allowedValues'][i]['value']
                      )

sort_data = sorted(insert_data)


col = db.project_key_category
data1 = list(col.find({"projectcategory":"QA 프로젝트"},{"_id":0, "key":-1, "name":-1}))
project_list = sorted(data1, reverse=False, key=lambda x:(x['name']))

print(project_list)

'''
col = db.customfield_list
col.delete_many({})
col.insert_many(insert_data)
'''
conn.close()
