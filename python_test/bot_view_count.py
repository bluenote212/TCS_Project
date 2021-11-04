import json, requests
import pymongo
from datetime import datetime

# Mongo DB에서 인증에 필요한 계정 정보를 가져와서 pw_data에 저장
conn = pymongo.MongoClient("219.240.43.93", 27017)
db = conn.tcs


col = db.rest_bot_question
data = list(col.find({"depth": "final"}, {"_id": 0, "result": -1}))


count = 0
for i in range(len(data)):
    count += data[i]['result']


print('depth 총 개수 : {0}'.format(len(data)))
print('depth 총 view count : {0}'.format(count))

conn.close()

