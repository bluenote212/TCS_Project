import sqlite3
import pandas as pd

# id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

# team code를 DB에서 가져와서 리스트로 변환---------------------------------------------------------------------------
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data_resource = pd.read_sql("SELECT * FROM RND_worklog_202111_draft", con)
con.close()
# -------------------------------------------------------------------------------------------------------------------

data_resource.loc[data_resource['issue_chip'] == 'Not related to Chip', 'issue_chip'] = data_resource['worklog_chip']
data_resource.loc[data_resource['issue_chip'] == 'Common', 'issue_chip'] = data_resource['worklog_chip']
data_resource.loc[data_resource['issue_chip'] == '', 'issue_chip'] = data_resource['worklog_chip']
data_resource.loc[data_resource['issue_chip'] == '', 'issue_chip'] = '기초연구'
data_resource.loc[data_resource['issue_chip'] == 'Not related to Chip', 'issue_chip'] = '기초연구'
data_resource.loc[data_resource['issue_chip'] == 'Common', 'issue_chip'] = '기초연구'
data_resource.loc[data_resource['issue_chip'] == 'D5', 'issue_chip'] = '기초연구'
data_resource.loc[data_resource['issue_chip'] == 'TCC530x', 'issue_chip'] = '기초연구'
data_resource.loc[data_resource['issue_chip'] == 'TCC806x', 'issue_chip'] = 'TCC805x'
data_resource.loc[data_resource['issue_chip'] == 'TCC901x', 'issue_chip'] = 'TCC899x'
data_resource.loc[data_resource['issue_chip'] == 'TCC803xPE', 'issue_chip'] = 'TCC803x'
data_resource.loc[data_resource['issue_chip'] == 'TCC70xx', 'issue_chip'] = 'TCC701x'
data_resource.loc[data_resource['issue_chip'] == 'AIX', 'issue_chip'] = '기초연구'
data_resource.loc[data_resource['issue_chip'] == 'AXON', 'issue_chip'] = '기초연구'
data_resource.loc[data_resource['issue_chip'] == 'VCP3', 'issue_chip'] = '기초연구'


data_resource = data_resource.drop(data_resource[data_resource['worklog_author'] == '송봉기 (BongGee Song)'].index)
data_resource = data_resource.drop(data_resource[data_resource['worklog_author'] == '김문수 (Moonsoo Kim)'].index)
data_resource = data_resource.drop(data_resource[data_resource['worklog_author'] == '최재순 (JS Choi)'].index)
data_resource = data_resource.drop(data_resource[data_resource['worklog_author'] == '노호식 (Hosi Roh)'].index)
data_resource = data_resource.drop(data_resource[data_resource['worklog_author'] == '이재호 (Justin Lee)'].index)
data_resource = data_resource.drop(data_resource[data_resource['worklog_author'] == '이영종 (Daxter Lee)'].index)
data_resource = data_resource.drop(data_resource[data_resource['worklog_author'] == '장지연 (Patrick Jang)'].index)
data_resource = data_resource.drop(data_resource[data_resource['team'] == 'Technical Writing Team'].index)
data_resource = data_resource.drop(data_resource[data_resource['team'] == 'RND Innovation Team'].index)

data_resource_final = data_resource[~data_resource['worklog_authorkey'].str.contains('f')]

data_resource_final.to_csv('C:/Users/B180093/Downloads/worklog.csv', index=False, encoding='utf-8-sig')
