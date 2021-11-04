import requests
import simplejson as json
import pymongo

conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}

#uri = 'http://192.168.33.120:8080/a/projects/?d'  # 모든 프로젝트의 정보 api
#uri = 'http://192.168.33.120:8080/a/projects/All-Projects/access'  # 특정 프로젝트에 접근가능한 group 정보 api, /projects/{project-name}/access
#uri = 'http://192.168.33.120:8080/a/groups/a6860db3283ce98f127dcb46f8ef1260309a77c1/members/'  # 특정 그룹의 멤버 정보 api, /groups/{group-id}/members/
uri = 'http://192.168.33.120:8080/a/groups/'  # 모든 그룹 리스트 정보 api

headers = {'Content-Type': 'application/json'}
r = requests.get(uri, headers=headers, auth=('B180093', '비번'))
print(r.text)
