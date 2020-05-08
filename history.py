

for i in range(0, len(data_resource)):
    data_row = '<tr>'
    for j in range(0,len(data_resource[i])):
        data_row += '<td>' + str(data_resource[i][j]) + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row


wiki = wiki_data_top + wiki_data_middle + wiki_data_bottom
wiki = wiki.replace("&","<p>&amp;</p>") #특수문자 & 치환

#confluence Auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])

confluence.update_page(
        parent_id = 93389637,
        page_id = 120318256,
        title = 'RND_worklog_' + str(month_1),
        body = wiki_data_top + wiki_data_middle + wiki_data_bottom,
        type='page',
        representation='storage'
        )
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')
print(userData[0])
print(userData.items(0))
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')
print(worklog[worklog['worklog_author']=='정희성 (HuiSung Jeong)']['time_spent'].sum())
print(userData.loc['0', 'worklog_author'])
print(userData.loc['1', 'worklog_author'])
print(userData.loc[1, 'worklog_author'])
print(userData.loc[1, 'name'])
print(userData.loc[0, 'name'])
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')
print(len(userData))
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Tue Apr 28 09:21:21 2020)---
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_role)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(len(project_role))
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_role)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data1)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(version_data[0]['name'])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(version_data)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(version_data)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(len(version))
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(version)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/version_dataDB_create_page.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Wed Apr 29 09:32:28 2020)---
runfile('C:/Users/B180093/.spyder-py3/project_key_category_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/project_role_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/profield_dataDB_create_page.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/version_dataDB_create_page.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/user_dataDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')
print(month)
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/send_mail.py', wdir='C:/Users/B180093/.spyder-py3')
print(send_mail.sendmail('tcs@telechips.com', ['mwlee@telechips.com'], msg.as_string()))
runfile('C:/Users/B180093/.spyder-py3/send_mail.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Wed May  6 10:25:41 2020)---
runfile('C:/Users/B180093/.spyder-py3/month_worklog_DBcreate.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')
print(worklog[worklog['worklog_author']== rnd_user.loc[1, 'name']]['time_spent'].sum())
print(worklog[worklog['worklog_author'] == '홍두일 (Dooil Hong)']['time_spent'].sum())
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/month_worklog_DBcreate.py', wdir='C:/Users/B180093/.spyder-py3')
print(team_code[0][0])
print(team_code[0][1])
runfile('C:/Users/B180093/.spyder-py3/month_worklog_DBcreate.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/month_worklog_DBcreate.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/month_worklog_DBcreate.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/month_worklog_DBcreate.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/worklog_minor.py', wdir='C:/Users/B180093/.spyder-py3')
print(url)