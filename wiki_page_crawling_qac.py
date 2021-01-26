from atlassian import Confluence
from bs4 import BeautifulSoup
from datetime import datetime

#Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = 'rnd_rest_api_account',
    password = 'rnd12345!')

#현재 날짜 저장
day = datetime.now()
today = day.day

#wiki page source code get
page_info_body1 = confluence.get_page_by_id(169361671, expand='space,body.view,version,container')


#페이지의 항목만 html 형식으로 Parse
temp = page_info_body1['body']['view']['value']
soup = BeautifulSoup(temp, 'html.parser')

#QAC 사용현황 Table 코드만 find
table = soup.find_all('table')

#ip를 저장할 리스트 선언
text=[]

#for문으로 현재 날짜 행의 td 태그의 text만 저장, qac_no 에는 qac 서버 번호를 입력하면 됨 QAC2=2, QAC4=3, QAC5=4
qac_no = 4
for j in range(0, len(table[qac_no].find_all('td'))):
    if table[qac_no].find_all('td')[j].text == str(today):
        if table[qac_no].find_all('td')[j+1].text == '':
            text.append('')
        else:
            if '(' in table[qac_no].find_all('td')[j+1].text:
                temp = table[qac_no].find_all('td')[j+1].text.replace(')','').split('(')[1]
                text.append(temp.strip())
            else:
                text.append('')


fw = open('ip_address.txt', 'w')

#배열에는 qac 서버 번호를 입력하면 됨 0=qac1, 1=qac2, 2=qac3, 3=qac4, 4=qac5
fw.write(str(text[0]))
fw.close()
