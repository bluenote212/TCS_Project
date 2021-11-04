import requests
import json
import pymongo
from io import BytesIO
from PIL import Image

conn = pymongo.MongoClient("192.168.3.237", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}


headers = {'Content-Type': 'application/json'}

r1 = requests.get('https://timsb.telechips.com:8443/secure/attachment/44800/%EC%9D%B4%EB%AF%B8%EC%A7%80+1.png', auth=(id_pw['os_username'], id_pw['os_password']))

'''
#파일 저장 없이 바로 사용
img = Image.open(BytesIO(r1.content))
img.show()
'''
'''
#파일 저장
with open('C:/Users/B180093/.spyder-py3/tims_issuecreate/%EC%9D%B4%EB%AF%B8%EC%A7%80+1.png', 'wb') as f:
    f.write(r1.content)
'''

conn.close()