import json, requests

headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'consumerKey': 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization': 'Bearer AAAA/nbEb0dM/5HS9XoOQR2VRvz+sMDtNRlrthxawuCejBN7uKg3Ylx75GbMnDMR0J+vqc9Yo5ACKzsrFrNA8GjN73ea98LqyMlgMsCxrGavZbnaY3JB5qPOkBatmDjfsxgWMzR8f7/sFUacKjOjhDbOAeeT/qlpsZpkmFKrmR9vo/MD9j+zYmbCuXoel6/zkJ56iJ4BJ5JCRELxdwqQk95iO6a4mJUK52/vVSFurNss53uI2NyoFPoyJXzMXbXcLa1enc8oKntUeP35Cy4+ovZs9d83NyVu+2d0rgfQPxPmxf6yYgjBfOKvjb2s4uJggCOd47wl6M5x9UO7QfPAOj+6G/4='
}

member = ['bluenote212@telechips.com', 'jy.lee@telechips.com']
title = 'Bot 단톡방 테스트'

def roomcreate(member, title):
    url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/room' #Bot이 포함된 room 생성
    body = {
        'accountIds': member,
        'title': title
    }
    result = requests.post(url, data=json.dumps(body), headers=headers)
    return result.text[11:-2]

print(roomcreate(member, title))
