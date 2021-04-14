import requests
import sqlite3
import simplejson as json
from datetime import datetime, timedelta
import pandas as pd

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#sql = "SELECT * FROM userData WHERE name='신호찬 (Chance H Shin)'"
#sql = "SELECT * FROM userData WHERE team='RND Innovation Team'"
sql = "SELECT * FROM userData WHERE team NOT in('Group Leader','CTO')"

#user_data를 DB에서 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user_data = pd.read_sql(sql, con) # WHERE 조건 확인
con.close()
user_data = user_data.values.tolist()

#어제 날짜 출력
week = datetime.now().weekday()
user_worklog = []

if week == 0:
    day = datetime.now() + timedelta(days=-3)
    day_week = '금요일'
    #쿼리 조건에 맞는 연구원들 어제의 worklog 계산
    for i in range(0, len(user_data)):
        url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate='+ str(day.year) + '-' + str(day.month) + '-' + str(day.day)
        url2 = '&endDate='+ str(day.year) + '-' + str(day.month) + '-' + str(day.day)
        url3 = '&targetKey=' + user_data[i][1]
        url = url1 + url2  + url3
        data1 = requests.get(url, id_pw)
        data2 = json.loads(data1.text)
    
        time = 0
        for j in range(0, len(data2['projects'])):
            for k in range(0, len(data2['projects'][j]['issues'])):
                for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                    time += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
        time_up = round(time,1)
        user_worklog.append([user_data[i][0], user_data[i][2], str(time_up)]) #
else:
    day = datetime.now() + timedelta(days=-1)
    if week == 1:
        day_week = '월요일'
    elif week == 2:
        day_week = '화요일'
    elif week == 3:
        day_week = '수요일'
    else:
        day_week = '목요일'
    #쿼리 조건에 맞는 연구원들 어제의 worklog 계산
    for i in range(0, len(user_data)):
        url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate='+ str(day.year) + '-' + str(day.month) + '-' + str(day.day)
        url2 = '&endDate='+ str(day.year) + '-' + str(day.month) + '-' + str(day.day)
        url3 = '&targetKey=' + user_data[i][1]
        url = url1 + url2  + url3
        data1 = requests.get(url, id_pw)
        data2 = json.loads(data1.text)
    
        time = 0
        for j in range(0, len(data2['projects'])):
            for k in range(0, len(data2['projects'][j]['issues'])):
                for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                    time += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
        time_up = round(time,1)
        user_worklog.append([user_data[i][0], user_data[i][2], str(time_up)]) # 이름, 사번, 이메일, worklog를 리스트로 저장

SOC_Advanced_Team = ''
SOC_IP_Design_Team = ''
SOC_Design_Team = ''
SOC_Implementation_Team = ''
HW_Platform_Team = ''
HW_Verification_Team = ''
System_BSP_Team = ''
Application_BSP_Team = ''
Automotive_MCU_Team = ''
Audio_Technology_Team = ''
Media_Android_Team = ''
Media_Linux_Team = ''
Media_HAL_Team = ''
Automotive_Platform_Team = ''
Project_Management_Team = ''
RND_Innovation_Team = ''

#각 팀별 worklog noti text 저장
for i in range(len(user_worklog)):
    if user_worklog[i][1] == 'SOC Advanced Team':
        SOC_Advanced_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'

    elif user_worklog[i][1] == 'SOC IP Design Team':
        SOC_IP_Design_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'SOC Design Team':
        SOC_Design_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'SOC Implementation Team':
        SOC_Implementation_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'HW Platform Team':
        HW_Platform_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'HW Verification Team':
        HW_Verification_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
    
    elif user_worklog[i][1] == 'System BSP Team':
        System_BSP_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'Application BSP Team':
        Application_BSP_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
    
    elif user_worklog[i][1] == 'Automotive MCU Team':
        Automotive_MCU_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'Audio Technology Team':
        Audio_Technology_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'Media Android Team':
        Media_Android_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'Media Linux Team':
        Media_Linux_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'Media HAL Team':
        Media_HAL_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'Automotive Platform Team':
        Automotive_Platform_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'Project Management Team':
        Project_Management_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'
         
    elif user_worklog[i][1] == 'RND Innovation Team':
        RND_Innovation_Team += user_worklog[i][0] + ' : ' + user_worklog[i][2] + 'h\n'

team_worklog = [
        [SOC_Advanced_Team, 'jongsang.choi@telechips.com'],
        [SOC_IP_Design_Team, 'mskim@telechips.com'],
        [SOC_Design_Team, 'wang@telechips.com'],
        [SOC_Implementation_Team, 'orionpark@telechips.com'],
        [HW_Platform_Team, 'anykim@telechips.com'],
        [HW_Verification_Team, 'kmw21c@telechips.com'],
        [System_BSP_Team, 'hjjang@telechips.com'],
        [Application_BSP_Team, 'nuekii@telechips.com'],
        [Automotive_MCU_Team, 'yhkim602@telechips.com'],
        [Audio_Technology_Team, 'yhyoun@telechips.com'],
        [Media_Android_Team, 'zzau@telechips.com'],
        [Media_Linux_Team, 'send2u77@telechips.com'],
        [Media_HAL_Team, 'biho17@telechips.com'],
        [Automotive_Platform_Team, 'jim@telechips.com'],
        [Project_Management_Team, 'bluecafe@telechips.com'],
        [RND_Innovation_Team, 'youngjochoi@telechips.com']
        ]

#Line Works Message push URL, header에는 인증 정보
url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push'
headers = {
    'Content-Type' : 'application/json; charset=UTF-8',
    'consumerKey' : 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization': 'Bearer AAABAXONcN0Ch9T4YmhyDiRG+1ilvRZoM1MoutdUZLzV6++m3h+/fipKAlD0I1OKCbAJFWhuiQV07ldyuY1M3qu0pVEKqWcrhPdK5k2PKp2Xo42bfFsPleMt8D0+ZHqJVGrXPdw3JheNM5hkVqpzEc0l24vlpymIeLTg74+aEUFa+SpI6mjkbP5vJwD5kR8auewDnQgmuE1cwdBVlveJq2ZDC7ohbAF29Hfd/Wmc75h72LAC3W1Zea+4LF/UpKoBnSxCmqSInyWmyYwAJ5HBrPp/9PdoxB5SqRma2aFswhmwvaR/6AClqjmuAKdGlcgA+DertSmLCCer7i2iNXxNimgqXsrvEAHQQpLwtrv8IGdcV/sf'
}

for i in range(0, len(team_worklog)):
    payload = {
    'botNo': '1809717',
    'accountId': team_worklog[i][1],
    #'accountId': 'bluenote212@telechips.com',
    'content': {
        'type': 'text',
        'text': str(day.month) + '/' + str(day.day)+ '일 (' + day_week + ') Team Worklog 현황입니다.\n' + team_worklog[i][0],
     }
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r)
    
