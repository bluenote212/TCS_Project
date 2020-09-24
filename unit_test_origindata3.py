from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
#import smtplib
#from email.mime.text import MIMEText

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
cql = 'label="단위테스트결과서2"'
page_list = []
page_list1 = confluence.cql(cql, start=0, limit=1000, expand=None, include_archived_spaces=None, excerpt=None)
page_list = page_list1['results']

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
        table = soup.find_all('table',limit=3) #페이지 내에서 두번째 테이블의 데이터를 저장
        table_text = {}
        for j in range(0,len(table)):
            table_th = table[j].find_all('th')
            table_td = table[j].find_all('td')
            for k in range(0, len(table_th)):
                if table_td[k].text == 'YYYY-MM-DD':
                    table_text.setdefault(table_th[k].text.strip(), '')
                elif table_td[k].text == '@ 사용하지 말고 이름만 입력(ex : 홍길동)':
                    table_text.setdefault(table_th[k].text.strip(), 'none')
                elif table_td[k].text == '참고자료명과 참고자료의 버전을 기입':
                    table_text.setdefault(table_th[k].text.strip(), 'none')
                elif table_td[k].text == '':
                    table_text.setdefault(table_th[k].text.strip(), '')
                else:
                    table_text.setdefault(table_th[k].text.strip(), table_td[k].text.strip()) #테이블의 입력된 텍스트를 앞, 뒤 공백을 제거하고 저장
        table_text.setdefault('url', 'https://wiki.telechips.com:8443/pages/viewpage.action?pageId=' + pageid[i])
        test_result.append(table_text) #페이지별로 추출한 데이터를 저장
    else:
        continue

#Table th, td에서 원하는 key와 item을 조회하여 저
test_result_final = []
for i in range(0, len(test_result)):
    row_text = []
    if 'test date' in test_result[i].keys():
        row_text.append(test_result[i]['test date'])
    else:
        row_text.append('')
    if 'author' in test_result[i].keys():
        row_text.append(test_result[i]['author'])
    else:
        row_text.append('')
    if 'reference & revision' in test_result[i].keys():
        row_text.append(test_result[i]['reference & revision'])
    else:
        row_text.append('')
    if 'SDK Name(Device)' in test_result[i].keys():
        row_text.append(test_result[i]['SDK Name(Device)'])
    else:
        row_text.append('')
    if 'SDK Name(Platform)' in test_result[i].keys():
        row_text.append(test_result[i]['SDK Name(Platform)'])
    else:
        row_text.append('')
    if 'SDK Name(Application)' in test_result[i].keys():
        row_text.append(test_result[i]['SDK Name(Application)'])
    else:
        row_text.append('')
    if 'Subtitle' in test_result[i].keys():
        row_text.append(test_result[i]['Subtitle'])
    else:
        row_text.append('')
    if 'Version' in test_result[i].keys():
        row_text.append(test_result[i]['Version'])
    else:
        row_text.append('')
    if 'Test Type' in test_result[i].keys():
        row_text.append(test_result[i]['Test Type'])
    else:
        row_text.append('')
    if 'Module Name' in test_result[i].keys():
        row_text.append(test_result[i]['Module Name'])
    else:
        row_text.append('')
    if 'Module Subtitle' in test_result[i].keys():
        row_text.append(test_result[i]['Module Subtitle'])
    else:
        row_text.append('')
    if 'Module Version' in test_result[i].keys():
        row_text.append(test_result[i]['Module Version'])
    else:
        row_text.append('')
    if 'Pass' in test_result[i].keys():
        row_text.append(test_result[i]['Pass'])
    else:
        row_text.append('')
    if 'Fail' in test_result[i].keys():
        row_text.append(test_result[i]['Fail'])
    else:
        row_text.append('')
    if 'N/A' in test_result[i].keys():
        row_text.append(test_result[i]['N/A'])
    else:
        row_text.append('')
    if 'N/T' in test_result[i].keys():
        row_text.append(test_result[i]['N/T'])
    else:
        row_text.append('')
    if 'Total' in test_result[i].keys():
        row_text.append(test_result[i]['Total'])
    else:
        row_text.append('')
    if 'Requirement Cnt' in test_result[i].keys():
        row_text.append(test_result[i]['Requirement Cnt'])
    else:
        row_text.append('')
    if 'Requirement Coverage(%)' in test_result[i].keys():
        row_text.append(test_result[i]['Requirement Coverage(%)'])
    else:
        row_text.append('')
    if 'Codesonar 결함수' in test_result[i].keys():
        row_text.append(test_result[i]['Codesonar 결함수'])
    else:
        row_text.append('')
    if '수정불가 Codesonar 결함수' in test_result[i].keys():
        row_text.append(test_result[i]['수정불가 Codesonar 결함수'])
    else:
        row_text.append('')
    if 'QAC 결함수' in test_result[i].keys():
        row_text.append(test_result[i]['QAC 결함수'])
    else:
        row_text.append('')
    if '수정불가 QAC 결함수' in test_result[i].keys():
        row_text.append(test_result[i]['수정불가 QAC 결함수'])
    else:
        row_text.append('')
    if '전체코드라인수' in test_result[i].keys():
        row_text.append(test_result[i]['전체코드라인수'])
    else:
        row_text.append('')
    if 'url' in test_result[i].keys():
        row_text.append(test_result[i]['url'])
    else:
        row_text.append('')
    test_result_final.append(row_text)

