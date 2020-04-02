        ['SOC Verification Team', '6', 'TMSVT'],
        ['SOC Implementation Team', '8', 'TMSIT'],
        ['Security Solution Team', '9', 'TMSEC'],
        ['System BSP Team', '10', 'TMBSP'],
        ['Application BSP Team', '11', 'TMABT'],
        ['SW Architecture Team', '14', 'TMSAT2'],
        ['Automotive Platform Team', '15', 'TMAPT'],
        ['Driver Assistance Platform Team', '18', 'TMAPT2'],
        ['Bluetooth Team', '19', 'TMBT'],
        ['Automotive MCU Team', '22', 'TMST'],
        ['HW Platform Team', '87', 'TMHWT'],
        ['HW Verification Team', '88', 'TMHVT'],
        ['Media Android Team', '89', 'TMMT'],
        ['Media Linux Team', '90', 'TMMLT'],
        ['Media HAL Team', '91', 'TMMHT'],
        ['Project Management Team', '92', 'TMPMT'],
        ['STB Platform Team', '93', 'TMCAT'],
        ['Technical Writing Team', '94', 'TMTWT'],
        ['SOC IP Design Team', '95', 'TMIDT']
        ]
data = pd.DataFrame(team_code, columns = ['team', 'team_code', 'project_key'])
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data.to_sql('team_code', index = False)
con.close()
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test1.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Mon Mar 30 09:45:19 2020)---
runfile('C:/Users/B180093/.spyder-py3/project_info.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2_test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_create2_test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2_test.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_create2_test.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Wed Apr  1 09:21:24 2020)---
runfile('C:/Users/B180093/.spyder-py3/project_info.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_create2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
print(data_resource)
print(month)

## ---(Thu Apr  2 11:53:51 2020)---
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_wikicreate2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/allteam_resource_wikicreate2.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Thu Apr  2 14:56:40 2020)---
runfile('C:/Users/B180093/.spyder-py3/user_dataDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(team_code)
runfile('C:/Users/B180093/.spyder-py3/user_dataDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(resource)
runfile('C:/Users/B180093/.spyder-py3/user_dataDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
import requests
import sqlite3
import simplejson as json
import pandas as pd

username = 'b180093'
password = 'infra4938hc!'
userData = {'os_username': username, 'os_password': password}

#Team code
team_code = {
        'SOC_Advanced_Team' : 'DEPT173',
        'SOC_IP_Design_Team' : 'DEPT188',
        'SOC_Design_Team' : 'TCW01600',
        'SOC_Verification_Team' : 'DEPT81',
        'SOC_Implementation_Team' : 'TCW01420',
        'HW Platform Team' : 'TCW03300',
        'HW Verification Team' : 'DEPT180',
        'System_BSP_Team' : 'TCW02900',
        'Application_BSP_Team' : 'TCW02203',
        'Security_solution_Team' : 'TCW02700',
        'Media_Android Team' : 'DEPT182',
        'Media_Linux Team' : 'TCW01230',
        'Media_HAL Team' : 'DEPT183',
        'Automotive_MCU Team' : 'TCW03100',
        'Wireless_Team' : 'TCW02070',
        'Bluetooth_Team' : 'DEPT75',
        'SW_Architecture_Team' : 'DEPT175',
        'Project_Management_Team' : 'DEPT184',
        'STB_Platform_Team' : 'TCW03110',
        'Automotive_Platform_Team' : 'TCW02500',
        'Driver_Assistance_Platform_Team' : 'TCW02400',
        'RND_Innovation_Team' : 'TCW04300',
        'Technical_Writing_Team' : 'DEPT186'
        }

team_code_values = list(team_code.values())
team_code_keys = list(team_code.keys())
runfile('C:/Users/B180093/.spyder-py3/user_dataDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
resource = requests.get('https://tcs.telechips.com:8443/rest/api/2/group/member?includeInactiveUsers=false&groupname=' + team_code_values[i], userData)
resource = json.loads(resource.text)
runfile('C:/Users/B180093/.spyder-py3/project_info.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/user_dataDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(type(resource))
data = json.loads(str(resource.text))

## ---(Thu Apr  2 17:14:04 2020)---
runfile('C:/Users/B180093/.spyder-py3/user_dataDB_create.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')
print(team_code[0][1])
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')
resource = requests.get('https://tcs.telechips.com:8443/rest/api/2/group/member?includeInactiveUsers=false&groupname=' + str(team_code[i][1]), userData)
print(resource)
runfile('C:/Users/B180093/.spyder-py3/project_info.py', wdir='C:/Users/B180093/.spyder-py3')
print(url)
runfile('C:/Users/B180093/.spyder-py3/test2.py', wdir='C:/Users/B180093/.spyder-py3')