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
        

body = {
    'botNo': '1809717',
    'accountId': 'bluenote212@telechips.com',
    'content': {
        'type': 'text',
        'text': '안녕하세요 R&D Bot 입니다.'
     }
}
r = requests.post(url, data=json.dumps(body), headers=headers)



