import requests
from requests.auth import HTTPBasicAuth
import json

# ---------------------------- jira cloud api
'''
url_jira = "https://telechips.atlassian.net/rest/api/3/issue/RITC-16"
url_confluence = "https://telechips.atlassian.net/wiki/rest/api/content/10158081?expand=body.storage"


auth = HTTPBasicAuth("bluenote212@telechips.com", "B0lNneIH0m6L0JT9Pnbl5C20")

headers = {
   "Accept": "application/json"
}

r = requests.get(url_jira, headers=headers, auth=auth)

#print(json.dumps(json.loads(r.text), indent=4, separators=(",", ": ")))
print(r.text)
'''
# -------------------------------------------------------------

# -------------------------Tempo rest api
# url = "https://api.tempo.io/core/3/worklogs?from=2021-10-01&to=2021-10-31"
# url = "https://telechips.atlassian.net/rest/api/2/user?accountId=61568669c7bea40069ff76d3"
url = "https://api.tempo.io/core/3/worklogs"
headers = {
   "Authorization": "Bearer Yq5uuN4nurLaCHikoOa8ivjLVT677b"
}

params = {
        'from': '2021-10-01',
        'to': '2021-10-31',
        'limit': 3,
        'offset': 5
    }

r = requests.get(url, headers=headers, params=params)

print(r.text)
