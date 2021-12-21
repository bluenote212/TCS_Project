import requests
import pymongo
import simplejson as json

conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs

col = db.user_data
data2 = list(col.find({}, {"_id": 0, "name": -1, "employee_No": -1}))
user_list = sorted(data2, reverse=False, key=lambda x: (x['name']))

db = conn.tcs
col = db.id_pw
pw_data = col.find({})

# -----------------------------------------------------------------
issue_key = 'ID103A1-731'
# -----------------------------------------------------------------

r_tcs = requests.get('https://tcs.telechips.com:8443/rest/api/2/issue/' + issue_key, auth=(pw_data[1]['id'], pw_data[1]['pw']))
issue_data = json.loads(r_tcs.text)

qa_project_name = issue_data['fields']['project']['name'].split(']')[-1]

if issue_data['fields']['customfield_10686'] is not None:  # customfield_10686 = SDK Version
    sdk_version = issue_data['fields']['customfield_10686']
else:
    sdk_version = 'SDK version 확인 필요'

patch_type = issue_data['fields']['customfield_11726']['value']  # customfield_11726 = patch type

if issue_data['fields']['customfield_10685'] is not None:
    patch_version = issue_data['fields']['customfield_10685']  # customfield_10685 = patch version
else:
    patch_version = 'Patch version 확인 필요'

summary = issue_data['fields']['summary'].split(']')[-1]

if patch_type is not None:
    if patch_type == 'TIMS (고객사 이슈)':
        if issue_data['fields']['customfield_12001'] is not None:
            r = requests.get('https://tims.telechips.com:8443/rest/api/2/issue/' + issue_data['fields']['customfield_12001'], auth=(pw_data[1]['id'], pw_data[1]['pw']))
            tims_issue = json.loads(r.text)
            if "errorMessages" in tims_issue.keys():
                css_project_key = '<font color="red">Patch Type Issuekeym Error, 잘못된 TIMS issue key</font>'
                css_issue_key = '<font color="red">Patch Type Issuekey Error, 잘못된 TIMS issue key</font>'
            else:
                css_project_key = tims_issue['fields']['project']['name']
                css_issue_key = tims_issue['key']
        else:
            css_project_key = '<font color="red">Patch Type Issuekeym 없음, TIMS Issue 확인 필요</font>'
            css_issue_key = '<font color="red">Patch Type Issuekey 없음, TIMS Issue 확인 필요</font>'

    elif patch_type == 'TCS (QA 검증 이슈)':
        if issue_data['fields']['customfield_12001'] is not None:
            r = requests.get('https://tcs.telechips.com:8443/rest/api/2/issue/' + issue_data['fields']['customfield_12001'], auth=(pw_data[1]['id'], pw_data[1]['pw']))
            tcs_issue = json.loads(r.text)
            if "errorMessages" in tcs_issue.keys():
                css_project_key = '<font color="red">Patch Type Issuekeym Error, 잘못된 TCS Issue key 확인 필요</font>'
                css_issue_key = '<font color="red">Patch Type Issuekeym Error, 잘못된 TCS Issue key 확인 필요</font>'

            else:
                css_project_key = tcs_issue['fields']['project']['name']
                css_issue_key = tcs_issue['key']
        else:
            css_project_key = '<font color="red">Patch Type Issuekeym 없음, TCS Issue 확인 필요</font>'
            css_issue_key = '<font color="red">Patch Type Issuekey 없음, TCS Issue 확인 필요</font>'

    elif patch_type == 'RND (신규 기능 추가/개선)':
        css_project_key = ''
        css_issue_key = ''

    else:
        css_project_key = ''
        css_issue_key = ''

else:
    patch_type = '<font color="red">Patch Type 없음 확인 필요</font>'
    css_project_key = '확인 필요'
    css_issue_key = '확인 필'


print('SDK Name : ' + qa_project_name)
print('SDK Version : ' + sdk_version)
print('sdkIdx : ')
print('Patch Type : ' + patch_type)
print('Patch issue key : ' + issue_key)
print('Patch - Project key : ' + css_project_key)
print('Patch - Issue key : ' + css_issue_key)
print('Patch Deployeement Type:')
print('Patch number (version) : ' + patch_version)
print('Patch Description : ' + summary)
print('Pre-applied Patch : ')
print('Release Note')
print('Patch Code')
print('Comment')
print('User (regId, regName, regDept')
