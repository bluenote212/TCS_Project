from atlassian import Confluence
from bs4 import BeautifulSoup
import pymongo
import requests, json

try:
    conn = pymongo.MongoClient("192.168.3.237", 27017)
    db = conn.tcs
    col = db.id_pw
    pw_data = col.find({})
    id_pw = {'os_username': pw_data[1]['id'], 'os_password': pw_data[1]['pw']}
    
    
    confluence = Confluence(
        url='https://wiki.telechips.com:8443',
        username = id_pw['os_username'],
        password = id_pw['os_password'])
    
    #레이블로 Wiki 페이지를 검색
    cql = 'label="oss_result"'
    page_list = []
    page_list1 = confluence.cql(cql, start=0, limit=1000, expand=None, include_archived_spaces=None, excerpt=None)
    page_list = page_list1['results']
    
    #검색한 Wiki 페이지의 ID들을 저장할 변수
    pageid = []
    
    
    for i in range(0, len(page_list)):
        pageid.append(page_list[i]['content']['id'])
    
    
    #전체 테스트 결과를 저장할 변수
    test_result = []
    
    for i in range(0, len(pageid)):
        page_info_body1 = confluence.get_page_by_id(pageid[i], expand='body.storage')
        soup = BeautifulSoup(page_info_body1['body']['storage']['value'],'html.parser')
        if soup.find('table'):
            table = soup.find_all('table') #페이지 내에서 두번째 테이블의 데이터를 저장
            for j in range(0,len(table)):
                temp = []
                table_th = table[j].find_all('th')
                table_td = table[j].find_all('td')
                if len(table_th) != 0 and table_th[0].text == 'SDK Name(Device)':
                    for k in range(0, len(table_th)):
                        if table_th[k].text == 'SDK Name(Device)':
                            temp.append(table_td[k].text)
                        if table_th[k].text == 'SDK Name(Platform)':
                            temp.append(table_td[k].text)
                        if table_th[k].text == 'SDK Name(Application)':
                            temp.append(table_td[k].text)
                        if table_th[k].text == 'Subtitle':
                            temp.append(table_td[k].text)
                        if table_th[k].text == 'SDK Version':
                            temp.append(table_td[k].text)
                        if table_th[k].text == 'Module Name':
                            temp.append(table_td[k].text)
                        if table_th[k].text == 'Module Subtitle':
                            temp.append(table_td[k].text)
                        if table_th[k].text == 'Module Version':
                            temp.append(table_td[k].text)
                        if table_th[k].text == '준법성 이슈':
                            temp.append(table_td[k].text)
                        if table_th[k].text == '고지문 이슈':
                            temp.append(table_td[k].text)
                        if table_th[k].text == 'TCS Link':
                            temp.append(str(table_td[k]))
                if len(temp) == 11:
                    temp.append(pageid[i])
                    test_result.append(temp)
                        
                else:
                    continue
    
    wiki_data_top = '<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" \
    ac:macro-id="eb7548cc-58be-4d80-800e-a0f02db5eefe"><ac:parameter ac:name="name">oss_test_backdata</ac:parameter><ac:rich-text-body>\
    <p class="auto-cursor-target"><br /></p><table class="fixed-table wrapped"><colgroup><col style="width: 117.0px;" /><col style="width: 130.0px;" /><col style="width: 149.0px;" />\
    <col style="width: 116.0px;" /><col style="width: 138.0px;" /><col style="width: 148.0px;" /><col style="width: 150.0px;" /><col style="width: 160.0px;" />\
    <col style="width: 140.0px;" /><col style="width: 140.0px;" /><col style="width: 230.0px;" /><col style="width: 120.0px;" /></colgroup>\
    <tbody><tr><th>SDK Name(Device)</th><th>SDK Name(Platform)</th><th>SDK Name(Application)</th><th>Subtitle</th><th>SDK Version</th><th>Module Name</th>\
    <th>Module Subtitle</th><th>Module Version</th><th>준법성 이슈</th><th>고지문 이슈</th><th>TCS_link</th><th>Link</th></tr>'
    wiki_data_middle = ''
    wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p><br /></p>'
    
    
    for i in range(0, len(test_result)):
        data_row = '<tr>'
        for j in range(0, len(test_result[i])):
            if j == 10:
                data_row += test_result[i][j]
            if j == 11:
                data_row += '<td><a href="https://wiki.telechips.com:8443/pages/viewpage.action?pageId=' + test_result[i][j] + '">' + test_result[i][j] + '</a></td>'
            if j != 10 and j != 11:
                data_row += '<td>' + test_result[i][j] + '</td>'
        data_row += '</tr>'
        wiki_data_middle += data_row
            
    #Unit_test_backdata2 페이지 업데이트
    r = confluence.update_page(
            parent_id = 95455710,
            page_id = 190659495,
            title = 'oss_test_backdata',
            body = wiki_data_top + wiki_data_middle + wiki_data_bottom,
            type='page',
            representation='storage'
        )
    
    conn.close()

except:
    conn = pymongo.MongoClient("192.168.3.237", 27017)
    db = conn.tcs
    col = db.bot_oauth
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'consumerKey': col.find({})[0]['consumerKey'],
    'Authorization': col.find({})[0]['Authorization']
    }
    conn.close()
    
    url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push' #1:1 메시지 Request URL
    body = {
        'botNo': '1809717',
        'accountId': 'bluenote212@telechips.com',
        'content': {
            'type': 'text',
            'text': 'Wikicreate_oss_test_result2.py 실행 실패했습니다.'
         }
    }
    r = requests.post(url, data=json.dumps(body), headers=headers)
