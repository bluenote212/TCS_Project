import json, requests
url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push'
headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'consumerKey': 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization': 'Bearer AAABAXONcN0Ch9T4YmhyDiRG+1ilvRZoM1MoutdUZLzV6++m3h+/fipKAlD0I1OKCbAJFWhuiQV07ldyuY1M3qu0pVEKqWcrhPdK5k2PKp2Xo42bfFsPleMt8D0+ZHqJVGrXPdw3JheNM5hkVqpzEc0l24vlpymIeLTg74+aEUFa+SpI6mjkbP5vJwD5kR8auewDnQgmuE1cwdBVlveJq2ZDC7ohbAF29Hfd/Wmc75h72LAC3W1Zea+4LF/UpKoBnSxCmqSInyWmyYwAJ5HBrPp/9PdoxB5SqRma2aFswhmwvaR/6AClqjmuAKdGlcgA+DertSmLCCer7i2iNXxNimgqXsrvEAHQQpLwtrv8IGdcV/sf'
}
payload = {
    'botNo': '1809717',
    'accountId': 'jy.lee@telechips.com',
    'content': {
        'type': 'text',
        'text': '라인 봇 테스트'
     }
}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r)
print(r.text)