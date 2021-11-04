import json, requests
import sqlite3
import pandas as pd

headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'consumerKey': 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization': 'Bearer AAABAXONcN0Ch9T4YmhyDiRG+1ilvRZoM1MoutdUZLzV6++m3h+/fipKAlD0I1OKCbAJFWhuiQV07ldyuY1M3qu0pVEKqWcrhPdK5k2PKp2Xo42bfFsPleMt8D0+ZHqJVGrXPdw3JheNM5hkVqpzEc0l24vlpymIeLTg74+aEUFa+SpI6mjkbP5vJwD5kR8auewDnQgmuE1cwdBVlveJq2ZDC7ohbAF29Hfd/Wmc75h72LAC3W1Zea+4LF/UpKoBnSxCmqSInyWmyYwAJ5HBrPp/9PdoxB5SqRma2aFswhmwvaR/6AClqjmuAKdGlcgA+DertSmLCCer7i2iNXxNimgqXsrvEAHQQpLwtrv8IGdcV/sf'
}

url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push' #1:1 메시지 Request URL

body = {
    "accountId": "bluenote212@telechips.com",
    "content": {
        "type": "flex",
        "altText": "this is a flexible template",
        "contents": {
            "type": "bubble",
            "size": "giga",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "신호찬 님의 8월 Worklog 안내드립니다.",
                        "wrap": True,
                        "weight": "bold",
                        "color": "#222222",
                        "size": "md",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "text": "총 188h",
                        "weight": "bold",
                        "color": "#222222",
                        "size": "md",
                        "margin": "md",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "text": "업무: 174h, 휴가: 14h",
                        "color": "#222222",
                        "size": "sm",
                        "margin": "md",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "text": "(이번달 최소 근무 시간은 160h, 최대 근무 시간은 210h입니다.)",
                        "color": "#222222",
                        "size": "sm",
                        "wrap": True,
                        "align": "center",
                        "margin": "sm"
                    },
                    {
                        "type": "separator",
                        "margin": "sm"
                    },
                    {
                        "type": "text",
                        "text": "자율 출퇴근하에 근무시간은 분기별로 합산하여 준수 여부를 판단합니다.\n수정이 필요하연 아래 버튼을 눌러 수정하세요",
                        "color": "#aaaaaa",
                        "size": "sm",
                        "wrap": True,
                        "align": "center",
                        "margin": "sm"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "Worklog 수정",
                            "uri": "https://tcs.telechips.com:8443/secure/WPShowTimesheetAction!customTimesheet.jspa#targetType=USER&targetKey=B180093&groupingType=Issue&periodMode=MONTH&startDate=2021-08-01&endDate=2021-08-31&&&periodLocked=false&calendarType=CUSTOM&saveToUserHistory=false&extraIssueFilter=&viewType=TIMESHEET"
                            },
                        "color": "#2432AB"
                    },
                    {
                        "type": "text",
                        "text": "1~2일 후 8월 Worklog는 수정할 수 없습니다.",
                        "color": "#f26400",
                        "size": "sm",
                        "align": "center",
                        "margin": "sm"
                    }
                ],
            }
        }
    }
}

r = requests.post(url, data=json.dumps(body), headers=headers)

print(r, r.text)
