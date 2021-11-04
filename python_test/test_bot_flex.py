import requests
import sqlite3
import simplejson as json
from datetime import datetime, timedelta
import pandas as pd

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push'
headers = {
    'Content-Type' : 'application/json; charset=UTF-8',
    'consumerKey' : 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization': 'Bearer AAABAXONcN0Ch9T4YmhyDiRG+1ilvRZoM1MoutdUZLzV6++m3h+/fipKAlD0I1OKCbAJFWhuiQV07ldyuY1M3qu0pVEKqWcrhPdK5k2PKp2Xo42bfFsPleMt8D0+ZHqJVGrXPdw3JheNM5hkVqpzEc0l24vlpymIeLTg74+aEUFa+SpI6mjkbP5vJwD5kR8auewDnQgmuE1cwdBVlveJq2ZDC7ohbAF29Hfd/Wmc75h72LAC3W1Zea+4LF/UpKoBnSxCmqSInyWmyYwAJ5HBrPp/9PdoxB5SqRma2aFswhmwvaR/6AClqjmuAKdGlcgA+DertSmLCCer7i2iNXxNimgqXsrvEAHQQpLwtrv8IGdcV/sf'
}


payload = {
        "botNo": "1809717",
        "accountId": "bluenote212@telechips.com",
        "content": {
                "type": "flex",
                "altText": "this is a flexible template",
                "contents": {
                              "type": "carousel",
                              "contents": [
                                {
                                  "type": "bubble",
                                  "body": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "The Message Bot API enables the client to interact with individual users, by using a message bot account.",
                                        "wrap": True
                                      }
                                    ]
                                  },
                                  "footer": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                      {
                                        "type": "button",
                                        "style": "primary",
                                        "action": {
                                          "type": "uri",
                                          "label": "See more",
                                          "uri": "http://worksmobile.com"
                                        },
                                        "height": "sm"
                                      }
                                    ]
                                  }
                                },
                                {
                                  "type": "bubble",
                                  "body": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "Hello, World!",
                                        "wrap": True
                                      }
                                    ]
                                  },
                                  "footer": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                      {
                                        "type": "button",
                                        "style": "primary",
                                        "action": {
                                          "type": "uri",
                                          "label": "See more",
                                          "uri": "http://worksmobile.com"
                                        },
                                        "height": "sm"
                                      }
                                    ]
                                  }
                                }
                              ]
                            }
            }
        }
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r, r.text)


