import requests
import sqlite3
import simplejson as json
import pandas as pd

username = 'b180093'
password = 'infra4938hC!'
userData = {'os_username': username, 'os_password': password}

#Team code
team_code = [
        ['SOC_Advanced_Team', 'DEPT173'],
        ['SOC_IP_Design_Team', 'DEPT188'],
        ['SOC_Design_Team', 'TCW01600'],
        ['SOC_Verification_Team', 'DEPT81'],
        ['SOC_Implementation_Team', 'TCW01420'],
        ['HW Platform Team', 'TCW03300'],
        ['HW Verification Team', 'DEPT180'],
        ['System_BSP_Team', 'TCW02900'],
        ['Application_BSP_Team', 'TCW02203'],
        ['Security_solution_Team', 'TCW02700'],
        ['Media_Android Team', 'DEPT182'],
        ['Media_Linux Team', 'TCW01230'],
        ['Media_HAL Team', 'DEPT183'],
        ['Automotive_MCU Team', 'TCW03100'],
        ['Wireless_Team', 'TCW02070'],
        ['Bluetooth_Team', 'DEPT75'],
        ['SW_Architecture_Team', 'DEPT175'],
        ['Project_Management_Team', 'DEPT184'],
        ['STB_Platform_Team', 'TCW03110'],
        ['Automotive_Platform_Team', 'TCW02500'],
        ['Driver_Assistance_Platform_Team', 'TCW02400'],
        ['RND_Innovation_Team', 'TCW04300'],
        ['Technical_Writing_Team' ,'DEPT186']
        ]

user_data = []
for i in range(0, len(team_code)):
    resource = requests.get('https://tcs.telechips.com:8443/rest/api/2/group/member?groupname=' + str(team_code[i][1]), userData)
    data = json.loads(resource.text)
    c = team_code[i][0]
    for i in range(0, len(data['values'])):
        a = data['values'][i]['key']
        b = data['values'][i]['displayName']
        d = data['values'][i]['emailAddress']
        user_data.append([a,b,c,d])
        
#user_data의 값을 DB에 저장
table = pd.DataFrame(user_data, columns=['employee_No', 'name', 'team', 'email'])
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
table.to_sql('userData', con, if_exists='replace', index=False)
con.close()