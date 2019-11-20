import requests
import simplejson as json


# ID, PW 정보
username = 'b180093'
password = 'infra4938hc!'
userData = {'os_username': username, 'os_password': password}

# TCS Rest API URL
base = 'https://tcs.telechips.com:8443'
version ='/rest/api/2/project/TPD/versions'
allissue = '/rest/api/2/version/10491/relatedIssueCounts'
unresolvedissue = '/rest/api/2/version/10491/unresolvedIssueCount'


# Wiki Rest API 정보
Wiki_baseURL = 'https://wiki.telechips.com:8443'


r1 = requests.get(base+version, userData)


# request 객체를 json 형식으로 변환
data = json.loads(r1.text)
print(type(data))
print(data)

'''
#data에서 key 값만 출력하여 list 형식으로 변경
data_key = list(data.keys())
print(data_key[0])
'''