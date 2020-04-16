user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
userData = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#Team code
team_code = [
        ['SOC Advanced Team', '4', 'DEPT173'],
        ['SOC IP Design Team', '95', 'DEPT188'],
        ['SOC Design Team', '5', 'TCW01600'],
        ['SOC Verification Team', '6', 'DEPT81'],
        ['SOC Implementation Team', '8', 'TCW01420'],
        ['HW Platform Team', '87', 'TCW03300'],
        ['HW Verification Team', '88', 'DEPT180'],
        ['System BSP Team', '10', 'TCW02900'],
        ['Application BSP Team', '11', 'TCW02203'],
        ['Security solution Team', '9', 'TCW02700'],
        ['Media Android Team', '89', 'DEPT182'],
        ['Media Linux Team', '90', 'TCW01230'],
        ['Media HAL Team', '91', 'DEPT183'],
        ['Automotive MCU Team', '22', 'TCW03100'],
        ['Wireless Team', '3', 'TCW02070'],
        ['Bluetooth Team', '19', 'DEPT75'],
        ['SW Architecture Team', '14', 'DEPT175'],
        ['Project Management Team', '92', 'DEPT184'],
        ['STB Platform Team', '93', 'TCW03110'],
        ['Automotive Platform Team', '15', 'TCW02500'],
        ['Driver Assistance Platform Team', '18', 'TCW02400'],
        ['RND Innovation Team', '2', 'TCW04300'],
        ['Technical Writing Team', '94','DEPT186']
        ]


data = pd.DataFrame(team_code, columns = ['team','team_code', 'group_code'])

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('team_code', con, if_exists='replace', index = False)
con.close()
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_wikicreate2.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Fri Apr 10 13:43:38 2020)---
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_wikicreate2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/user_dataDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_wikicreate2.py', wdir='C:/Users/B180093/.spyder-py3')
print(data_resource)
total_time = worklog[worklog['team'] == team_code[0][0]]['time_spent'].sum()
print(total_time)
total_time = worklog[worklog['team'] == team_code[22][0]]['time_spent'].sum()
print(total_time)
total_time = worklog[worklog['team'] == team_code[22][0]]['time_spent'].sum()
team_time = worklog[(worklog['team'] == team_code[22][0]) & (worklog['project_key'] == team_code[22][2])]['time_spent'].sum()
tims_time = worklog[(worklog['team'] == team_code[22][0]) & (worklog['project_key'] == 'TIMS')]['time_spent'].sum()
print(team_time)
runfile('C:/Users/B180093/.spyder-py3/user_dataDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_wikicreate2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data[3]['id'])
print(data[3]['key'])
print(data[3]['field'])
print(data[3]['fields'])
print(data[3]['fields'][0])
print(data[3]['fields'][0]['field'])
print(data[3]['fields'][0]['field']['id'] = '-2')
if data[3]['fields'][0]['field']['id'] == '-2':
    print(data[3]['fields'][0]['field']['id'])
if data[3]['fields'][0]['field']['id'] == '-2':
    print(data[3]['fields'][0]['field']['name'])
print(data[3]['fields'][0]['field']['name'])
if data[3]['fields'][0]['field']['id'] == -2:
    print(data[3]['fields'][0]['field']['name'])
if data[3]['fields'][0]['field']['id'] != -2:
    print(data[3]['fields'][0]['field']['name'])
print(data[data[3]['fields'][0]['field']['id'] == -2]['name'])
print(data[data[3]['fields'][0]['field']['id'] == -2])
print(data[data[3]['fields'][0]['field']['id'] == -2]['name'])
print(data[data[3]['fields'][0]['field']['id'] == -2]['id'])
print(data[3]['fields'][0]['field']['id'] == -2)
a=[]

if data[3]['fields'][0]['field']['id'] == -2:
    a.append(data[3]['fields'][0]['field']['name'])
    a.append(data[3]['fields'][0]['value']['value'])


print(a)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(a)
print(data[3]['fields'][0]['value']['value'])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data[3]['fields'][8]['value']['value'])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(type(data[3]['fields'][8]['value']['value']))
print(type(data[3]['fields'][7]['value']['value']))
print(data[3]['fields'][7]['value']['value'])
print(data[3]['fields'][8]['value'])
print(type(data[3]['fields'][8]['value']))
print(type(str(data[3]['fields'][8]['value'])))
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Thu Apr 16 13:53:23 2020)---
runfile('C:/Users/B180093/.spyder-py3/unit_test_origindata2.py', wdir='C:/Users/B180093/.spyder-py3')
print(page_list)
print(test_result_list)
print(test_result)
module_result = test_result.drop_duplicates(['Module_Name'], keep='last')
print(module_result)
print(module_result.values.tolist())
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data[3]['fields'][0]['value']['value'])
print(data[3]['fields'][8]['value']['value'])
print(data[3]['fields'][8]['value']['value'].get())
print(data[3]['fields'][7]['value']['value'])
print(data[3]['fields'][8]['value']['value'])
print(data[3]['fields'][8]['value']['value'].items())
print(data[3]['fields'][7]['value']['value'].items())
print(data[3]['fields'][7]['value']['value'].get())
print(type(data[3]['fields'][7]['value']['value']))
print(type(data[3]['fields'][7]['value']))
print(data[3]['fields'][7]['value'].items())
print(data[3]['fields'][8]['value'].items())
print(data[3]['fields'][8]['value'])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_data)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(wiki_data_top + wiki_data_middle + wiki_data_bottom)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_data)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/page_body_storage_info.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(len(project_data[0]))
print(len(project_data))
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(project_data[94])
print(project_data[93])
runfile('C:/Users/B180093/.spyder-py3/page_body_storage_info.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')