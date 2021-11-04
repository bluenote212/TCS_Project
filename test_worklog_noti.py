import requests
import simplejson as json
from datetime import datetime, timedelta
import pymongo

#pymongo에 접속해서 id, pw data를 가져 옴(rnd_rest_api_account)
conn = pymongo.MongoClient("192.168.3.237", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}

#user_data document에서 G-leader, CTO, T-Leader를 제외한 연구원들의 정보를 가져옴
col = db.user_data
user_data = list(col.find({"employee_No": "b180093"}))
#user_data = list(col.find({"leader":{"$nin":["T-Leader", "G-Leader","CTO"]}}))

#오늘이 무슨요일인지 week 변수에 저장
week = datetime.now().weekday()
user_worklog = []

#Line Works Message push URL, header에는 인증 정보
url_message = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push'
headers = {
    'Content-Type' : 'application/json; charset=UTF-8',
    'consumerKey' : 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization': 'Bearer AAABAXONcN0Ch9T4YmhyDiRG+1ilvRZoM1MoutdUZLzV6++m3h+/fipKAlD0I1OKCbAJFWhuiQV07ldyuY1M3qu0pVEKqWcrhPdK5k2PKp2Xo42bfFsPleMt8D0+ZHqJVGrXPdw3JheNM5hkVqpzEc0l24vlpymIeLTg74+aEUFa+SpI6mjkbP5vJwD5kR8auewDnQgmuE1cwdBVlveJq2ZDC7ohbAF29Hfd/Wmc75h72LAC3W1Zea+4LF/UpKoBnSxCmqSInyWmyYwAJ5HBrPp/9PdoxB5SqRma2aFswhmwvaR/6AClqjmuAKdGlcgA+DertSmLCCer7i2iNXxNimgqXsrvEAHQQpLwtrv8IGdcV/sf'
}

#오늘 날짜가 월요일인 경우 금요일의 worklog를 보내는 분기
if week == 0:
    day = datetime.now() + timedelta(days=-3)
    col = db.working_date
    month_holiday = list(col.find({"$and": [{"year": day.year}, {"month": day.month}]}))
    
    if not(str(day.day) in month_holiday[0]["holiday"]):
        day_week = '금요일'
    
        #쿼리 조건에 맞는 연구원들 어제의 worklog 계산
        for i in range(0, len(list(user_data))):
            url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate='+ str(day.year) + '-' + str(day.month) + '-' + str(day.day)
            url2 = '&endDate='+ str(day.year) + '-' + str(day.month) + '-' + str(day.day)
            url3 = '&targetKey=' + user_data[i]['employee_No']
            url_total = url1 + url2  + url3
            data1 = requests.get(url_total, id_pw)
            data2 = json.loads(data1.text)
    
            time = 0
            for j in range(0, len(data2['projects'])):
                for k in range(0, len(data2['projects'][j]['issues'])):
                    for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                        time += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
            time_up = round(time,1)#소수점 한자리까지 반올림
            user_worklog.append([user_data[i]['name'], user_data[i]['employee_No'], user_data[i]['email'], str(time_up)]) # 이름, 사번, 이메일, worklog를 리스트로 저장
        for i in range(0, len(user_worklog)):
            text_temp = user_worklog[i][0] + '님은 ' + str(day.month) + '/' + str(day.day)+ '일 (' + day_week + ') ' + ' Worklog를 6h 이하로 입력했습니다.' + \
            '\n누락된 Worklog가 있으면 입력해 주세요 (주말 근무자는 토/일 Worklog도 확인)'
            user_worklog[i].append(text_temp)
        
        #Bot으로 연구원들에게 전날 기록한 worklog를 noti 보냄
        for i in range(0, len(user_worklog)):
            if float(user_worklog[i][3]) < float(6):
                payload = {
                'botNo': '1809717',
                #'accountId': user_worklog[i][2],
                'accountId': 'bluenote212@telechips.com',
                'content': {
                    'type': 'link',
                    'contentText': user_worklog[i][4],
                    'linkText': 'Worklog 확인',
                    'link': 'https://tcs.telechips.com:8443/secure/WPShowTimesheetAction!customTimesheet.jspa?periodMode=WEEK&targetType=USER&calendarType=CUSTOM&groupingType=ISSUE#targetType=USER&targetKey='+ user_worklog[i][1]\
                    + '&groupingType=Issue&periodMode=WEEK&&&periodLocked=false&calendarType=CUSTOM&saveToUserHistory=false&extraIssueFilter=&viewType=TIMESHEET'
                 }
                }
                r = requests.post(url_message, data=json.dumps(payload), headers=headers)
                print(r,user_worklog[i][0] + ' : ' + user_worklog[i][3])
            else:
                continue
    else:
        False

#오늘 날짜가 월요일이 아닌경우
else:
    day = datetime.now() + timedelta(days=-1)#어제 날짜 계산
    col = db.working_date
    month_holiday = list(col.find({"$and": [{"year": day.year}, {"month": day.month}]}))
    
    if not(str(day.day) in month_holiday[0]["holiday"]):
        if week == 1:
            day_week = '월요일'
        elif week == 2:
            day_week = '화요일'
        elif week == 3:
            day_week = '수요일'
        else:
            day_week = '목요일'
        #쿼리 조건에 맞는 연구원들 어제의 worklog 계산
    
        for i in range(0, len(list(user_data))):
            url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate='+ str(day.year) + '-' + str(day.month) + '-' + str(day.day)
            url2 = '&endDate='+ str(day.year) + '-' + str(day.month) + '-' + str(day.day)
            url3 = '&targetKey=' + user_data[i]['employee_No']
            
            url_total = url1 + url2  + url3
            data1 = requests.get(url_total, id_pw)
            data2 = json.loads(data1.text)
        
            time = 0
            for j in range(0, len(data2['projects'])):
                for k in range(0, len(data2['projects'][j]['issues'])):
                    for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                        time += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
            time_up = round(time,1)
            user_worklog.append([user_data[i]['name'], user_data[i]['employee_No'], user_data[i]['email'], str(time_up)]) # 이름, 사번, 이메일, worklog를 리스트로 저장
        for i in range(0, len(user_worklog)):
            text_temp = user_worklog[i][0] + '님은 ' + str(day.month) + '/' + str(day.day)+ '일 (' + day_week + ') ' + ' Worklog를 6h 이하로 입력했습니다.' + \
            '\n혹시 누락된 Worklog가 있으면 입력해 주세요.'
            user_worklog[i].append(text_temp)
        
        #Bot으로 연구원들에게 전날 기록한 worklog를 noti 보냄
        for i in range(0, len(user_worklog)):
            if float(user_worklog[i][3]) < float(6):
                payload = {
                'botNo': '1809717',
                #'accountId': user_worklog[i][2],
                'accountId': 'bluenote212@telechips.com',
                'content': {
                    'type': 'link',
                    'contentText': user_worklog[i][4],
                    'linkText': 'Worklog 확인',
                    'link': 'https://tcs.telechips.com:8443/secure/WPShowTimesheetAction!customTimesheet.jspa?periodMode=WEEK&targetType=USER&calendarType=CUSTOM&groupingType=ISSUE#targetType=USER&targetKey='+ user_worklog[i][1]\
                    + '&groupingType=Issue&periodMode=WEEK&&&periodLocked=false&calendarType=CUSTOM&saveToUserHistory=false&extraIssueFilter=&viewType=TIMESHEET'
                 }
                }
                r = requests.post(url_message, data=json.dumps(payload), headers=headers)
                print(r,user_worklog[i][0] + ' : ' + user_worklog[i][3])
            else:
                continue
conn.close()
