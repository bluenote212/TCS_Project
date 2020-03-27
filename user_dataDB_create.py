import requests
import sqlite3
import simplejson as json
import pandas as pd

username = 'b180093'
password = 'infra4938hc!'
userData = {'os_username': username, 'os_password': password}

#Team code
team_code = {
        'SOC_Advanced_Team' : 'DEPT173',
        'SOC_Design_Team' : 'TCW01600',
        'SOC_Verification_Team' : 'DEPT81',
        'RF_Design_Team' : 'TCW02050',
        'SOC_Implementation_Team' : 'TCW01420',
        'Security_Team' : 'TCW02700',
        'System_BSP_Team' : 'TCW02900',
        'Application_BSP_Team' : 'TCW02203',
        'HW_Team' : 'TCW03300',
        'SW_Architecture_Team' : 'DEPT175',
        'Automotive_Platform_Team' : 'TCW02500',
        'CE-Linux_Team' : 'TCW03110',
        'CE-Android_Team' : 'TCW02750',
        'Advanced_Platform_Team' : 'TCW02400',
        'Bluetooth_Team' : 'DEPT75',
        'Wireless_Team' : 'TCW02070',
        'Multimedia_Team' : 'TCW01230',
        'Safety_Team' : 'TCW03100',
        'Technology_Planning_Dept' : 'TCW04300'
        }

team_code_values = list(team_code.values())
team_code_keys = list(team_code.keys())

user_data = []
for i in range(0, len(team_code_keys)):
    resource = requests.get('https://tcs.telechips.com:8443/rest/api/2/group/member?includeInactiveUsers=false&groupname=' + team_code_values[i], userData)
    resource = json.loads(resource.text)
    c = team_code_keys[i]
    for i in range(0, len(resource['values'])):
        a = resource['values'][i]['key']
        b = resource['values'][i]['displayName']
        d = resource['values'][i]['emailAddress']
        user_data.append([a,b,c,d])
        
#user_data의 값을 DB에 저장
table = pd.DataFrame(user_data, columns=['employee_No', 'name', 'team', 'email'])
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
table.to_sql('userData', con, if_exists='replace', index=False)
con.close()
