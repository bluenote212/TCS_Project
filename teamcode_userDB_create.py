import requests
import sqlite3
import simplejson as json
import pandas as pd

#userdata를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#Team code
team_code = [
        ['SOC Advanced Team', '4', 'TMSAT', 'DEPT173'],
        ['SOC IP Design Team', '95', 'TMIDT', 'DEPT188'],
        ['SOC Design Team', '5', 'TMSDT', 'TCW01600'],
        ['SOC Verification Team', '6', 'TMSVT', 'DEPT81'],
        ['SOC Implementation Team', '8', 'TMSIT', 'TCW01420'],
        ['HW Platform Team', '87', 'TMHWT', 'TCW03300'],
        ['HW Verification Team', '88', 'TMHVT', 'DEPT180'],
        ['System BSP Team', '10', 'TMBSP', 'TCW02900'],
        ['Application BSP Team', '11', 'TMABT', 'TCW02203'],
        ['Security Solution Team', '9', 'TMSEC', 'TCW02700'],
        ['Automotive MCU Team', '22', 'TMST', 'TCW03100'],
        ['Audio Technology Team', '100', 'TMAT', 'DEPT196'],
        ['Media Android Team', '89', 'TMMT', 'DEPT182'],
        ['Media Linux Team', '90', 'TMMLT', 'TCW01230'],
        ['Media HAL Team', '91', 'TMMHT', 'DEPT183'],
        ['SW Architecture Team', '14', 'TMSAT2', 'DEPT175'],
        ['STB Platform Team', '93', 'TMCAT', 'TCW03110'],
        ['Automotive Platform Team', '15', 'TMAPT', 'TCW02500'],
        ['Driver Assistance Platform Team', '18', 'TMAPT2', 'TCW02400'],
        ['Core Technology Team', '101', 'TMCT', 'DEPT75'],
        ['Project Management Team', '92', 'TMPMT', 'DEPT184'],
        ['RND Innovation Team', '2', 'TMTPD', 'TCW04300'],
        ['Technical Writing Team', '94', 'TMTWT','DEPT186']
        ]

data = pd.DataFrame(team_code, columns = ['team', 'team_code', 'project_key','group_code'])

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('team_code', con, if_exists='replace', index = False)
con.close()

user_data = []
for i in range(0, len(team_code)):
    resource = requests.get('https://tcs.telechips.com:8443/rest/api/2/group/member?includeInactiveUsers=false&groupname=' + team_code[i][3], id_pw)
    data = json.loads(resource.text)
    c = team_code[i][0]
    for i in range(0, len(data['values'])):
        a = data['values'][i]['displayName']
        b = data['values'][i]['key']        
        d = data['values'][i]['emailAddress']
        user_data.append([a,b,c,d])

user_data.append(['송봉기 (BongGee Song)','b150137','CTO','bgsong@telechips.com'])
#user_data.append(['김문수 (Moonsoo Kim)','b020069','Group Leader','mskim@telechips.com']) 팀장님 겸임으로 추가하지 않아도 됨
user_data.append(['최재순 (JS Choi)','b030187','Group Leader','arm7@telechips.com'])
user_data.append(['노호식 (Hosi Roh)','b050120','Group Leader','rohhosik@telechips.com'])
user_data.append(['이재호 (Justin Lee)','b030240','Group Leader','jhlee17@telechips.com'])
user_data.append(['장지연 (Patrick Jang)','a990059','Group Leader','zerocool@telechips.com'])
user_data.append(['이영종 (Daxter Lee)','b050109','Group Leader','yjrobot@telechips.com'])
        
#user_data의 값을 DB에 저장
table = pd.DataFrame(user_data, columns=['name', 'employee_No', 'team', 'email'])
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
table.to_sql('userData', con, if_exists='replace', index=False)
con.close()

