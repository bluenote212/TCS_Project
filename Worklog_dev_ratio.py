import sqlite3
import pandas as pd

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#team code를 DB에서 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
team_code = pd.read_sql("SELECT * FROM team_code", con)
con.close()
team_code = team_code.values.tolist()

#월별 리소스 DB를 가져와서 데이터 가공 해당 월 입력 data 변수 수정, DB Table 이름 수정 !!!!!------------------------------------------------------------------------------------------!!!!!!!!!!!!!
date = '20210830'
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data_resource = pd.read_sql("SELECT * FROM RND_worklog_20219_draft", con)
con.close()
#----------------------------------------------------------------------------------------------------------------------------

#R&D 프로젝트만 정렬
develop = data_resource[((data_resource['project_category'] == '1.SOC 개발') | (data_resource['project_category'] == '2.SOC 검증') | (data_resource['project_category'] == '3.SDK 개발')\
                        | (data_resource['project_category'] == '4.요소/기반 기술') | (data_resource['project_category'] == '5.사업자/선행/국책') |\
                        (data_resource['project_category'] == '6.HW개발') | (data_resource['project_category'] == 'QA 프로젝트') | (data_resource['project_category'] == '기타 프로젝트_개발'))]

suport = data_resource[data_resource['project_category'] == 'TIMS']

team_dev = data_resource[((data_resource['project_category'] == 'RnD-팀 프로젝트') & (data_resource['issue_type'] == '연구')) | \
                         ((data_resource['project_category'] == 'RnD-팀 프로젝트') & (data_resource['issue_type'] == 'Sub-task') & (data_resource['parent_type'] == '연구'))]

team_etc = data_resource[((data_resource['project_category'] == 'RnD-팀 프로젝트') & (data_resource['issue_type'] == '기타')) | \
                         ((data_resource['project_category'] == 'RnD-팀 프로젝트') & (data_resource['issue_type'] == 'Sub-task') & (data_resource['parent_type'] == '기타')) | \
                         (data_resource['project_category'] == 'RnD-외부 팀 프로젝트') | (data_resource['project_category'] == 'RnD-Group 프로젝트')]


    

for i in range(0, len(team_code)):
    temp_devlop = develop[develop['team'] == team_code[i][0]]
    temp_team_dev = team_dev[team_dev['team'] == team_code[i][0]]
    print(team_code[i][0] + ' : ' + str(round(temp_devlop['worklog_timespent'].sum(), 1)) + '/' + str(round(temp_team_dev['worklog_timespent'].sum(), 1)))

