#!/usr/bin/env python  
from atlassian import Jira
from atlassian import Confluence
import requests
import simplejson as json
from datetime import datetime
from datetime import timedelta

# 프로젝트 Key
project_list = ['TPD']

# 해당 버전의 전체 이슈 API
allissue1 = 'https://tcs.telechips.com:8443/rest/api/2/version/'
allissue2 = '/relatedIssueCounts'

# 해당 버전의 미해결 이슈 API
unresolvedissue1 = 'https://tcs.telechips.com:8443/rest/api/2/version/'
unresolvedissue2 = '/unresolvedIssueCount'

# ID, PW 정보
username = 'b180093'
password = 'infra4938hc!'
userData = {'os_username': username, 'os_password': password}

# jira auth
jira = Jira(
    url='https://tcs.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

# Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

#TCS에 등록된 모든 프로젝트의 ID를 key, 프로젝트 이름을 value로 정리
project_data = jira.projects(included_archived=None)
r1 = {}
for i in range(0, len(project_data)):
    r1.setdefault(project_data[i]['id'], project_data[i]['name'])
data_project = r1


# TCS 버전정보 Get
version_base = jira.get_project_versions(project_list, expand=None)

# 해당 프로젝트에 입력된 모든 버전의 name, releaseDate, overdue 출력
data_project = {}
for i in range(0, len(project_data)):
    r1 = {}
    r1.setdefault('name', project_data[i]['name'])
    r1.setdefault('key', project_data[i]['key'])
    r1.setdefault('projectcategory', project_data[i]['projectCategory']['name'])
    data_project.setdefault(project_data[i]['id'], r1)

for i in range(0, len(project_list)):
    # TCS 버전정보 Get
    version_base = jira.get_project_versions(project_list[i], expand=None)
    
    # Project에 등록된 version의 정보들을 추출
    for i in range(0, len(version_base)):
        r = {}
        r.setdefault('name', version_base[i]['name'])
        r.setdefault('link', version_base[i]['self'])
        
        if 'releaseDate' in version_base[i]:
            str_releaseDate1 = str(version_base[i]['releaseDate'])
            r.setdefault('duedate', str_releaseDate1)
        else:
            r.setdefault('duedate', '종료일 없음')
    
        if 'overdue' in version_base[i]:
            if version_base[i]['overdue'] is True:
                r.setdefault('status', '지연')
            else:
                r.setdefault('status', '진행중')
    
        if version_base[i]['released'] is True:
            r.setdefault('status', '완료')
        else:
            r.setdefault('status', '진행중')
        
        # TCS 버전에서 전체 이슈 개수 Get
        tcs_r1 = requests.get(allissue1 + version_base[i]['id'] + allissue2, userData)
        allissue = json.loads(tcs_r1.text)
        r.setdefault('allissue', str(allissue['issuesFixedCount']))
        
        # TCS 버전에서 unresolved 이슈 개수 Get
        tcs_r2 = requests.get(unresolvedissue1 + version_base[i]['id'] + unresolvedissue2, userData)
        unsolvedissue = json.loads(tcs_r2.text)
        r.setdefault('unsolvedissue', str(unsolvedissue['issuesUnresolvedCount']))
        
        r.setdefault('projectId', str(version_base[i]['projectId']))
        r.setdefault('projectName', data_project[str(version_base[i]['projectId'])]['name'])
        
        # key는 버전의 id, value는 버전의 name, link, projectId, releaseDate, duedate, status, allissue, unsolvedissue를 저장
        data_version.setdefault(version_base[i]['id'], r)

#print(data_version)


#차트 시작, 종료일을 출력하기 위해 version duedate에서 최대/최소값을 정제
wiki_duedate = []

# version id만 data_version_key에 저장
data_version_key = list(data_version.keys())

# version의 duedate만 리스트로 저장
for i in range(0, len(data_version_key)):
    wiki_duedate.append(data_version[data_version_key[i]]['duedate'])

# Wiki 메인 차트 시작일 추출
project_due_min = min(wiki_duedate)

# version에 등록된 duedate중 최대, 최소값을 뽑기위해 sort
wiki_duedate.sort()
wiki_duedate.reverse()

num = 0
while num < len(wiki_duedate):
    num = num + 1
    if wiki_duedate[num-1] != '종료일 없음':
        # Wiki 메인 차트 종료일 추출
        r_date1 = datetime.strptime(wiki_duedate[num-1], '%Y-%m-%d').date()
        r_date2 = str(r_date1 + timedelta(weeks = 2))
        project_due_max = r_date2
        break

# Wiki 메인 차트 종료일 출력
#print(project_due_max)

# Wiki project 이름 출력
#print(data_version[data_version_key[0]]['projectName'])

# Wiki 차트 colors parameter 색상 데이터 추출
chart_color = ''

for i in range(0, len(data_version_key)):
    if data_version[data_version_key[len(data_version_key) - 1 - i]]['status'] == '완료':
        r_color = ',#000000'
    if data_version[data_version_key[len(data_version_key) - 1 - i]]['status'] == '진행중':
        r_color = ',#3572b0'
    if data_version[data_version_key[len(data_version_key) - 1 - i]]['status'] == '지연':
        r_color = ',#cc1010'
    chart_color = chart_color + r_color

# Wiki 차트  colors parameter 색상 코드 출력
#print(chart_color)

# Wiki pieKeys parameter 데이터 추출
pieKeys_Top = '마일스톤' + '&sbquo;'
pieKeys_Middle = ''
pieKeys_Bottom = 'Today'

for i in range(0, len(data_version_key)):
    r_p = '마일스톤' + ': ' + data_version[data_version_key[len(data_version_key) - 1 - i]]['name'] + '&sbquo;'
    pieKeys_Middle = pieKeys_Middle + r_p

# Wiki pieKeys parameter 출력
#print(pieKeys_Top + pieKeys_Middle + pieKeys_Bottom)

# Wiki 첫번째 table 데이터 추출
tableRow1 = ''
for i in range(0, len(data_version_key)):
    r_t = '<tr><td><span>' + '마일스톤' + '</span></td>' + \
    '<td><span>' + data_version[data_version_key[len(data_version_key) - 1 - i]]['name'] + '</span></td>' +\
    '<td><span>미해결 이슈:' + str(data_version[data_version_key[len(data_version_key) - 1 - i]]['unsolvedissue']) + '</span></td>' + \
    '<td><span>' + data_version[data_version_key[len(data_version_key) - 1 - i]]['duedate'] + '</span></td></tr>'
    tableRow1 = tableRow1 + r_t
# Wiki 첫번째 table 데이터 출력
#print(tableRow1)

# Wiki 두번째 table
tableRow2 = ''
for i in range(0, len(data_version_key)):
    r_t2 = '<tr><td style="text-align: center;" colspan="1"><a href="' + data_version[data_version_key[len(data_version_key) - 1 - i]]['link'] + '">' + \
    data_version[data_version_key[len(data_version_key) - 1 - i]]['name'] + '</a></td><td style="text-align: center;" colspan="1">' + \
    data_version[data_version_key[len(data_version_key) - 1 - i]]['duedate'] + '</td><td style="text-align: center;" colspan="1">' + \
    data_version[data_version_key[len(data_version_key) - 1 - i]]['status'] + '</td><td style="text-align: center;" colspan="1">' + \
    data_version[data_version_key[len(data_version_key) - 1 - i]]['unsolvedissue'] + '</td><td style="text-align: center;" colspan="1">' + \
    data_version[data_version_key[len(data_version_key) - 1 - i]]['allissue'] + '</td><td colspan="1"><br /></td></tr>'
    tableRow2 = tableRow2 + r_t2
#print(tableRow2)

# Wiki 지연중인 이슈 필터 결과
tableRow3 = ''
for i in range(0, len(data_version_key)):
    r_t3 ='<ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="85959282-270a-481c-a73b-82a3b37d96c7"><ac:parameter ac:name="title">' + \
    data_version[data_version_key[len(data_version_key) - 1 - i]]['name'] + ' 마일스톤에서 지연중인 이슈</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="jira" ac:schema-version="1" ac:macro-id="394c50ba-1b13-4a13-9fff-7ff8f112ebe3"><ac:parameter ac:name="server">TCS (Telechips Collaboration System)</ac:parameter><ac:parameter ac:name="columns">key,type,priority,summary,status,creator,assignee,created,updated,start date,due</ac:parameter><ac:parameter ac:name="maximumIssues">20</ac:parameter><ac:parameter ac:name="jqlQuery">fixVersion = ' + \
    data_version_key[i] + ' AND status not in(Resolved,closed) and due &lt; now() ORDER BY due ASC </ac:parameter><ac:parameter ac:name="serverId">1aff8ec6-5d59-3004-8410-8dc6eceba71e</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p><br /></p>'
    tableRow3 = tableRow3 + r_t3

wiki_data = '<p class="auto-cursor-target"><br /></p>\
<ac:structured-macro ac:name="table-chart" ac:schema-version="1" ac:macro-id="4bcd7588-ef4a-45d0-9d87-e5c25bd0b252">\
<ac:parameter ac:name="innerlabels">Percentage</ac:parameter>\
<ac:parameter ac:name="hidecontrols">true</ac:parameter>\
<ac:parameter ac:name="dataorientation">Vertical</ac:parameter>\
<ac:parameter ac:name="legend">right</ac:parameter>\
<ac:parameter ac:name="column">Project&sbquo;Milestone&sbquo;Event&sbquo;Description</ac:parameter>\
<ac:parameter ac:name="aggregation">Start Date&sbquo;End Date&sbquo;Due Date&sbquo;Date</ac:parameter>\
<ac:parameter ac:name="align">Left</ac:parameter>\
<ac:parameter ac:name="type">Gantt</ac:parameter>\
<ac:parameter ac:name="separator">Point (.)</ac:parameter>\
<ac:parameter ac:name="version">3</ac:parameter>\
<ac:parameter ac:name="colors">#ffffff' + \
chart_color + \
',#cc1010</ac:parameter>\
<ac:parameter ac:name="hide">true</ac:parameter><ac:parameter ac:name="xscalestep">1m</ac:parameter>\
<ac:parameter ac:name="tfc-height">250</ac:parameter>\
<ac:parameter ac:name="grid">false</ac:parameter>\
<ac:parameter ac:name="datepattern">yy-mm-dd</ac:parameter>\
<ac:parameter ac:name="pieKeys">' + \
pieKeys_Top + pieKeys_Middle + pieKeys_Bottom + '</ac:parameter>\
<ac:parameter ac:name="id">1561468620660_2129630830</ac:parameter>\
<ac:parameter ac:name="worklog">5|8|w d h m|w d h m</ac:parameter>\
<ac:parameter ac:name="formatVersion">3</ac:parameter>\
<ac:rich-text-body><p class="auto-cursor-target"><br /></p>\
<table><colgroup><col /><col /><col /></colgroup>\
<tbody><tr><th>Project</th><th>Start Date</th><th>End Date</th></tr>\
<tr><td>마일스톤</td><td>' + project_due_min + '</td><td>' + project_due_max + \
'</td></tr></tbody></table><p class="auto-cursor-target"><br /></p><table><colgroup><col /><col /><col /><col /></colgroup>\
<tbody><tr><th>Project</th><th>Milestone</th><th>Description</th><th>Due Date</th></tr>' + \
tableRow1 + \
'</tbody></table><p class="auto-cursor-target"><br /></p>\
<table><colgroup><col /><col /><col /></colgroup>\
<tbody><tr><th>Event</th><th>Description of Event</th><th>Date</th></tr><tr><td>Today</td><td><br /></td><td>today</td></tr></tbody></table>\
<p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>\
<p style="text-align: center;">★ : 완료,&nbsp;<span style="color: rgb(51,102,255);">★</span>&nbsp;: 진행중,&nbsp;<span style="color: rgb(255,0,0);">★</span>&nbsp;: 지연</p>\
<table><colgroup><col /><col /><col /><col /><col /><col /></colgroup><tbody><tr><th style="text-align: center;">Milestone</th><th style="text-align: center;">종료일</th>\
<th style="text-align: center;" colspan="1">상태</th><th style="text-align: center;">미해결 이슈</th><th style="text-align: center;">전체 이슈</th><th style="text-align: center;">특이사항</th></tr>' + \
tableRow2 + \
'</tbody></table><p class="auto-cursor-target"><br /></p><p><br /></p>' + tableRow3

# 현재 날짜 생성
now = datetime.now()
nowdate = ('%s-%s-%s' % (now.year, now.month, now.day))

#print(wiki_data)

'''
# Wiki 페이지 생성
confluence.create_page(
        space='~B180093',
        title= data_version[data_version_key[0]]['projectName'] + ' (' + nowdate + ')',
        body='{0}'.format(wiki_data),
        parent_id=77172264,
        type='page'
    )
'''