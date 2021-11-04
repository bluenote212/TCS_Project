import requests
import json
import pymongo
from bs4 import BeautifulSoup
from urllib import parse


conn = pymongo.MongoClient("192.168.3.237", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}


headers = {'X-Atlassian-Token': 'no-check'}
name = '이미지 1.png'

f = open('C:/Users/B180093/.spyder-py3/tims_issuecreate/이미지.png', 'rb')
files = [('file', (parse.quote(name), f, "image/png"))]


url = "https://tcs.telechips.com:8443/rest/api/2/issue/TMTPD-3762/attachments"
r = requests.post(url, headers=headers ,auth=(id_pw['os_username'], id_pw['os_password']), files=files)


f.close()
conn.close()
print(r)


