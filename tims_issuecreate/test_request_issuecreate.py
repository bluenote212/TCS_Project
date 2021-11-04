import requests
import json
import pymongo


conn = pymongo.MongoClient("192.168.3.237", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}


data = {
            "fields": {
                        "project": {"key":"TMTPD"},
                        "summary": "API으로 이슈 생성",
                        "assignee": {"name": "B180093"},
                        "issuetype": {"name": "연구"},
                        "customfield_11101": {"id": "11305"},
                        "customfield_10200": "2021-03-26",
                        "duedate": "2021-03-26"
                    }
        }
headers = {'Content-Type': 'application/json'}

r1 = requests.post('https://tcs.telechips.com:8443/rest/api/2/issue', data=json.dumps(data), headers=headers, auth=(id_pw['os_username'], id_pw['os_password']))

conn.close()
print(r1.status_code)
print(r1.json())
