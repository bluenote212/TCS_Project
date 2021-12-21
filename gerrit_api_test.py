import requests
import simplejson as json
import pymongo

uri = 'https://tcat-tb1.telechips.com/a/projects/?d'  # 모든 프로젝트의 정보를 가져오는 api
#uri = 'http://192.168.33.120:8080/a/projects/?d'  # 모든 프로젝트의 정보를 가져오는 api
#uri = 'http://192.168.33.10:8080/a/projects/All-Projects/access'  # 특정 프로젝트에 접근가능한 group 정보를 확인할 수 있는 api, /projects/{project-name}/access
#uri = 'http://192.168.33.10:8080/a/groups/a6860db3283ce98f127dcb46f8ef1260309a77c1/members/'  # 특정 그룹의 멤버를 확인 할 수 있는 api, /groups/{group-id}/members/


headers = {'Content-Type': 'application/json'}
r = requests.get(uri, headers = headers, auth=('cowon', 'asdf!@#456'))
print(r.text)
