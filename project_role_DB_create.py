import requests
import sqlite3
import simplejson as json
import pandas as pd

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#project category table에서 category 선별해서 프로젝트 key를 가져 옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
project = pd.read_sql("SELECT * FROM project_key WHERE category = '1.SOC 개발' or category = '2.SOC 검증' or category = '3.SDK 개발' or category = '4.요소/기반 기술' or category = '5.사업자/선행/국책' or category = '6.HW개발' ", con)
project_key = project.values.tolist()
con.close()

#프로젝트 role data 생성
data_role = []
for i in range(0, len(project_key)):
    url = requests.get('https://tcs.telechips.com:8443/rest/api/2/project/' + project_key[i][0] + '/role/10400' , id_pw) #sub_pl 추가
    sub_pl = json.loads(url.text)
    if len(sub_pl['actors']) == 0:
        sub_temp = ''
    else:
        sub_temp = ''
        for j in range(0, len(sub_pl['actors'])):
            if j == len(sub_pl['actors']) -1:
                sub_temp += sub_pl['actors'][j]['displayName'].replace('(', ' ').split()[0]
            else:
                sub_temp += sub_pl['actors'][j]['displayName'].replace('(', ' ').split()[0] + ', '

    url = requests.get('https://tcs.telechips.com:8443/rest/api/2/project/' + project_key[i][0] + '/role/10500' , id_pw) #rit 추가
    rit = json.loads(url.text)
    if len(rit['actors']) == 0:
        rit_temp = ''
    else:
        rit_temp = ''
        for j in range(0, len(rit['actors'])):
            if j == len(rit['actors']) -1:
                rit_temp += rit['actors'][j]['displayName'].replace('(', ' ').split()[0]
            else:
                rit_temp += rit['actors'][j]['displayName'].replace('(', ' ').split()[0] + ', '    

    data_role.append([project_key[i][0], sub_temp, rit_temp])#추가한 role을 data_role에 추가

data = pd.DataFrame(data_role, columns = ['project_key', 'Sub_PL', 'RIT']) #DataFrame 생성

#project_role DB 생
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('project_role', con, if_exists='replace', index = False)
con.close()
