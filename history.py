            data_row += '<td>' + project_data[i][j].replace('(', ' ').split()[0] + '</td>'
        elif j == 4 and project_data[i][j] != '': #종료보고에 link
            data_row += '<td><a href="' + project_data[i][j] + '">종료보고서</a></td>'
        elif j == 7 and project_data[i][j] != '': #kick_off에 link
            data_row += '<td><a href="' + project_data[i][j] + '">Kick-off회의</a></td>'
        elif j == 11 and project_data[i][j] != '': #Wiki에 link
            data_row += '<td><a href="' + project_data[i][j] + '">' + project_data[i][0] + '</a></td>'
        elif (j == 12 or 13) and project_data[i][j] != '':
            temp = ''
            for k in range(0, len(project_data[i][j])):
                temp += project_data[i][j][k].replace('(', ' ').split()[0]
            data_row += '<td>' + temp + '</td>'
        else: #나머지 항목은 값만 입력
            data_row += '<td>' + project_data[i][j] + '</td>'
    data_row += '</tr>'
    wiki_data_middle += data_row


wiki = wiki_data_top + wiki_data_middle + wiki_data_bottom
wiki = wiki.replace("&","<p>&amp;</p>") #특수문자 & 치환

confluence.update_page(
        parent_id = 95455710,
        page_id = 120297594,
        title = 'project_data',
        body = wiki,
        type='page',
        representation='storage'
    )
print(temp)
runfile('C:/Users/B180093/.spyder-py3/profield_projectDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_data[0][12][0])
print(project_data[0][12][0].replace('(', ' ').split()[0])
runfile('C:/Users/B180093/.spyder-py3/profield_projectDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_data[0])
runfile('C:/Users/B180093/.spyder-py3/profield_projectDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_data[0])
print(project_data[0][12])
print(project_data[0][12].replace('(', ' ').split()[0])
print(project_data[0][12][0].replace('(', ' ').split()[0])
print(project_data[0][12][1].replace('(', ' ').split()[0])
print(project_data[0][13][1].replace('(', ' ').split()[0])
runfile('C:/Users/B180093/.spyder-py3/profield_projectDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(data_role)
runfile('C:/Users/B180093/.spyder-py3/profield_projectDB_create.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Tue Apr 21 11:08:31 2020)---
runfile('C:/Users/B180093/.spyder-py3/project_key_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/profield_projectDB_create.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Thu Apr 23 09:15:12 2020)---
runfile('C:/Users/B180093/.spyder-py3/project_key_project_category_profield_data_create_page.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(url)
print(day_before)
print(day_last)
print(today)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(today)
print(day)
print(first_day)
print(day_before)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(first_day_1)
print(last_day)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(last_day)
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_wikicreate2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(url)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(user)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(user_info)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/project_key_project_category_profield_data_create_page.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/project_key_category_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/project_key_project_category_profield_data_create_page.py', wdir='C:/Users/B180093/.spyder-py3')
print(data_role)
runfile('C:/Users/B180093/.spyder-py3/project_role_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(data)
runfile('C:/Users/B180093/.spyder-py3/project_role_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(data_role)
runfile('C:/Users/B180093/.spyder-py3/project_role_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_role)
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/project_role_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(type(data[i]['startDate']))
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(type(data[0]))
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data[0]['userReleaseDate'])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data2)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data1)
print(data1[0])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Fri Apr 24 15:00:32 2020)---
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/project_role_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data['roles'][5]['users']['displayName'])
print(data['roles'][5]['users'][0]['displayName'])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_key)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/project_key_category_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')