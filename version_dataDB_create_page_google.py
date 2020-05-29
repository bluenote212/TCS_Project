import sqlite3
import pandas as pd
import requests
import simplejson as json
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()

id_pw = {'os_username' : user_info[0][0], 'os_password' : user_info[0][1]}

#project category table에서 category 선별해서 프로젝트 key를 가져 옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_key WHERE category = '1.SOC 개발' or category = '2.SOC 검증' or category = '3.SDK 개발' or category = '4.요소/기반 기술' or category = '5.사업자/선행/국책' or category = '6.HW개발' ", con)
project_key = project.values.tolist()
con.close()

version_data = []
for i in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/projects/1.0/project/' + project_key[i][0] + '/release/allversions', id_pw)
    version = json.loads(url.text)
    if len(version) != 0:
        for j in range(0, len(version)):
            temp = []
            if version[j]['released'] == True:
                status = 'Released'
            else:
                status = 'Unreleased'
            if version[j]['overdue'] == True:
                overdue = '지연'
            else:
                overdue = ''
            url2 = requests.get('https://tcs.telechips.com:8443/rest/api/2/search?jql=duedate%3Cnow()%20and%20fixVersion%3D'+ version[j]['id'] +'&maxResults=1&fields=1', id_pw)
            duedate = json.loads(url2.text)
            if version[j]['startDate']['formatted'] == '' or version[j]['releaseDate']['formatted'] == '':
                days = 0
            else:
                d = datetime.strptime(version[j]['releaseDate']['formatted'], '%Y-%m-%d') - datetime.strptime(version[j]['startDate']['formatted'], '%Y-%m-%d')
                days = d.days
            temp = [
                    project_key[i][0],
                    version[j]['id'],
                    version[j]['name'],
                    version[j]['description'],
                    version[j]['startDate']['formatted'],
                    version[j]['releaseDate']['formatted'],
                    status,
                    duedate['total'],
                    version[j]['status']['complete']['count'],
                    version[j]['status']['unmapped']['count'] + version[j]['status']['toDo']['count'] + version[j]['status']['inProgress']['count'] + version[j]['status']['complete']['count'],
                    overdue,
                    str(days)
                    ]
            version_data.append(temp)

data = pd.DataFrame(version_data, columns = ['Key', 'id', 'name', 'description', 'start_date', 'release_date', 'status', 'duedate_over_issue', 'resolved_issue',\
                                             'total_issue', 'overdue', 'days'])

scope = ['https://spreadsheets.google.com/feeds']
json_file_name = 'C:/Users/B180093/Downloads/intrepid-axe-277609-b37d174aa812.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1gig_5gJ1w3dBSMC16QKXVk_r6NNDYoXu2kEV3ZBW_Vg/edit?usp=sharing'

sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet('version')

worksheet.insert_row(data.columns.tolist(),1)
for i in range(0, len(data.values.tolist())):
    worksheet.insert_row(data.values.tolist()[i],i+2)
    time.sleep(2)
worksheet.resize(len(data.values.tolist()), 13)
