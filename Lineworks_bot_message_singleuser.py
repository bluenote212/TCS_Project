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

url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push' #1:1 메시지 Request URL
text = '안녕하세요 R&D Bot 입니다.\n연구소에서 공유가 필요한 여러 가지 정보들을 사내 메신저로 안내드리기 위해 만들어진 Bot입니다.'+ \
'\n오늘부터는 연구원분들이 입력한 Worklog를 안내 드릴 예정이며 앞으로 더 많은 정보를 공유드리도록 하겠습니다.(혹시 잘못된 정보나 오류가 있다면 RIT 신호찬M 에게 문의 부탁드립니다)'

for i in range(0, len(user_data)):
    body = {
        'botNo': '1809717',
        'accountId': user_data[i][3],
        'content': {
            'type': 'text',
            'text': text
         }
    }
    r = requests.post(url, data=json.dumps(body), headers=headers)
    print(r)
    print(user_data[i][3])
