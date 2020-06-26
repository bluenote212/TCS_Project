from atlassian import Confluence
import pandas as pd
import sqlite3

#Wiki auth
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

#DB에서 값을 불러옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
sql = "SELECT * FROM Unit_test3 WHERE Module_Name != 'BT' \
UNION \
SELECT * FROM Unit_test3 WHERE Module_Name == 'BT' AND SDK_Name_Platform == 'Linux' ORDER BY Module_Name"

test_result = pd.read_sql(sql, con)
con.close()

#모듈 결과 중 date가 없는 것과 MF만 별도 분리
module_result = test_result[(test_result['test_date'] != 'none') & (test_result['Module_Name'] != 'MF')].drop_duplicates(['Module_Name'], keep='last')

#MF 모듈 결과에서 subtitle까지 비교해서 중복값제거
mf_result = test_result[test_result['Module_Name'] == 'MF'].drop_duplicates(['Module_subtitle'], keep='last')

#module_result에 mf_result 추가
module_result = module_result.append(mf_result)


#DataFrame을 리스트로 변환
test_result_list = module_result.values.tolist()

for i in range(0, len(test_result_list)):
    sdk_name = test_result_list[i][1] + '_' + test_result_list[i][2] + '_' + test_result_list[i][3]
    if sdk_name.endswith('_'):
        sdk_name = sdk_name[:-1]
    test_result_list[i][1] = sdk_name
    del test_result_list[i][2:4]

#Wiki 페이지에 Data 생성
wiki_data_top = '<ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="161913ea-7275-49ec-89af-a4e8e775825c">\
<ac:parameter ac:name="name">module_name_test_result</ac:parameter><ac:rich-text-body>\
<p><br /></p><table><colgroup><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /><col /></colgroup>\
<tbody><tr><th>test_date</th><th>SDK_Name</th><th>Subtitle</th><th>Version</th>\
<th>Module_Name</th><th>Module_subtitle</th><th>Module_Version</th><th>Pass</th><th>Fail</th><th>N/A</th><th>N/T</th><th>Total</th>\
<th>Codesonar결함수</th><th>수정불가 Codesonar결함수</th><th>QAC결함수</th><th>수정불가 QAC결함수</th><th>전체코드라인수</th></tr>'

wiki_data_middle = ''

wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>'

for i in range(0, len(test_result_list)):
    data_row = '<tr>'
    for j in range(0, len(test_result_list[i])-1):
        if j==0:
            data_row += '<td><a href="' + test_result_list[i][17] + '">' + test_result_list[i][j] + '</a></td>'
        else:
            data_row += '<td>' + test_result_list[i][j] + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row
    
confluence.update_page(
        parent_id = 99890426,
        page_id = 120296661,
        title = 'module_name_test_result',
        body = wiki_data_top + wiki_data_middle + wiki_data_bottom,
        type='page',
        representation='storage'
    )
