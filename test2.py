import requests
import sqlite3
import simplejson as json
import pandas as pd

#userdata를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
userData = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#Team code
team_code = [
        ['SOC Advanced Team', 'DEPT173'],
        ['SOC IP Design Team', 'DEPT188'],
        ['SOC Design Team', 'TCW01600'],
        ['SOC Verification Team', 'DEPT81'],
        ['SOC Implementation Team', 'TCW01420'],
        ['HW Platform Team', 'TCW03300'],
        ['HW Verification Team', 'DEPT180'],
        ['System BSP Team', 'TCW02900'],
        ['Application BSP Team', 'TCW02203'],
        ['Security solution Team', 'TCW02700'],
        ['Media Android Team', 'DEPT182'],
        ['Media Linux Team', 'TCW01230'],
        ['Media HAL Team', 'DEPT183'],
        ['Automotive MCU Team', 'TCW03100'],
        ['Wireless Team', 'TCW02070'],
        ['Bluetooth Team', 'DEPT75'],
        ['SW Architecture Team', 'DEPT175'],
        ['Project Management Team', 'DEPT184'],
        ['STB Platform Team', 'TCW03110'],
        ['Automotive Platform Team', 'TCW02500'],
        ['Driver Assistance Platform Team', 'TCW02400'],
        ['RND Innovation Team', 'TCW04300'],
        ['Technical Writing Team' ,'DEPT186']
        ]

user_data = []
for i in range(0, len(team_code)):
    resource = requests.get('https://tcs.telechips.com:8443/rest/api/2/group/member?groupname=' + team_code[i][1], userData)
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
