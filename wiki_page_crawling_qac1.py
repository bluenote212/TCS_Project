from atlassian import Confluence
from bs4 import BeautifulSoup
#import time

#Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = 'rnd_rest_api_account',
    password = 'rnd12345!')


#wiki page source code get
page_info_body1 = confluence.get_page_by_id(169361671, expand='space,body.view,version,container')

#페이지의 항목만 html 형식으로 Parse
temp = page_info_body1['body']['view']['value']
soup = BeautifulSoup(temp, 'html.parser')

#QAC 사용현황 Table 코드만 find
table = soup.find_all('table', limit = 1)

#ip를 저장할 리스트 선언
text=[]

#qac_no 에는 qac 서버 번호를 입력하면 됨 QAC1 = 0, QAC3 = 1
qac_no = 0
if table[qac_no].find_all('td')[0].text == '':
    text.append('')
else:
    if '(' in table[qac_no].find_all('td')[0].text:
        temp = table[qac_no].find_all('td')[0].text.replace(')','').split('(')[1]
        text.append(temp.strip())
    else:
        text.append('')

print(text)

'''
#txt 파일로 저장
fw = open('ip_address.txt', 'w')


fw.write(str(text[0]))
fw.close()
'''
