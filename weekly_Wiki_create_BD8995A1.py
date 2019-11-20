#!/usr/bin/env python3
import pandas as pd
import sqlite3
from atlassian import Confluence
import datetime
import requests
import json

username = 'b180093'
password = 'infra4938hc!'

# 프로젝트 Key
project_list = ['BD8995A1']

# Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

#현재 날짜 생성
date = datetime.datetime.now()
nowdate = date.strftime('%Y-%m-%d')

#------------------------------ DB에서 원하는 값을 추출-------------------#
#DB 연결하여 data import
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
table_version = pd.read_sql('select * from ' + project_list[0], con)
#Dataframe에서 index값을 list로 추출
data_index = table_version.index.tolist()

table_project = pd.read_sql('select * from project_info where projectKey="' + table_version.loc[data_index[0]]['projectKey'] + '"', con)
con.close()

#print(table_project.loc[data_index[0]]['projectLead'])

# Wiki 차트 colors parameter 색상 데이터 추출
chart_color = ''
for i in range(0, len(data_index)):
    if table_version.loc[data_index[i]]['status'] == '완료':
        r_color = ',#000000'
    if table_version.loc[data_index[i]]['status'] == '진행중':
        r_color = ',#3572b0'
    if table_version.loc[data_index[i]]['status'] == '지연':
        r_color = ',#cc1010'
    chart_color = chart_color + r_color

# Wiki 차트  colors parameter 색상 코드 출력
#print(chart_color)

# Wiki pieKeys parameter 데이터 추출
pieKeys_Top = '마일스톤' + '&sbquo;'
pieKeys_Middle = ''
pieKeys_Bottom = 'Today</ac:parameter>'

for i in range(0, len(data_index)):
    r_p = '마일스톤' + ': ' + table_version.loc[data_index[i]]['name'].replace('&','&amp;') + '&sbquo;'
    pieKeys_Middle = pieKeys_Middle + r_p

# Wiki pieKeys parameter 출력
#print(pieKeys_Middle)

# Wiki 첫번째 table 데이터 추출
tableRow1 = ''
for i in range(0, len(data_index)):
    r_t = '<tr><td>' + '마일스톤' + '</td>' + \
    '<td>' + table_version.loc[data_index[i]]['name'].replace('&','&amp;') + '</td>' +\
    '<td>' + table_version.loc[data_index[i]]['duedate'] + '</td></tr>'
    tableRow1 = tableRow1 + r_t
# Wiki 첫번째 table 데이터 출력
#print(tableRow1)

# Wiki 두번째 table
tableRow2 = ''
for i in range(0, len(data_index)):
    r_t2 = '<tr><td style="text-align: center;" colspan="1"><a href="https://tcs.telechips.com:8443/projects/' + project_list[0] + '/versions/' + \
    table_version.loc[data_index[i]]['versionId'] + '">' + \
    table_version.loc[data_index[i]]['name'].replace('&','&amp;') + '</a></td><td style="text-align: center;" colspan="1">' + \
    table_version.loc[data_index[i]]['duedate'] + '</td><td style="text-align: center;" colspan="1">' + \
    table_version.loc[data_index[i]]['status'] + '</td><td style="text-align: center;" colspan="1">' + \
    table_version.loc[data_index[i]]['unsolvedissue'] + '</td><td style="text-align: center;" colspan="1">' + \
    table_version.loc[data_index[i]]['allissue'] + '</td><td style="text-align: center;" colspan="1">' + \
    '<a style="text-align: center;" href="https://tcs.telechips.com:8443/issues/?jql=status%20not%20in(Closed%2C%20Resolved)%20and%20duedate%20%3C%20' + nowdate + '%20and%20fixVersion%20%3D%20' + \
    table_version.loc[data_index[i]]['versionId'] + '">' + table_version.loc[data_index[i]]['delayIssue'] + '</a></td><td colspan="1"><br /></td></tr>'
    tableRow2 = tableRow2 + r_t2
#print(tableRow2)

