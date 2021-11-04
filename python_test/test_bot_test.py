import requests
import simplejson as json
import pymongo
from datetime import datetime

#id_pw를 가져와서 리스트로 변환
conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs
col = db.rest_bot_question

find = col.find({'keyword': {'$regex':'start', '$options': 'i'}}, {"_id": 0,"keyword":1})


'''
message = {}
for i in range(0, len(find)):
    message = find[i]['code']


print(message)
'''



url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/2065000/message/push'
headers = {
    'Content-Type' : 'application/json; charset=UTF-8',
    'consumerKey' : 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization': 'Bearer AAABAXONcN0Ch9T4YmhyDiRG+1ilvRZoM1MoutdUZLzV6++m3h+/fipKAlD0I1OKCbAJFWhuiQV07ldyuY1M3qu0pVEKqWcrhPdK5k2PKp2Xo42bfFsPleMt8D0+ZHqJVGrXPdw3JheNM5hkVqpzEc0l24vlpymIeLTg74+aEUFa+SpI6mjkbP5vJwD5kR8auewDnQgmuE1cwdBVlveJq2ZDC7ohbAF29Hfd/Wmc75h72LAC3W1Zea+4LF/UpKoBnSxCmqSInyWmyYwAJ5HBrPp/9PdoxB5SqRma2aFswhmwvaR/6AClqjmuAKdGlcgA+DertSmLCCer7i2iNXxNimgqXsrvEAHQQpLwtrv8IGdcV/sf'
}


body = [
            {
                        'accountId': 'bluenote212@telechips.com',
                        'content': {
                                    'type': 'button_template',
                                    'contentText': '테스트',
                                    'actions': [
                                                {
                                                    "type" : "message",
                                                    "label" : "정적분석",
                                                    "text" : "정적분석",
                                                    "postback" : "static_analysis"
                                                },
                                                {
                                                    "type" : "message",
                                                    "label" : "정적분석",
                                                    "text" : "정적분석",
                                                    "postback" : "static_analysis"
                                                },
                                                {
                                                    "type" : "message",
                                                    "label" : "정적분석",
                                                    "text" : "정적분석",
                                                    "postback" : "static_analysis"
                                                }
                                            ]
                                    
                                }
                    }
        ]

for i in range(0, len(body)):
    r = requests.post(url, data=json.dumps(body[i]), headers=headers)
    print(r, r.text)



conn.close()
