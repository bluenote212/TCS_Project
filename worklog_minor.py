import sqlite3
import pandas as pd
from atlassian import Confluence

#userdata를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()

#confluence Auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

#rnd_user 리스트를 가져옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
rnd_user = pd.read_sql("SELECT * FROM userData", con)

#검색할 월의 DB 이름을 입력
month = 'RND_worklog_20213_draft'

#현재월의 worklog를 가져옴
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
worklog = pd.read_sql('SELECT * FROM ' + month, con)
con.close()

#worklog 입력이 미흡한 인원 파악
data = []
for i in range(0, len(rnd_user)):
    if worklog[worklog['worklog_author']== rnd_user.loc[i, 'name']]['worklog_timespent'].sum() < 158.4:
        data.append([rnd_user.loc[i, 'team'], rnd_user.loc[i, 'name'], round(worklog[worklog['worklog_author']== rnd_user.loc[i, 'name']]['worklog_timespent'].sum(),2)])


#Wiki 페이지에 Data table 생성
wiki_data_top = '<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="table-excerpt" ac:schema-version="1" ac:macro-id="70b8954e-f54e-46e7-8b34-a176d7c406ee">\
<ac:parameter ac:name="name">worklog_minor</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><table><colgroup><col /><col /><col />\
</colgroup><tbody><tr><th>Team</th><th>name</th><th>worklog</th></tr>'
wiki_data_middle = ''
wiki_data_bottom = '</tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p><br /></p>'

#data 돌면서 table 생성
for i in range(0, len(data)):
    data_row = '<tr>'
    for j in range(0, len(data[i])):
        data_row += '<td>' + str(data[i][j]) + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row

wiki = wiki_data_top + wiki_data_middle + wiki_data_bottom
wiki = wiki.replace("&","<p>&amp;</p>") #특수문자 & 치환

confluence.update_page(
        parent_id = 42675555,
        page_id = 122586911,
        title = 'worklog 평균 이하 입력',
        body = wiki,
        type='page',
        representation='storage'
    )