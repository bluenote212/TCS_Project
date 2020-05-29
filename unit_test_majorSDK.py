from atlassian import Confluence
import pandas as pd
import sqlite3

#DB에서 Unit_test3 값을 불러옴
con1 = sqlite3.connect('C:/Users/B180093/database/tcs.db')
test_result_unit = pd.read_sql("SELECT * FROM Unit_test3", con1)
con1.close()

#DB에서 SIT_test2 값을 불러옴
con2 = sqlite3.connect('C:/Users/B180093/database/tcs.db')
test_result_sit = pd.read_sql("SELECT * FROM SIT_test2", con2)
con2.close()

#Wiki auth
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

#------------------------------------------------------- 1. TCC803x_AndroidP_IVI_32bit_1.5.0 --------------------------------------
SDK = '1. TCC803x_AndroidP_IVI_32bit_1.5.0'
wiki_page = 108802412
#unit test 결과 조회, 필요없는 Column 제거
unit1_temp = test_result_unit[(test_result_unit.SDK_Name_Device == 'TCC803x') & (test_result_unit.SDK_Name_Platform == 'AndroidP') & (test_result_unit.SDK_Name_Application == 'IVI') & \
                  (test_result_unit.Subtitle == '32bit') & (test_result_unit.Version == '1.5.0')].drop(['Pass', 'N/A', 'N/T', 'Total', 'Codesonar_결함수', \
                  '수정불가_Codesonar_결함수', 'QAC_결함수', '수정불가_QAC_결함수', '전체코드라인수'], axis=1)
unit1 = unit1_temp.reset_index().drop(['index'], axis=1)

#sit test 결과 조회, 필요없는 Column 제거
sit1_temp = test_result_sit[(test_result_sit.SDK_Name_Device == 'TCC803x') & (test_result_sit.SDK_Name_Platform == 'AndroidP') & (test_result_sit.SDK_Name_Application == 'IVI') & \
                  (test_result_sit.Subtitle == '32bit') & (test_result_sit.Version == '1.5.0')].drop(['Test_Type', 'Pass', 'N/A', 'N/T', 'Total', 'Requirement_Cnt',\
                  'Requirement_Coverage'], axis=1)
sit1 = sit1_temp.reset_index().drop(['index'], axis=1)

Module_list = [['AudioHAL', 'MMG'],
               ['BT', 'CTG'],
               ['CameraHAL', 'MMG'],
               ['CarPlay', 'CTG'],
               #['CobaltBrowser', 'PTG'],
               #['DAB', 'CTG'],
               #['DRM30', 'CTG'],
               #['ECAM', 'BSPG'],
               #['ECNR', 'CTG'],
               #['EXTD', 'MMG'],
               ['Graphic', 'MMG'],
               #['HDCP', 'BSPG'],
               #['HDR10', 'CTG'],
               ['HSM', 'BSPG'],
               ['HWC', 'MMG'],
               ['iAP2', 'CTG'],
               #['ISDB-T', 'CTG'],
               ['Kernel', 'BSPG'],
               ['MF', 'MMG'],
               #['MICOM', 'CTG'],
               #['OPTEE', 'BSPG'],
               #['PlayReady', 'BSPG'],
               ['SCLCAM', 'BSPG'],
               ['SecureBoot', 'BSPG'],
               ['SVM', 'BSPG'],
               #['TDD', 'MMG'],
               #['T-Sound', 'BSPG'],
               #['Widevine', 'BSPG'],
               ['WIFI', 'CTG']]

test_result = {}


for i in range(0, len(Module_list)):
    if any(unit1['Module_Name'].isin([Module_list[i][0]])):
        temp = [list(unit1.loc[unit1['Module_Name'] == Module_list[i][0], ['Fail']].values[0]), list(unit1.loc[unit1['Module_Name'] == Module_list[i][0], ['test_date']].values[0]), \
                list(unit1.loc[unit1['Module_Name'] == Module_list[i][0], ['URL']].values[0]), Module_list[i][1]]
        test_result.setdefault(Module_list[i][0], [temp[0][0], temp[1][0], temp[2][0], Module_list[i][1]])
        temp = []
    if any(unit1['Module_Name'].isin([Module_list[i][0]])) == False:
        test_result.setdefault(Module_list[i][0], ['N/T', 'N/T', 'N/T', Module_list[i][1]])

#test_result에 sit 결과 추가
Module_list.append(['SIT', 'PLG'])

if not sit1.values.tolist():
    test_result.setdefault('SIT', ['N/T', '', '', 'PLG'])
else:
    test_result.setdefault('SIT', [sit1['Fail'].values[0], sit1['test_date'].values[0], sit1['URL'].values[0], 'PLG'])


Wiki_body_top = '<ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="table-excerpt" \
ac:schema-version="1" ac:macro-id="0cd61a8e-0ee3-41f5-b485-5e0fc926eece"><ac:parameter ac:name="name">' + SDK + '_unit</ac:parameter>\
<ac:rich-text-body><p class="auto-cursor-target"><br /></p><table><colgroup><col /><col /><col /><col /></colgroup><tbody><tr><th>Module_Name</th><th>Group</th><th>Fail</th><th>test_date</th></tr>'

Wiki_body_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>\
</ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="table-excerpt-include" ac:schema-version="1" ac:macro-id="76e65e76-4bc4-4e0d-8551-f26273acd239">\
<ac:parameter ac:name="name">' + SDK + '</ac:parameter><ac:parameter ac:name="page"><ac:link><ri:page ri:content-title="주요 SDK 모듈 구성 현황" />\
</ac:link></ac:parameter><ac:parameter ac:name="type">page</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout>'

Wiki_body_middle = ''
for i in range(0, len(test_result)):
    if test_result[Module_list[i][0]][0] == 'N/T':
        Wiki_body_middle += '<tr><td>' + Module_list[i][0] + '</td><td>' + Module_list[i][1] + '</td><td>'  + test_result[Module_list[i][0]][0] + '</td><td></td></tr>'
    else:
        Wiki_body_middle += '<tr><td>' + Module_list[i][0] + '</td><td>' + Module_list[i][1] + '</td><td>' + test_result[Module_list[i][0]][0] +\
        '</td><td><a href="' + test_result[Module_list[i][0]][2] + '">' + test_result[Module_list[i][0]][1] + '</a></td></tr>'

Wiki_body_top + Wiki_body_middle + Wiki_body_bottom

confluence.update_page(
        parent_id = 105541245,
        page_id = wiki_page,
        title = SDK,
        body = Wiki_body_top + Wiki_body_middle + Wiki_body_bottom,
        type='page',
        representation='storage'
    )
