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
        user_worklog.append([user_data[i][0], user_data[i][1], user_data[i][3], str(time_up)]) # 이름, 사번, 이메일, worklog를 리스트로 저장
    for i in range(0, len(user_worklog)):
        text_temp = user_worklog[i][0] + '님은 ' + str(day.month) + '/' + str(day.day)+ '일 (' + day_week + ') ' + ' Worklog를 6h 이하로 입력했습니다.' + \
        '\n누락된 Worklog가 있으면 입력해 주세요 (주말 근무자는 토/일 Worklog도 확인)'
        user_worklog[i].append(text_temp)
        
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
        user_worklog.append([user_data[i][0], user_data[i][1], user_data[i][3], str(time_up)]) # 이름, 사번, 이메일, worklog를 리스트로 저장
    for i in range(0, len(user_worklog)):
        text_temp = user_worklog[i][0] + '님은 ' + str(day.month) + '/' + str(day.day)+ '일 (' + day_week + ') ' + ' Worklog를 6h 이하로 입력했습니다.' + \
        '\n혹시 누락된 Worklog가 있으면 입력해 주세요.'
        user_worklog[i].append(text_temp)


#Line Works Message push URL, header에는 인증 정보
url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push'
headers = {
    'Content-Type' : 'application/json; charset=UTF-8',
    'consumerKey' : 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization' : 'Bearer AAAA/nbEb0dM/5HS9XoOQR2VRvz+sMDtNRlrthxawuCejBN7uKg3Ylx75GbMnDMR0J+vqc9Yo5ACKzsrFrNA8GjN73ea98LqyMlgMsCxrGavZbnaY3JB5qPOkBatmDjfsxgWMzR8f7/sFUacKjOjhDbOAeeT/qlpsZpkmFKrmR9vo/MD9j+zYmbCuXoel6/zkJ56iJ4BJ5JCRELxdwqQk95iO6a4mJUK52/vVSFurNss53uI2NyoFPoyJXzMXbXcLa1enc8oKntUeP35Cy4+ovZs9d83NyVu+2d0rgfQPxPmxf6yYgjBfOKvjb2s4uJggCOd47wl6M5x9UO7QfPAOj+6G/4='
}

#Bot으로 연구원들에게 전날 기록한 worklog를 noti 보냄
for i in range(0, len(user_worklog)):
    if float(user_worklog[i][3]) < float(6):
        payload = {
        'botNo': '1809717',
        'accountId': user_worklog[i][2],
        'content': {
            'type': 'link',
            'contentText': user_worklog[i][4],
            'linkText': 'Worklog 확인',
            'link': 'https://tcs.telechips.com:8443/secure/WPShowTimesheetAction!customTimesheet.jspa?periodMode=WEEK&targetType=USER&calendarType=CUSTOM&groupingType=ISSUE#targetType=USER&targetKey='+ user_data[i][1]\
            + '&groupingType=Issue&periodMode=WEEK&&&periodLocked=false&calendarType=CUSTOM&saveToUserHistory=false&extraIssueFilter=&viewType=TIMESHEET'
         }
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print(r,user_worklog[i][0] + ' : ' + user_worklog[i][3])
    else:
        continue

