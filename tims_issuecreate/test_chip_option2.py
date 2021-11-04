import requests
import simplejson as json
import pymongo

conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}

'''
insert_data = []

#TCS chip Field customfield_11101 저장
r = requests.get('https://tcs.telechips.com:8443/rest/api/2/issue/createmeta?projectKeys=TMTPD&expand=projects.issuetypes.fields',auth=(id_pw['os_username'], id_pw['os_password']))
data = json.loads(r.text)

for i in range(0, len(data['projects'][0]['issuetypes'][0]['fields']['customfield_11101']['allowedValues'])):
    insert_data.append({'field_id':'customfield_11101',
                      'value':data['projects'][0]['issuetypes'][0]['fields']['customfield_11101']['allowedValues'][i]['value']
                      })

    
col = db.customfield_list
col.delete_many({})
col.insert_many(insert_data)
'''
col = db.customfield_list
result = list(col.find({"field_id":"customfield_11101", "value":"TCC805X"}))

print(result)
conn.close()
