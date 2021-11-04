import requests
import simplejson as json
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pymongo
import calendar

try:
    # pymongo에 접속해서 id, pw data를 가져 옴(rnd_rest_api_account)
    conn = pymongo.MongoClient("192.168.3.237", 27017)
    db = conn.tcs
    col = db.id_pw
    pw_data = col.find({})
    id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}
    
    # user_data document에서 G-leader, CTO, T-Leader를 제외한 연구원들의 정보를 가져옴
    col = db.user_data
    #user_data = list(col.find({"leader": {"$nin": ["G-Leader", "CTO", "T-Leader"]}}))
    user_data = list(col.find({"name": "신호찬 (Chance H Shin)"}))
    #user_data = list(col.find({"team": "Technical Writing Team"}))
    
    url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push'  # 1:1 메시지 Request URL

    col = db.bot_oauth
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'consumerKey': col.find({})[0]['consumerKey'],
        'Authorization': col.find({})[0]['Authorization']
    }
    
    today = datetime.now()  # 현재일시
    #today = datetime.strptime('2021-09-01 10:00:40', '%Y-%m-%d %H:%M:%S')
    year = today.year  # 이번달의 년도
    month = today.month  # 이번달
    date = today.day  # 오늘날짜
    date_count = calendar.monthrange(year, month)[1]  # 이번달 일수
    
    # 이번달 최소 근무시간
    col = db.working_date
    start_date = list(col.find({'$and': [{'year': int(year)}, {'month': int(month)}]}, {'_id': 0}))
    work_date_min = (start_date[0]['working_date']) * 8
    
    # 이번달 최대 근무시간
    work_date_max = int(7.428 * (date_count))
    
    if date == start_date[0]['first_working_date']:
        if month == 1 or month == 4 or month == 7 or month == 10:
    
            # ~ 3개월 달 정보
            month_1b = (today + relativedelta(months=-1)).month
            month_2b = (today + relativedelta(months=-2)).month
            month_3b = (today + relativedelta(months=-3)).month
    
            # ~ 3개월 전 년 정보
            year_1b = (today + relativedelta(months=-1)).year
            year_2b = (today + relativedelta(months=-2)).year
            year_3b = (today + relativedelta(months=-3)).year
    
            # ~ 3개월 전 최소 근무시간
            work_date_min_1b = list(col.find({'$and': [{'year': year_1b}, {'month': month_1b}]}, {'_id': 0}))[0]['working_date'] * 8
            work_date_min_2b = list(col.find({'$and': [{'year': year_2b}, {'month': month_2b}]}, {'_id': 0}))[0]['working_date'] * 8
            work_date_min_3b = list(col.find({'$and': [{'year': year_3b}, {'month': month_3b}]}, {'_id': 0}))[0]['working_date'] * 8
    
            # ~ 3개월 전 최대 근무시간
            work_date_max_1b = int(7.428 * (calendar.monthrange(year_1b, month_1b)[1]))
            work_date_max_2b = int(7.428 * (calendar.monthrange(year_2b, month_2b)[1]))
            work_date_max_3b = int(7.428 * (calendar.monthrange(year_3b, month_3b)[1]))
    
            user_worklog = []
            for i in range(0, len(list(user_data))):
                # -1달 전체 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_1b) + '-' + str(month_1b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No']
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)
    
                time = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                total_time_1b = round(time, 1)
    
                # -1달 휴가 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_1b) + '-' + str(month_1b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No'] + '&extraIssueFilter=issuetype%20%3D%20%ED%9C%B4%EA%B0%80'
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)
    
                time_off = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time_off += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                off_time_1b = round(time_off, 1)
    
                # 전체 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_3b) + '-' + str(month_3b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No']
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)
    
                time = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                total_time = round(time, 1)
    
                # 전체 휴가 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_3b) + '-' + str(month_3b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No'] + '&extraIssueFilter=issuetype%20%3D%20%ED%9C%B4%EA%B0%80'
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)
    
                time_off = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time_off += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                off_time = round(time_off, 1)
    
                # 이름, 사번, 이메일, 전체 worklog, 휴가 worklog 를 리스트로 저장
                user_worklog.append([user_data[i]['name'].split('(')[0].replace(' ', ''), user_data[i]['employee_No'], user_data[i]['email'], str(total_time_1b), str(off_time_1b), str(total_time), str(off_time)])
    
                body = {
                            "accountId": user_worklog[i][2],
                            "content": {
                                "type": "flex",
                                "altText": str(month_1b) + "월 워크로그 안내",
                                "contents": {
                                    "type": "bubble",
                                    "size": "giga",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": user_worklog[i][0] + " 님의 " + str(month_1b) + "월 Worklog 안내드립니다.",
                                                "wrap": True,
                                                "weight": "bold",
                                                "color": "#222222",
                                                "size": "md",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": "총 " + user_worklog[i][3] + "h",
                                                "weight": "bold",
                                                "color": "#222222",
                                                "size": "md",
                                                "margin": "md",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": "업무: " + str(float(user_worklog[i][3]) - float(user_worklog[i][4])) + "h, 휴가: " + user_worklog[i][4] + "h",
                                                "color": "#222222",
                                                "size": "sm",
                                                "margin": "md",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(month_1b) + "월 최소 근무 시간은 " + str(work_date_min_1b) + "h, 최대 근무 시간은 " + str(work_date_max_1b) + "h입니다.",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "wrap": True,
                                                "align": "center",
                                                "margin": "sm"
                                            },
                                            {
                                                "type": "separator",
                                                "margin": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "선택 근로시간제 근무시간은 분기별로 합산하여 준수 여부를 판단합니다.\n이번 분기 (" + str(month_3b) + "월, " +  str(month_2b) + "월, " + str(month_1b) + "월) 기준 근무 시간\n" + " - 최소근무시간 : " + str(work_date_min_3b + work_date_min_2b + work_date_min_1b) + "h, 최대근무시간 : " + str(work_date_max_3b + work_date_max_2b + work_date_max_1b) + "h\n\n" + user_worklog[i][0] + " 님의 " + str(month_3b) + "월, " +  str(month_2b) + "월, " + str(month_1b) + "월 근무시간\n" + " - 총 " + str(round(float(user_worklog[i][5]), 1)) + "h (업무 : " + str(round(float(user_worklog[i][5]) - float(user_worklog[i][6]), 1)) + "h, 휴가 : " + user_worklog[i][6] + "h)",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "wrap": True,
                                                "align": "start",
                                                "margin": "sm"
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "primary",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": str(month_1b) + "월 Worklog 확인",
                                                    "uri": "https://tcs.telechips.com:8443/secure/WPShowTimesheetAction!customTimesheet.jspa#targetType=USER&targetKey=" + user_worklog[i][1] + "&groupingType=Issue&periodMode=MONTH&startDate=" + str(year_1b) + "-" +  str(month_1b) + "-" + "1&endDate=" + str(year_1b) + "-" + str(month_1b) + "-" + str(calendar.monthrange(year_1b, month_1b)[1]) + "&&&periodLocked=false&calendarType=CUSTOM&saveToUserHistory=false&extraIssueFilter=&viewType=TIMESHEET"
                                                    },
                                                "color": "#2432AB"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1~2일 후 " + str(month_1b) + "월 Worklog는 수정할 수 없습니다.",
                                                "color": "#f26400",
                                                "size": "sm",
                                                "align": "center",
                                                "margin": "sm"
                                            }
                                        ],
                                    }
                                }
                            }
                        }

                r = requests.post(url, data=json.dumps(body), headers=headers)
                print(user_worklog[i][0], r, r.text)

        elif month == 2 or month == 5 or month == 8 or month == 11:

            # -1, +1 개월 달 정보
            month_1b = (today + relativedelta(months=-1)).month
            month_1a = (today + relativedelta(months=+1)).month

            # -1, +1 개월 전 년 정보
            year_1b = (today + relativedelta(months=-1)).year
            year_1a = (today + relativedelta(months=+1)).year

            # 분기 최소 근무시간
            work_date_min_1b = list(col.find({'$and': [{'year': year_1b}, {'month': month_1b}]}, {'_id': 0}))[0]['working_date'] * 8
            work_date_min = list(col.find({'$and': [{'year': year}, {'month': month}]}, {'_id': 0}))[0]['working_date'] * 8
            work_date_min_1a = list(col.find({'$and': [{'year': year_1a}, {'month': month_1a}]}, {'_id': 0}))[0]['working_date'] * 8

            # 분기 최대 근무시간
            work_date_max_1b = int(7.428 * (calendar.monthrange(year_1b, month_1b)[1]))
            work_date_max = int(7.428 * (calendar.monthrange(year, month)[1]))
            work_date_max_1a = int(7.428 * (calendar.monthrange(year_1a, month_1a)[1]))

            user_worklog = []
            for i in range(0, len(list(user_data))):
                # -1달 전체 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_1b) + '-' + str(month_1b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No']
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)

                time = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                total_time_1b = round(time, 1)

                # -1달 휴가 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_1b) + '-' + str(month_1b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No'] + '&extraIssueFilter=issuetype%20%3D%20%ED%9C%B4%EA%B0%80'
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)

                time_off = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time_off += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                off_time_1b = round(time_off, 1)

                # 이름, 사번, 이메일, 전체 worklog, 휴가 worklog 를 리스트로 저장
                user_worklog.append([user_data[i]['name'].split('(')[0].replace(' ', ''), user_data[i]['employee_No'], user_data[i]['email'], str(total_time_1b), str(off_time_1b), '0', '0'])

                body = {
                            "accountId": user_worklog[i][2],
                            "content": {
                                "type": "flex",
                                "altText": str(month_1b) + "월 워크로그 안내",
                                "contents": {
                                    "type": "bubble",
                                    "size": "giga",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": user_worklog[i][0] + " 님의 " + str(month_1b) + "월 Worklog 안내드립니다.",
                                                "wrap": True,
                                                "weight": "bold",
                                                "color": "#222222",
                                                "size": "md",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": "총 " + user_worklog[i][3] + "h",
                                                "weight": "bold",
                                                "color": "#222222",
                                                "size": "md",
                                                "margin": "md",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": "업무: " + str(float(user_worklog[i][3]) - float(user_worklog[i][4])) + "h, 휴가: " + user_worklog[i][4] + "h",
                                                "color": "#222222",
                                                "size": "sm",
                                                "margin": "md",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(month_1b) + "월 최소 근무 시간은 " + str(work_date_min_1b) + "h, 최대 근무 시간은 " + str(work_date_max_1b) + "h입니다.",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "wrap": True,
                                                "align": "center",
                                                "margin": "sm"
                                            },
                                            {
                                                "type": "separator",
                                                "margin": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "선택 근로시간제 근무시간은 분기별로 합산하여 준수 여부를 판단합니다.\n이번 분기 (" + str(month_1b) + "월, " +  str(month) + "월, " + str(month_1a) + "월) 기준 근무 시간\n" + " - 최소근무시간 : " + str(work_date_min_1b + work_date_min + work_date_min_1a) + "h, 최대근무시간 : " + str(work_date_max_1b + work_date_max + work_date_max_1a) + "h",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "wrap": True,
                                                "align": "start",
                                                "margin": "sm"
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "primary",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": str(month_1b) + "월 Worklog 확인",
                                                    "uri": "https://tcs.telechips.com:8443/secure/WPShowTimesheetAction!customTimesheet.jspa#targetType=USER&targetKey=" + user_worklog[i][1] + "&groupingType=Issue&periodMode=MONTH&startDate=" + str(year_1b) + "-" +  str(month_1b) + "-" + "1&endDate=" + str(year_1b) + "-" + str(month_1b) + "-" + str(calendar.monthrange(year_1b, month_1b)[1]) + "&&&periodLocked=false&calendarType=CUSTOM&saveToUserHistory=false&extraIssueFilter=&viewType=TIMESHEET"
                                                    },
                                                "color": "#2432AB"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1~2일 후 " + str(month_1b) + "월 Worklog는 수정할 수 없습니다.",
                                                "color": "#f26400",
                                                "size": "sm",
                                                "align": "center",
                                                "margin": "sm"
                                            }
                                        ],
                                    }
                                }
                            }
                        }

                r = requests.post(url, data=json.dumps(body), headers=headers)
                print(user_worklog[i][0], r, r.text)
    
        elif month == 3 or month == 6 or month == 9 or month == 12:
    
            # ~ 2개월 달 정보
            month_1b = (today + relativedelta(months=-1)).month
            month_2b = (today + relativedelta(months=-2)).month

            # ~ 2개월 전 년 정보
            year_1b = (today + relativedelta(months=-1)).year
            year_2b = (today + relativedelta(months=-2)).year

            # 분기 최소 근무시간
            work_date_min = list(col.find({'$and': [{'year': year}, {'month': month}]}, {'_id': 0}))[0]['working_date'] * 8
            work_date_min_1b = list(col.find({'$and': [{'year': year_1b}, {'month': month_1b}]}, {'_id': 0}))[0]['working_date'] * 8
            work_date_min_2b = list(col.find({'$and': [{'year': year_2b}, {'month': month_2b}]}, {'_id': 0}))[0]['working_date'] * 8

            # 분기 최대 근무시간
            work_date_max = int(7.428 * (calendar.monthrange(year, month)[1]))
            work_date_max_1b = int(7.428 * (calendar.monthrange(year_1b, month_1b)[1]))
            work_date_max_2b = int(7.428 * (calendar.monthrange(year_2b, month_2b)[1]))

            user_worklog = []
            for i in range(0, len(list(user_data))):
                # -1달 전체 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_1b) + '-' + str(month_1b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No']
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)
    
                time = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                total_time_1b = round(time, 1)
    
                # -1달 휴가 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_1b) + '-' + str(month_1b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No'] + '&extraIssueFilter=issuetype%20%3D%20%ED%9C%B4%EA%B0%80'
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)
    
                time_off = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time_off += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                off_time_1b = round(time_off, 1)
    
                
                # 전체 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_2b) + '-' + str(month_2b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No']
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)
    
                time = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                total_time = round(time, 1)
    
                # 전체 휴가 워크로그 계산
                url1 = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate=' + str(year_2b) + '-' + str(month_2b) + '-' + '01'
                url2 = '&endDate=' + str(year_1b) + '-' + str(month_1b) + '-' + str(calendar.monthrange(year_1b, month_1b)[1])
                url3 = '&targetKey=' + user_data[i]['employee_No'] + '&extraIssueFilter=issuetype%20%3D%20%ED%9C%B4%EA%B0%80'
                url = url1 + url2 + url3
                data1 = requests.get(url, id_pw)
                data2 = json.loads(data1.text)
    
                time_off = 0
                for j in range(0, len(data2['projects'])):
                    for k in range(0, len(data2['projects'][j]['issues'])):
                        for l in range(0, len(data2['projects'][j]['issues'][k]['workLogs'])):
                            time_off += data2['projects'][j]['issues'][k]['workLogs'][l]['timeSpent']/60/60
                off_time = round(time_off, 1)
    
                # 이름, 사번, 이메일, 전체 worklog, 휴가 worklog 를 리스트로 저장
                user_worklog.append([user_data[i]['name'].split('(')[0].replace(' ', ''), user_data[i]['employee_No'], user_data[i]['email'], str(total_time_1b), str(off_time_1b), str(total_time), str(off_time)])
    
                body = {
                            "accountId": user_worklog[i][2],
                            "content": {
                                "type": "flex",
                                "altText": str(month_1b) + "월 워크로그 안내",
                                "contents": {
                                    "type": "bubble",
                                    "size": "giga",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": user_worklog[i][0] + " 님의 " + str(month_1b) + "월 Worklog 안내드립니다.",
                                                "wrap": True,
                                                "weight": "bold",
                                                "color": "#222222",
                                                "size": "md",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": "총 " + user_worklog[i][3] + "h",
                                                "weight": "bold",
                                                "color": "#222222",
                                                "size": "md",
                                                "margin": "md",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": "업무: " + str(float(user_worklog[i][3]) - float(user_worklog[i][4])) + "h, 휴가: " + user_worklog[i][4] + "h",
                                                "color": "#222222",
                                                "size": "sm",
                                                "margin": "md",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": str(month_1b) + "월 최소 근무 시간은 " + str(work_date_min_1b) + "h, 최대 근무 시간은 " + str(work_date_max_1b) + "h입니다.",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "wrap": True,
                                                "align": "center",
                                                "margin": "sm"
                                            },
                                            {
                                                "type": "separator",
                                                "margin": "sm"
                                            },
                                            {
                                                "type": "text",
                                                "text": "선택 근로시간제 근무시간은 분기별로 합산하여 준수 여부를 판단합니다.\n이번 분기 (" + str(month_2b) + "월, " +  str(month_1b) + "월, " + str(month) + "월) 기준 근무 시간\n" + " - 최소근무시간 : " + str(work_date_min_2b + work_date_min_1b + work_date_min) + "h, 최대근무시간 : " + str(work_date_max_2b + work_date_max_1b + work_date_max) + "h\n\n" + user_worklog[i][0] + " 님의 " + str(month_2b) + "월, " +  str(month_1b) + "월 근무시간\n" + " - 총 " + str(round(float(user_worklog[i][5]), 1)) + "h (업무 : " + str(round(float(user_worklog[i][5]) - float(user_worklog[i][6]), 1)) + "h, 휴가 : " + user_worklog[i][6] + "h)",
                                                "color": "#aaaaaa",
                                                "size": "sm",
                                                "wrap": True,
                                                "align": "start",
                                                "margin": "sm"
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "primary",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": str(month_1b) + "월 Worklog 확인",
                                                    "uri": "https://tcs.telechips.com:8443/secure/WPShowTimesheetAction!customTimesheet.jspa#targetType=USER&targetKey=" + user_worklog[i][1] + "&groupingType=Issue&periodMode=MONTH&startDate=" + str(year_1b) + "-" +  str(month_1b) + "-" + "1&endDate=" + str(year_1b) + "-" + str(month_1b) + "-" + str(calendar.monthrange(year_1b, month_1b)[1]) + "&&&periodLocked=false&calendarType=CUSTOM&saveToUserHistory=false&extraIssueFilter=&viewType=TIMESHEET"
                                                    },
                                                "color": "#2432AB"
                                            },
                                            {
                                                "type": "text",
                                                "text": "1~2일 후 " + str(month_1b) + "월 Worklog는 수정할 수 없습니다.",
                                                "color": "#f26400",
                                                "size": "sm",
                                                "align": "center",
                                                "margin": "sm"
                                            }
                                        ],
                                    }
                                }
                            }
                        }

                r = requests.post(url, data=json.dumps(body), headers=headers)
                print(user_worklog[i][0], r, r.text)
        else:
            False
    else:
        False

    conn.close()

except Exception:
    # 에러 발생시 메신저로 noti
    conn = pymongo.MongoClient("192.168.3.237", 27017)
    db = conn.tcs
    col = db.bot_oauth
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'consumerKey': col.find({})[0]['consumerKey'],
        'Authorization': col.find({})[0]['Authorization']
    }
    conn.close()

    url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push'  # 1:1 메시지 Request URL
    body = {
        'botNo': '1809717',
        'accountId': 'bluenote212@telechips.com',
        'content': {
            'type': 'text',
            'text': 'Lineworks_noti_month_worklog.py 실행 실패했습니다.'
         }
    }
    requests.post(url, data=json.dumps(body), headers=headers)
