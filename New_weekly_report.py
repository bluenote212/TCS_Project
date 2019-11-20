import requests
import sqlite3
import simplejson as json
from datetime import datetime, timedelta
from atlassian import Confluence

username = 'b180093'
password = 'infra4938hc!'
userData = {'os_username': username, 'os_password': password}

#현재 날짜, 일주일 전 날짜 생성
date = datetime.now()
date_1 = date + timedelta(days=-7)
nowdate = date.strftime('%Y-%m-%d')
nowdate_1 = date_1.strftime('%Y-%m-%d')

# 사용자 정보
user = 'B180093'

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
cur = con.cursor()

query = 'SELECT employee_No, name FROM userData WHERE team = "Technology_Planning_Dept";'
cur.execute(query)
userdata = cur.fetchall()
con.close()

#print(userdata[0][0])

#리소스 구하기
url = 'https://tcs.telechips.com:8443/rest/com.deniz.jira.worklog.email/1.0/timesheet/user?startDate='+ nowdate_1 + '&endDate=' + nowdate + '&targetKey=' + user

data1 = requests.get(url, userData)
data2 = json.loads(data1.text)
print(data2)

weekly_data = {}
for i in range(0, len(data2['projects'])):
    issue_data = []
    for j in range(0, len(data2['projects'][i]['issues'])):
        key = data2['projects'][i]['issues'][j]['key']
        summary = data2['projects'][i]['issues'][j]['summary'].replace(",","/")
        time_spent = 0
        for k in range(0, len(data2['projects'][i]['issues'][j]['workLogs'])):
            time_spent = time_spent + data2['projects'][i]['issues'][j]['workLogs'][k]['timeSpent']
        issue_data.append([key, summary, round(time_spent/60/60,1)])
    weekly_data.setdefault(data2['projects'][i]['name'], sorted(issue_data,key=lambda x: x[2], reverse=True))

key = list(weekly_data.keys())

wiki_body = ''
for i in range(0, len(weekly_data)):
    for j in range(0, len(weekly_data[key[i]])):
        wiki_body = wiki_body + '<tr><td>' + key[i] + '</td><td>' + weekly_data[key[i]][j][0] + '</td><td>' + weekly_data[key[i]][j][1] + '</td><td style="text-align: center;">' + str(weekly_data[key[i]][j][2]) + '</td><td><br /></td></tr>'

wiki_data = '<h3><span style="color: rgb(0,0,255);">● 진행한 업무</span></h3>\
<table><colgroup><col /><col /><col /><col /><col /></colgroup>\
<tbody><tr><th style="text-align: center;">프로젝트</th><th style="text-align: center;">Issue Key</th><th style="text-align: center;">Issue Summary</th><th style="text-align: center;">WorkLog(H)</th><th style="text-align: center;">특이사항</th></tr>' + \
wiki_body + \
'</tbody></table><p><span style="color: rgb(0,0,255);"><br /></span></p>\
<h3><span style="color: rgb(0,0,255);">● 이번 주 할 일</span></h3>\
<ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="74dc65d1-aa95-46a2-bca6-5a9bf1be2bdf">\
<ac:rich-text-body><p><ac:structured-macro ac:name="jira" ac:schema-version="1" ac:macro-id="192659b0-28b5-44a5-9c43-bd182b31a1e8">\
<ac:parameter ac:name="server">TCS (Telechips Collaboration System)</ac:parameter>\
<ac:parameter ac:name="columns">priority,type,key,summary,status,start date,due</ac:parameter>\
<ac:parameter ac:name="maximumIssues">20</ac:parameter>\
<ac:parameter ac:name="jqlQuery">(&quot;Start date&quot; &lt;= endofWeek(0) AND duedate &gt;= startOfweek(0) OR &quot;Start date&quot; &gt;= startOfweek(0) AND &quot;Start date&quot; &lt;= endofWeek(0) OR duedate &gt;= startOfweek(0) AND duedate &lt;= endofWeek(0)) AND status not in (Resolved, closed) AND (assignee = b180093 OR Sub_Assignee = ' + \
user + ')   </ac:parameter><ac:parameter ac:name="serverId">1aff8ec6-5d59-3004-8410-8dc6eceba71e</ac:parameter></ac:structured-macro></p>\
</ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p><span style="color: rgb(0,0,255);"><br /></span></p>'

# Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

# Wiki 페이지 생성
confluence.create_page(
        space='TA3',
        title= '신호찬_주간보고',
        body='{0}'.format(wiki_data),
        parent_id=88902085,
        type='page'
    )
