from atlassian import Confluence
import pandas as pd
import pymongo

#id_pw를 가져와서 리스트로 변환
conn = pymongo.MongoClient("192.168.3.237", 27017)
db = conn.tcs
col = db.id_pw
pw_data = col.find({})
id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}
 
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = pw_data[1]['id'],
    password = pw_data[1]['pw'])
 
col = db.Unit_test
test_result1 = list(col.find({'Module_Name':{
                        "$nin":['BT', 'DAB', 'HWC', 'Graphic', ]
                    }}
        ))


test_result2 = list(col.find({
            "$and": [
                        {'Module_Name': 'BT'},
                        {'SDK_Name_Platform': 'Linux'},
                    ]
        }))

test_result3 = list(col.find({
            "$and":[
                        {'Module_Name': 'HWC'},
                        {'Module_subtitle': 'v2.x'},
                    ]
        }))

test_result4 = list(col.find({
            "$and":[
                        {'Module_Name': 'DAB'},
                        {'Module_subtitle': 'v2'},
                    ]
        }))

test_result5 = list(col.find({
            "$and":[
                        {'Module_Name': 'Graphic'},
                        {'SDK_Name_Platform': 'Linux'},
                    ]
        }))

data = test_result1 + test_result2 + test_result3 + test_result4 + test_result5

test_result = pd.DataFrame(data, columns = ['test_date', 'SDK_Name_Device', 'SDK_Name_Platform', 'SDK_Name_Application', 'Subtitle',\
                                            'Version', 'Module_Name', 'Module_subtitle', 'Module_Version', 'Pass', 'Fail', 'N/A', 'N/T', 'Total', 'Codesonar_결함수',\
                                            '수정불가_Codesonar_결함수', 'QAC_결함수', '수정불가_QAC_결함수', '전체코드라인수', 'URL'])


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

conn.close()
