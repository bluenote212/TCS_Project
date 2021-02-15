import json, requests
import sqlite3
import pandas as pd

#user_data를 DB에서 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user_data = pd.read_sql("SELECT * FROM userData", con) # WHERE 조건 확인
con.close()
user_data = user_data.values.tolist()

headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'consumerKey': 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization': 'Bearer AAAA/nbEb0dM/5HS9XoOQR2VRvz+sMDtNRlrthxawuCejBN7uKg3Ylx75GbMnDMR0J+vqc9Yo5ACKzsrFrNA8GjN73ea98LqyMlgMsCxrGavZbnaY3JB5qPOkBatmDjfsxgWMzR8f7/sFUacKjOjhDbOAeeT/qlpsZpkmFKrmR9vo/MD9j+zYmbCuXoel6/zkJ56iJ4BJ5JCRELxdwqQk95iO6a4mJUK52/vVSFurNss53uI2NyoFPoyJXzMXbXcLa1enc8oKntUeP35Cy4+ovZs9d83NyVu+2d0rgfQPxPmxf6yYgjBfOKvjb2s4uJggCOd47wl6M5x9UO7QfPAOj+6G/4='
}

user_list = [['B180031','2021-02-20'],['B100217','2021-02-27'],['B160020','2021-02-22'],['B180308','2021-02-28'],['B180093','2021-02-28']]

for i in range(0, len(user_data)):
    for j in range(0, len(user_list)):
        if user_list[j][0].lower() == user_data[i][1]:
            user_list[j].append(user_data[i][0])
            user_list[j].append(user_data[i][3])

url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push' #1:1 메시지 Request URL        
for i in range(0, len(user_list)):
    body = {
        'botNo': '1809717',
        'accountId': user_list[i][3],
        'content': {
            'type': 'text',
            'text': '안녕하세요 ' + user_list[i][2] + '님\n연구소 개발서버 접속 패스워드가 '+ user_list[i][1] + '에 만료되오니 갱신부탁드립니다.\nSSP 접속 주소 - https://openldap.telechips.com'
         }
    }
    r = requests.post(url, data=json.dumps(body), headers=headers)
    print(r)
    print(user_list[i][3])