wiki_data = '<h3><span style="color: rgb(0,0,255);">●&nbsp;<strong>주간보고 작성 상태</strong></span></h3>\
<ac:structured-macro ac:name="details" ac:schema-version="1" ac:macro-id="dad5accd-f050-4efc-912b-99a154537cd7">\
<ac:rich-text-body><p class="auto-cursor-target"><br /></p><table><colgroup><col /><col /></colgroup>\
<tbody><tr><th style="text-align: center;">주간 보고 생성</th><th style="text-align: center;">주간 보고 작성</th></tr>\
<tr><td style="text-align: center;"><div class="content-wrapper"><p>\
<ac:structured-macro ac:name="status" ac:schema-version="1" ac:macro-id="40d00797-b7a1-4bd3-9341-7b844da2dfd8">\
<ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">Complete</ac:parameter><ac:parameter ac:name="" />\
</ac:structured-macro></p></div></td><td style="text-align: center;"><br /></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>\
</ac:rich-text-body></ac:structured-macro>\
<h3><span style="color: rgb(0,0,255);"><strong>●&nbsp;</strong>\
<strong>프로젝트 주요 일정</strong>\
</span></h3><ac:structured-macro ac:name="table-chart" ac:schema-version="1" ac:macro-id="46d60b38-2591-4d13-9b68-8d7e9c0f3064">\
<ac:parameter ac:name="innerlabels">Percentage</ac:parameter>\
<ac:parameter ac:name="hidecontrols">true</ac:parameter>\
<ac:parameter ac:name="dataorientation">Vertical</ac:parameter>\
<ac:parameter ac:name="legend">right</ac:parameter>\
<ac:parameter ac:name="column">Project&sbquo;Milestone&sbquo;Event</ac:parameter>\
<ac:parameter ac:name="aggregation">Start Date&sbquo;End Date&sbquo;Due Date&sbquo;Date</ac:parameter>\
<ac:parameter ac:name="align">Center</ac:parameter>\
<ac:parameter ac:name="type">Gantt</ac:parameter><ac:parameter ac:name="separator">Point (.)</ac:parameter>\
<ac:parameter ac:name="version">3</ac:parameter>\
<ac:parameter ac:name="colors">#ffffff' + chart_color + \
',#cc1010</ac:parameter>\
<ac:parameter ac:name="hide">true</ac:parameter>\
<ac:parameter ac:name="tfc-height">200</ac:parameter>\
<ac:parameter ac:name="grid">false</ac:parameter>\
<ac:parameter ac:name="datepattern">yy-mm-dd</ac:parameter>\
<ac:parameter ac:name="pieKeys">' + pieKeys_Top + pieKeys_Middle + pieKeys_Bottom + \
'<ac:parameter ac:name="id">1562303225565_213485116</ac:parameter>\
<ac:parameter ac:name="worklog">5|8|w d h m|w d h m</ac:parameter>\
<ac:parameter ac:name="formatVersion">3</ac:parameter>\
<ac:rich-text-body><p class="auto-cursor-target"><br /></p>\
<table><colgroup><col /><col /><col /></colgroup><tbody><tr><th>Project</th><th>Start Date</th><th>End Date</th></tr>' + \
'<tr><td>마일스톤</td><td>' + table_project.loc[data_index[0]]['startDate'] + '</td><td>' + \
table_project.loc[data_index[0]]['endDate'] + \
'</td></tr></tbody></table><p class="auto-cursor-target"><br /></p>\
<table><colgroup><col /><col /><col /></colgroup><tbody><tr><th>Project</th><th>Milestone</th><th>Due Date</th></tr>' + \
tableRow1 + '</tbody></table><p class="auto-cursor-target"><br /></p>\
<table><colgroup><col /><col /></colgroup><tbody><tr><th>Event</th><th>Date</th></tr><tr><td>Today</td>\
<td>today</td></tr></tbody></table>\
<p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro>\
<p style="text-align: center;">★ : 완료,&nbsp;<span style="color: rgb(51,102,255);">★</span>&nbsp;: 진행중,&nbsp;\
<span style="color: rgb(255,0,0);">★</span>&nbsp;: 지연</p>\
<h3><span style="color: rgb(0,0,255);">● 프로젝트 리소스</span></h3>\
<table><colgroup><col style="width: 15%;" /><col style="width: 75%;" /><col style="width: 10%;" /></colgroup><tbody>\
<tr><th colspan="1" style="text-align: center;">PL</th><th style="text-align: center;">투입인원(' + \
str(table_project.loc[data_index[0]]['member']) + '명)</th><th style="text-align: center;">누적 리소스(hours)</th></tr>\
<tr><td colspan="1" style="text-align: center;">' + table_project.loc[data_index[0]]['projectLead'] + '</td><td><span>' + table_project.loc[data_index[0]]['member_List'] + '</span></td><td style="text-align: center;"><span>' + str(table_project.loc[data_index[0]]['totalTime']) + '</span></td></tr></tbody></table>\
<p class="auto-cursor-target"><br /></p>\
<h3><span style="color: rgb(0,0,255);"><strong>●&nbsp;</strong>프로젝트 주요이슈/특이사항</span></h3>\
<table><colgroup><col /><col /><col /><col /><col /><col /><col />\
</colgroup><tbody><tr><th style="text-align: center;">Milestone</th><th style="text-align: center;">종료일\
</th><th style="text-align: center;" colspan="1">상태</th><th style="text-align: center;">미해결 이슈</th>\
<th style="text-align: center;">전체 이슈</th><th style="text-align: center;" colspan="1">지연 이슈</th>\
<th style="text-align: center;">주간 보고 특이사항</th></tr>' + tableRow2 + '</tbody></table><p><br /></p>'

# Wiki 페이지 생성
confluence.create_page(
        space='RNDPRO006',
        title= table_version.loc[data_index[0]]['projectName'] + ' (' + nowdate + ')',
        body='{0}'.format(wiki_data),
        parent_id=93392437,
        type='page'
    )

page_id = confluence.get_page_by_title('RNDPRO006', table_version.loc[data_index[0]]['projectName'] + ' (' + nowdate + ')', start=None, limit=None)

data = [{"prefix":"global","name":"프로젝트주간보고"}]
headers = {'Content-Type': 'application/json'}
requests.post('https://wiki.telechips.com:8443/rest/api/content/' + page_id['id'] + '/label', data=json.dumps(data), headers=headers, auth=(username, password))