data = pd.DataFrame(test_result_final, columns = ['test_date','author','reference&revision', 'SDK_Name_Device', 'SDK_Name_Platform', 'SDK_Name_Application', 'Subtitle',\
                                            'Version', 'Test_Type', 'Module_Name', 'Module_subtitle', 'Module_Version', 'Pass', 'Fail', 'N/A', 'N/T', 'Total', 'Requirement_Cnt',\
                                            'Requirement_Coverage', 'Codesonar_결함수', '수정불가_Codesonar_결함수', 'QAC_결함수', '수정불가_QAC_결함수', '전체코드라인수', 'URL'])

data_drop = data.drop(['author','reference&revision', 'Test_Type', 'Requirement_Cnt', 'Requirement_Coverage'], axis=1) #'author','reference&revision' 열 제거

data_reindex = data_drop.reindex(['test_date', 'SDK_Name_Device', 'SDK_Name_Platform', 'SDK_Name_Application', 'Subtitle', 'Version', 'Module_Name',\
                                  'Module_subtitle', 'Module_Version', 'Pass', 'Fail', 'N/A', 'N/T', 'Total', 'Codesonar_결함수',\
                                  '수정불가_Codesonar_결함수', 'QAC_결함수', '수정불가_QAC_결함수', '전체코드라인수', 'URL'], axis=1)

data = data_reindex.sort_values('test_date')
data_dup = data.drop_duplicates(['SDK_Name_Device', 'SDK_Name_Platform', 'SDK_Name_Application', 'Subtitle', 'Version', 'Module_Name', 'Module_subtitle'], keep='last')

#DB에 data를 저장
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data_dup.to_sql('Unit_test4', con, if_exists='replace', index = False)
con.close()

#DB에서 값을 불러옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
test_result = pd.read_sql("SELECT * FROM Unit_test4", con)
con.close()

#DataFrame을 리스트로 변환
test_result_list = test_result.values.tolist()

#SDK_Name_Device,SDK_Name_Platform,SDK_Name_Application을 합쳐서 SDK Name으로 생성
for i in range(0, len(test_result_list)):
    sdk_name = test_result_list[i][1] + '_' + test_result_list[i][2] + '_' + test_result_list[i][3]
    if sdk_name.endswith('_'):
        sdk_name = sdk_name[:-1]
    test_result_list[i][1] = sdk_name
    del test_result_list[i][2:4]

#Wiki 페이지에 Data 생성
wiki_data_top = '<ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="161913ea-7275-49ec-89af-a4e8e775825c">\
<ac:parameter ac:name="name">Unit_test_backdata2</ac:parameter><ac:rich-text-body>\
<p><br /></p><table><colgroup><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /></colgroup>\
<tbody><tr><th>test_date</th><th>SDK_Name</th><th>Subtitle</th><th>Version</th>\
<th>Module_Name</th><th>Module_subtitle</th><th>Module_Version</th><th>Pass</th><th>Fail</th><th>N/A</th><th>N/T</th><th>Total</th>\
<th>Codesonar결함수</th><th>수정불가 Codesonar결함수</th><th>QAC결함수</th><th>수정불가 QAC결함수</th><th>전체코드라인수</th></tr>'

wiki_data_middle = ''

wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>'


#test date 열에 Wiki url 링크를 걸기 위한 조건
for i in range(0, len(test_result_list)):
    data_row = '<tr>'
    for j in range(0, len(test_result_list[i])-1):
        if j==0 and test_result_list[i][j] != '':
            data_row += '<td><a href="' + test_result_list[i][17] + '">' + test_result_list[i][j] + '</a></td>'
        elif j==0 and test_result_list[i][j] == '':
            data_row += '<td><a href="' + test_result_list[i][17] + '">' + test_result_list[i][17].split('=')[1] + '</a></td>'
        else:
            data_row += '<td>' + test_result_list[i][j] + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row

#Unit_test_backdata2 페이지 업데이트
confluence.update_page(
        parent_id = 95455710,
        page_id = 99890426,
        title = 'Unit_test_backdata2',
        body = wiki_data_top + wiki_data_middle + wiki_data_bottom,
        type='page',
        representation='storage'
    )


