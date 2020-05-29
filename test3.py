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
data_resource = pd.read_sql("SELECT * FROM RND_worklog_5", con)
con.close()



data_resource.loc[data_resource['issue_chip'] == 'Not related to Chip','issue_chip'] = data_resource['worklog_chip']
data_resource.loc[data_resource['issue_chip'] == 'Common','issue_chip'] = data_resource['worklog_chip']
data_resource.loc[data_resource['issue_chip'] == '','issue_chip'] = data_resource['worklog_chip']
data_resource['auto_ce'] = 'auto'
data_resource['resource_category'] = '개발'
data_resource['group'] = 'SW'
data_resource.loc[data_resource['issue_chip'] == 'TCC898x','auto_ce'] = 'ce'
data_resource.loc[data_resource['issue_chip'] == 'TCC899x','auto_ce'] = 'ce'
data_resource.loc[data_resource['issue_chip'] == 'TCC901x','auto_ce'] = 'ce'
data_resource.loc[data_resource['project_name'] == data_resource['team'],'resource_category'] = '기타'
data_resource.loc[data_resource['project_category'] == 'RnD-Group 프로젝트','resource_category'] = '기타'
data_resource.loc[data_resource['project_name'] == 'TIMS','resource_category'] = '지원'
data_resource.loc[data_resource['team'] == 'SOC Advanced Team','group'] = 'SOCG'
data_resource.loc[data_resource['team'] == 'SOC IP Design Team','group'] = 'SOCG'
data_resource.loc[data_resource['team'] == 'SOC Design Team','group'] = 'SOCG'
data_resource.loc[data_resource['team'] == 'SOC Verification Team','group'] = 'SOCG'
data_resource.loc[data_resource['team'] == 'SOC Implementation Team','group'] = 'SOCG'
data_resource.loc[data_resource['team'] == 'HW Platform Team','group'] = 'HWG'
data_resource.loc[data_resource['team'] == 'HW Verification Team','group'] = 'HWG'
del data_resource['summary']
del data_resource['worklog_comment']

data_resource.to_csv('C:/Users/B180093/Downloads/worklog_workshop_5.csv', index=False, encoding = 'utf-8-sig')
