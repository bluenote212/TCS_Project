import requests
import json
from atlassian import Confluence
from atlassian import Jira

username = 'b180093'
password = 'infra4938hc!'

# jira auth
jira = Jira(
    url='https://tcs.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

#Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

#page_info = confluence.get_page_labels(77172264, prefix=None, start=None, limit=None)
#page_info1 = confluence.get_page_by_title('~B180093', 'new page', start=None, limit=None)
#print(page_info1)

#page_labels = confluence.get_page_labels(87852914, prefix=None, start=None, limit=None)
#print(page_labels)        

data = [{"prefix":"global","name":"프로젝트주간보고"}]
headers = {'Content-Type': 'application/json'}
'''
r1 = requests.post('https://wiki.telechips.com:8443/rest/api/content/87853314/label', data=json.dumps(data), headers=headers, auth=(username, password))
print(r1.status_code)
'''