from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime

#오늘날짜 계산
date = datetime.now().strftime('%Y-%m-%d')

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
cql = 'label="통합테스트결과서2"'
page_list = []
page_list1 = confluence.cql(cql, start=0, limit=1000, expand=None, include_archived_spaces=None, excerpt=None)
page_list2 = confluence.cql(cql, start=1000, limit=1000, expand=None, include_archived_spaces=None, excerpt=None)
page_list3 = confluence.cql(cql, start=2000, limit=1000, expand=None, include_archived_spaces=None, excerpt=None)
page_list4 = confluence.cql(cql, start=3000, limit=1000, expand=None, include_archived_spaces=None, excerpt=None)
page_list5 = confluence.cql(cql, start=4000, limit=1000, expand=None, include_archived_spaces=None, excerpt=None)
page_list = page_list1['results'] + page_list2['results'] + page_list3['results'] + page_list4['results'] + page_list5['results']

#전체 테스트 결과를 저장할 변수
test_result = []

#검색한 Wiki 페이지의 ID들을 저장할 변수
pageid = []
for i in range(0, len(page_list)):
    pageid.append(page_list[i]['content']['id'])

#검색한 ID로 각 페이지에 접근하여 최초 2개의 table에서 원하는 텍스트만 저장
for i in range(0, len(pageid)):
    page_info_body1 = confluence.get_page_by_id(pageid[i], expand='body.storage')
    soup = BeautifulSoup(page_info_body1['body']['storage']['value'],'html.parser')
    if soup.find('table'):
        table = soup.find_all('table', limit=2) #페이지 내에서 두번째 테이블의 데이터를 저장
        table_text = []
        for j in range(0,len(table)):
            table_td = table[j].find_all('td', limit=13) #테이블행에서 15개의 값 까지만 저장
            for k in range(0, len(table_td)):
                if table_td[k].text == 'YYYY-MM-DD':
                    table_text.append('none')
                elif table_td[k].text == '@ 사용하지 말고 이름만 입력(ex : 홍길동)':
                    table_text.append('none')
                elif table_td[k].text == '참고자료명과 참고자료의 버전을 기입':
                    table_text.append('none')
                #elif table_td[k].text == '':
                    #table_text.append('none') #아무 값이 없는 부분을 none로 저장
                else:
                    table_text.append(table_td[k].text.strip()) #테이블의 입력된 텍스트를 앞, 뒤 공백을 제거하고 저장
        table_text.append('https://wiki.telechips.com:8443/pages/viewpage.action?pageId=' + pageid[i])
        test_result.append(table_text) #페이지별로 추출한 데이터를 저장
    else:
        continue

data = pd.DataFrame(test_result, columns = ['test_date','author','reference&revision', 'SDK_Name_Device', 'SDK_Name_Platform', 'SDK_Name_Application', 'Subtitle',\
                                            'Version', 'Test_Type', 'Pass', 'Fail', 'N/A', 'N/T', 'Total', 'Requirement_Cnt',\
                                            'Requirement_Coverage', 'URL'])

data_drop = data.drop(['author','reference&revision'], axis=1) #'author','reference&revision' 열 제거

data_reindex = data_drop.reindex(['test_date', 'SDK_Name_Device', 'SDK_Name_Platform', 'SDK_Name_Application', 'Subtitle', 'Version', 'Test_Type', 'Pass', 'Fail',\
                                  'N/A', 'N/T', 'Total', 'Requirement_Cnt', 'Requirement_Coverage', 'URL'], axis=1)

data = data_reindex.sort_values('test_date')
data_dup = data.drop_duplicates(['SDK_Name_Device', 'SDK_Name_Platform', 'SDK_Name_Application', 'Subtitle', 'Version'], keep='last')

#DB에 data를 저장
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data_dup.to_sql('SIT_test2', con, if_exists='replace', index = False)
con.close()

#DB에서 값을 불러옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
test_result = pd.read_sql("SELECT * FROM SIT_test2", con)
con.close()

#DataFrame을 리스트로 변환
test_result_list = test_result.values.tolist()

for i in range(0, len(test_result_list)):
    sdk_name = test_result_list[i][1] + '_' + test_result_list[i][2] + '_' + test_result_list[i][3]
    if sdk_name.endswith('_'):
        sdk_name = sdk_name[:-1]
    test_result_list[i][1] = sdk_name
    del test_result_list[i][2:4]

#Wiki 페이지에 Data 생성
wiki_data_top = '<ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="161913ea-7275-49ec-89af-a4e8e775825c">\
<ac:parameter ac:name="name">SIT_test_backdata2</ac:parameter><ac:rich-text-body>\
<p><br /></p><table><colgroup><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /></colgroup>\
<tbody><tr><th>test_date</th><th>SDK_Name</th><th>Subtitle</th><th>Version</th><th>Test_Type</th>\
<th>Pass</th><th>Fail</th><th>N/A</th><th>N/T</th><th>Total</th><th>Req_Cnt</th><th>Req_Coverage(%)</th></tr>'

wiki_data_middle = ''

wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>'

for i in range(0, len(test_result_list)):
    data_row = '<tr>'
    for j in range(0, len(test_result_list[i])-1):
        if j==0:
            data_row += '<td><a href="' + test_result_list[i][12] + '">' + test_result_list[i][j] + '</a></td>'
        else:
            data_row += '<td>' + test_result_list[i][j] + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row

confluence.update_page(
        parent_id = 95455710,
        page_id = 99891658,
        title = 'SIT_test_backdata2',
        body = wiki_data_top + wiki_data_middle + wiki_data_bottom,
        type='page',
        representation='storage'
    )
