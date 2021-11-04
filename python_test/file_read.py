import pandas as pd
import pymongo
import json
import requests


conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs

headers = {'Content-Type': 'application/json'}

col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']} # TIMS, TCS rest api 접속 계정 정보 저장


excel_data = pd.read_excel('C:/Users/B180093/.spyder-py3/python_test/test.xlsx', keep_default_na=False, index_col=0)

final_result = excel_data.fillna('').to_dict('index')
print(len(final_result))


# Task 생성 data
for i in range(1, len(final_result)):
    data = {}
    if final_result[i]['Project Key'] != '':
        if final_result[i]['Issue Type'] == '연구' or final_result[i]['Issue Type'] == 'Task':

            sub_assignee = []
            if final_result[i]['Sub_Assignee'] != '':
                temp = final_result[i]['Sub_Assignee'].replace(' ', '').split(',')
                for j in range(0, len(temp)):
                    sub_assignee.append({'name': temp[j]})

            if final_result[i]['Epic No'] != '':
                link = final_result[final_result[i]['Epic No']]['Result']
            else:
                link = None

            data = {
                'fields': {
                    'project': {'key': final_result[i]['Project Key']},
                    'issuetype': {'name': final_result[i]['Issue Type']},
                    'summary': final_result[i]['Summary'],
                    'description': final_result[i]['Description'],
                    'assignee': {'name': final_result[i]['Assignee']},
                    'reporter': {'name': final_result[i]['Reporter']},
                    'customfield_10300': sub_assignee,  # sub assignee
                    'fixVersions': [{'name': final_result[i]['Fix Version/s']}],
                    'customfield_10200': str(final_result[i]['Start date']),  # start date
                    'duedate': str(final_result[i]['Due Date']),
                    'customfield_11101': {'value': final_result[i]['Chip']},  # chip
                    'customfield_10102': link  # Epic Link
                    }
                }
        elif final_result[i]['Issue Type'] == 'Epic':
            
            sub_assignee = []
            if final_result[i]['Sub_Assignee'] != '':
                temp = final_result[i]['Sub_Assignee'].replace(' ', '').split(',')
                for j in range(0, len(temp)):
                    sub_assignee.append({'name': temp[j]})

            data = {
                'fields': {
                    'project': {'key': final_result[i]['Project Key']},
                    'issuetype': {'name': final_result[i]['Issue Type']},
                    'customfield_10104': final_result[i]['Epic name'], # Epic name
                    'summary': final_result[i]['Summary'],
                    'description': final_result[i]['Description'],
                    'assignee': {'name': final_result[i]['Assignee']},
                    'reporter': {'name': final_result[i]['Reporter']},
                    'fixVersions': [{'name': final_result[i]['Fix Version/s']}],
                    'customfield_10200': str(final_result[i]['Start date']),  # start date
                    'duedate': str(final_result[i]['Due Date']),
                    'customfield_11101': {'value': final_result[i]['Chip']}  # chip
                    }
                }
        elif final_result[i]['Issue Type'] == 'Sub-task':
            
            sub_assignee = []
            if final_result[i]['Sub_Assignee'] != '':
                temp = final_result[i]['Sub_Assignee'].replace(' ', '').split(',')
                for j in range(0, len(temp)):
                    sub_assignee.append({'name': temp[j]})
                    
            data = {
                'fields': {
                    'project': {'key': final_result[i]['Project Key']},
                    'issuetype': {'name': final_result[i]['Issue Type']},
                    'parent': {'key': final_result[final_result[i]['Parent No']]['Result']},
                    'summary': final_result[i]['Summary'],
                    'description': final_result[i]['Description'],
                    'assignee': {'name': final_result[i]['Assignee']},
                    'reporter': {'name': final_result[i]['Reporter']},
                    'customfield_10300': sub_assignee,  # sub assignee
                    'fixVersions': [{'name': final_result[i]['Fix Version/s']}],
                    'customfield_10200': str(final_result[i]['Start date']),  # start date
                    'duedate': str(final_result[i]['Due Date']),
                    'customfield_11101': {'value': final_result[i]['Chip']}  # chip
                    }
            }
    
        r = requests.post('https://tcs.telechips.com:8443/rest/api/2/issue', data=json.dumps(data), headers=headers, auth=(id_pw['os_username'], id_pw['os_password']))

        dump = eval(r.text)

        if r.status_code == 201 or r.status_code == 200:
            final_result[i]['Result'] = dump['key']
        else:
            final_result[i]['Result'] = str(dump['errorMessages']) + ' / ' + str(dump['errors'])
        print(r.status_code, r.text)

    else:
        final_result[i]['Result'] = 'Fail'

print(final_result)
