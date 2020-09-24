import sqlite3
import pandas as pd
from atlassian import Confluence

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

#team code를 DB에서 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
team_code = pd.read_sql("SELECT * FROM team_code", con)
con.close()
team_code = team_code.values.tolist()

#월별 리소스 DB를 가져와서 데이터 가공 해당 월 입력 data 변수 수정, DB Table 이름 수정 !!!!!------------------------------------------------------------------------------------------!!!!!!!!!!!!!
date = '20200830'
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data_resource = pd.read_sql("SELECT * FROM RND_worklog_8_draft", con)
con.close()
#----------------------------------------------------------------------------------------------------------------------------

#R&D 프로젝트만 정렬
develop = data_resource[(data_resource['project_category'] == '1.SOC 개발') | (data_resource['project_category'] == '2.SOC 검증') | (data_resource['project_category'] == '3.SDK 개발')\
                        | (data_resource['project_category'] == '4.요소/기반 기술') | (data_resource['project_category'] == '5.사업자/선행/국책') |\
                        (data_resource['project_category'] == '6.HW개발') | (data_resource['project_category'] == 'QA 프로젝트') | (data_resource['project_category'] == '기타 프로젝트_개발')]

develop_unique = develop['project_name'].drop_duplicates()

#temp에 프로젝트별 리소스 저장
temp = []
for i in range(len(develop_unique)):
    temp.append([date, develop_unique.iloc[i], round(data_resource[data_resource['project_name'] == develop_unique.iloc[i]]['worklog_timespent'].sum(), 2)])

temp.sort(reverse=True, key=lambda x:x[2])#worklog_timespent 내림차순으로 정렬
project_resource = pd.DataFrame(temp[:20], columns=['date', 'project_name', 'worklog_timespent']) #상위 20개 프로젝트만 dataframe로 생성

#project_resource DB 테이블 update
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project_resource.to_sql('project_resource', con, if_exists='append', index = False)
con.close()

#각팀 개발/지원/경상 리소스 구분
team_resource = []
for i in range(0, len(team_code)):
    if team_code[i][2] == 'TMSAT2' or team_code[i][2] == 'TMPMT' or team_code[i][2] == 'TMTPD':#비 개발 팀들 리소스 구분
        #팀 프로젝트의 품질 data 생성
        qul = data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == '품질'))]['worklog_timespent'].sum() + \
        data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == 'Sub-task') & (data_resource['parent_type'] == '품질'))]['worklog_timespent'].sum()
        #팀 프로젝트의 Task data 생성
        task = data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == 'Task'))]['worklog_timespent'].sum() +\
        data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == 'Sub-task') & (data_resource['parent_type'] == 'Task'))]['worklog_timespent'].sum()
        #팀 프로젝트의 회의(개발) data 생성
        meet_dev = data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == '회의') & (data_resource['issue_meeting'] == '개발회의'))]['worklog_timespent'].sum() +\
        data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == 'Sub-task') & (data_resource['parent_type'] == '회의') & (data_resource['issue_meeting'] == '개발회의'))]['worklog_timespent'].sum()
        #R&D 개발 프로젝트 data 생성
        dev = develop[develop['team'] == team_code[i][0]]['worklog_timespent'].sum() + qul + meet_dev + task
        #지원 data 생성
        tims = data_resource[(data_resource['issue_type'] == 'TIMS') & (data_resource['team'] == team_code[i][0])]['worklog_timespent'].sum() + \
        data_resource[(data_resource['parent_type'] == 'TIMS') & (data_resource['team'] == team_code[i][0]) & (data_resource['issue_type'] == 'Sub-task')]['worklog_timespent'].sum()
        #etc data 생성
        etc = data_resource[(data_resource['project_category'] == 'RnD-팀 프로젝트') & (data_resource['team'] == team_code[i][0])]['worklog_timespent'].sum() +\
        data_resource[(data_resource['project_category'] == 'RnD-Group 프로젝트') & (data_resource['team'] == team_code[i][0])]['worklog_timespent'].sum() - qul - meet_dev - task
        
        team_resource.append([date, team_code[i][0] , round(dev, 1), round(tims, 1), round(etc, 1)])
        
    else:#개발 팀들 리소스 구분
        #팀 프로젝트의 품질 data 생성
        qul = data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == '품질'))]['worklog_timespent'].sum() +\
        data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == 'Sub-task') & (data_resource['parent_type'] == '품질'))]['worklog_timespent'].sum()
        #팀 프로젝트의 회의(개발) data 생성
        meet_dev = data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == '회의') & (data_resource['issue_meeting'] == '개발회의'))]['worklog_timespent'].sum() +\
        data_resource[((data_resource['project_key'] == team_code[i][2]) & (data_resource['issue_type'] == 'Sub-task') & (data_resource['parent_type'] == '회의') & (data_resource['issue_meeting'] == '개발회의'))]['worklog_timespent'].sum()
        #R&D 개발 프로젝트 data 생성
        dev = develop[develop['team'] == team_code[i][0]]['worklog_timespent'].sum() + qul + meet_dev
        #지원 data 생성
        tims = data_resource[(data_resource['issue_type'] == 'TIMS') & (data_resource['team'] == team_code[i][0])]['worklog_timespent'].sum() + \
        data_resource[(data_resource['parent_type'] == 'TIMS') & (data_resource['team'] == team_code[i][0]) & (data_resource['issue_type'] == 'Sub-task')]['worklog_timespent'].sum()
        
        etc = data_resource[(data_resource['project_category'] == 'RnD-팀 프로젝트') & (data_resource['team'] == team_code[i][0])]['worklog_timespent'].sum() +\
        data_resource[(data_resource['project_category'] == 'RnD-Group 프로젝트') & (data_resource['team'] == team_code[i][0])]['worklog_timespent'].sum() - qul - meet_dev
        
        team_resource.append([date, team_code[i][0] , round(dev, 1), round(tims, 1), round(etc, 1)])


team_resource = pd.DataFrame(team_resource, columns=['date', 'team', 'devlop', 'custom', 'etc'])

#team_resource DB 테이블 update
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
team_resource.to_sql('team_resource', con, if_exists='append', index = False)
con.close()
