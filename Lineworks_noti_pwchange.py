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
    'Authorization': 'Bearer AAABAXONcN0Ch9T4YmhyDiRG+1ilvRZoM1MoutdUZLzV6++m3h+/fipKAlD0I1OKCbAJFWhuiQV07ldyuY1M3qu0pVEKqWcrhPdK5k2PKp2Xo42bfFsPleMt8D0+ZHqJVGrXPdw3JheNM5hkVqpzEc0l24vlpymIeLTg74+aEUFa+SpI6mjkbP5vJwD5kR8auewDnQgmuE1cwdBVlveJq2ZDC7ohbAF29Hfd/Wmc75h72LAC3W1Zea+4LF/UpKoBnSxCmqSInyWmyYwAJ5HBrPp/9PdoxB5SqRma2aFswhmwvaR/6AClqjmuAKdGlcgA+DertSmLCCer7i2iNXxNimgqXsrvEAHQQpLwtrv8IGdcV/sf'
}

file = open('pw_expiration.txt', 'r')


user_list = [['B190316','2021-03-03'],['B070298','2021-03-03'],['B100217','2021-02-27'],['B160020','2021-02-25'],['B170180','2021-03-08'],['B190342','2021-03-08']]

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