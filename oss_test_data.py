from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import smtplib
from email.mime.text import MIMEText

#Wiki auth
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

#레이블로 Wiki 페이지를 검색
cql = 'label="oss_result"'
page_list = confluence.cql(cql, start=0, limit=1000, expand=None, include_archived_spaces=None, excerpt=None)
page_list = page_list['results']

#전체 테스트 결과를 저장할 변수
test_result = []

#검색한 Wiki 페이지의 ID들을 저장할 변수
pageid = []
for i in range(0, len(page_list)):
    pageid.append(page_list[i]['content']['id'])

#검색한 ID로 각 페이지에 접근하여 최초 2개의 table에서 원하는 텍스트만 저장
table_error = [] #에러페이지를 저장하기 위한 리스트

for i in range(0, len(pageid)):
    page_info_body1 = confluence.get_page_by_id(pageid[i], expand='body.storage')
    soup = BeautifulSoup(page_info_body1['body']['storage']['value'],'html.parser')
    if soup.find('table'):
        table = soup.find_all('table', limit=2) #페이지 내에서 두번째 테이블의 데이터를 저장
        table_text = []
        for j in range(0,len(table)):
            table_td = table[j].find_all('td', limit=8)
            for k in range(0, len(table_td)):
                table_text.append(table_td[k].text.strip())
        table_text.append('https://wiki.telechips.com:8443/pages/viewpage.action?pageId=' + pageid[i])
        if len(table_text) == 11:
            test_result.append(table_text) #페이지별로 추출한 데이터를 저장
        else:
            table_error.append(table_text)
    else:
        continue

data = pd.DataFrame(test_result, columns = ['SDK_Name(Device)','SDK_Name(Platform)','SDK_Name(Application)', 'Subtitle', 'Version', 'Module_Name', 'Module_Subtitle',\
                                            'Module_Version', '준법성이슈_Count', '고지문이슈_Count', 'link'])

#DB에 data를 저장
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('oss_test_result', con, if_exists='replace', index = False)
con.close()

#DB에서 값을 불러옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
test_result = pd.read_sql("SELECT * FROM oss_test_result", con)
con.close()

#DataFrame을 리스트로 변환
test_result_list = test_result.values.tolist()
for i in range(0, len(test_result_list)):
    sdk_name = test_result_list[i][0] + '_' + test_result_list[i][1] + '_' + test_result_list[i][2]
    if sdk_name.endswith('_'):
        sdk_name = sdk_name[:-1]
    test_result_list[i][0] = sdk_name
    del test_result_list[i][1:3]

#Wiki 페이지에 Data 생성
wiki_data_top = '<ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="161913ea-7285-49ec-89af-a4e8e775825c">\
<ac:parameter ac:name="name">oss_test_data</ac:parameter><ac:rich-text-body>\
<p></p><table><colgroup><col /><col /><col /><col /><col /><col /><col /><col /><col /></colgroup>\
<tbody><tr><th>SDK_Name</th><th>Subtitle</th><th>Version</th><th>Module_Name</th><th>Module_Subtitle</th><th>Module_Version</th><th>준법성이슈_Count</th>\
<th>고지문이슈_Count</th><th>link</th></tr>'

wiki_data_middle = ''

wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>'

for i in range(0, len(test_result_list)):
    data_row = '<tr>'
    for j in range(0, len(test_result_list[i])):
        if j==8:
            data_row += '<td><a href="' + test_result_list[i][8] + '">' + test_result_list[i][j] + '</a></td>'
        else:
            data_row += '<td>' + test_result_list[i][j] + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row

#oss_test_data 페이지 업데이트
confluence.update_page(
        parent_id = 95455710,
        page_id = 137824554,
        title = 'oss_test_data',
        body = wiki_data_top + wiki_data_middle + wiki_data_bottom,
        type='page',
        representation='storage'
    )

body = ''
if len(table_error) != 0:
    for i in range(0, len(table_error)):
        body += str(table_error[i]) + '\n' + '두번째 라인 테스트'
    
     # 세션 생성
    send_mail = smtplib.SMTP('smtp.gmail.com', 587)
    # TLS 보안 시작
    send_mail.starttls()
    # 로그인 인증
    send_mail.login('telechips.rnd.noti@gmail.com', 'wmzqupmvwtpfqhur')
    # 보낼 메시지 설정
    msg = MIMEText(body)
    msg['Subject'] = 'oss_test_data 페이지에서 table 개수가 틀린 페이지 입니다.'     
    # 메일 보내기
    send_mail.sendmail('telechips.rnd.noti@gmail.com', ['hyoyong.jung@telechips.com', 'bluenote212@telechips.com'], msg.as_string())    
    # 세션 종료
    send_mail.quit()