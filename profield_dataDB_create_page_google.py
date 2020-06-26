import requests
import sqlite3
import simplejson as json
import pandas as pd
from atlassian import Confluence
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

#project category table에서 category 선별해서 프로젝트 key를 가져 옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_key WHERE category = '1.SOC 개발' or category = '2.SOC 검증' or category = '3.SDK 개발' or category = '4.요소/기반 기술' or category = '5.사업자/선행/국책' or category = '6.HW개발' ", con)
project_key = project.values.tolist()
con.close()

#project_role table을 가져옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_role", con)
project_role = project.values.tolist()
con.close()

data = []
for i in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/profields/api/2.0/values/projects/' + str(project_key[i][0]) + '?calculated=true', id_pw)
    data.append(json.loads(url.text))

project_data = []
for i in range(0, len(data)):
    a=[]
    for j in range(len(data[i])):
        if data[i][j]['field']['id'] == -2:#Name
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])
        
        if data[i][j]['field']['id'] == -1:#Key
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])
        
        if data[i][j]['field']['id'] == -5:#PL
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['displayName'].replace('(', ' ').split()[0])
        
        if data[i][j]['field']['id'] == -7:#Category
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['name'])

        if data[i][j]['field']['id'] == 48:#종료보고
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])

        if data[i][j]['field']['id'] == 43:#Chip
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['value'])
        
        if data[i][j]['field']['id'] == 35:#due_date
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])

        if data[i][j]['field']['id'] == 47:#kick_off
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])

        if data[i][j]['field']['id'] == 30:#time_spent
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['formatted'])

        if data[i][j]['field']['id'] == 34:#start_date
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])
        
        if data[i][j]['field']['id'] == 33:#Status
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value']['text'])
        
        if data[i][j]['field']['id'] == 36:#Wiki
            if data[i][j]['value'] is None:
                a.append('')
            else:
                a.append(data[i][j]['value']['value'])
    project_data.append(a)

#project_data에 project_role 추가
for i in range(0, len(project_data)):
    for j in range(0, len(project_role)):
        if project_data[i][1] == project_role[j][0]:
            project_data[i].append(project_role[j][1])
            project_data[i].append(project_role[j][2])


table = pd.DataFrame(project_data, columns=['Project_name', 'Key','PL', 'Category', '종료보고', 'Chip', 'Project_close', 'Kick_off', 'Time_spent', 'Project_start', 'Status',\
                                            'Wiki', 'Sub_PL', 'RIT'])


scope = ['https://spreadsheets.google.com/feeds']
json_file_name = 'C:/Users/B180093/Downloads/intrepid-axe-277609-b37d174aa812.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1gig_5gJ1w3dBSMC16QKXVk_r6NNDYoXu2kEV3ZBW_Vg/edit?usp=sharing'

sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet('project')

worksheet.insert_row(table.columns.tolist(),1)
for i in range(0, len(table.values.tolist())):
    worksheet.insert_row(table.values.tolist()[i],i+2)
    time.sleep(2)
worksheet.resize(len(table.values.tolist()), 4)
