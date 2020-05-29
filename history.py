con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

#team code를 DB에서 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
team_code = pd.read_sql("SELECT * FROM team_code", con)
con.close()
team_code = team_code.values.tolist()

#project info를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
data2 = pd.read_sql("SELECT * FROM project_key", con)
con.close()
project_key = data2.values.tolist()

#검증하고 싶은 년, 월을 지정
days_start = '2020-04-1'
days_end = '2020-04-30'

#현재 월의 첫째날을 출력
day = datetime.now()
first_day = day.replace(day=1)

#전 월의 년도, 월, 첫째날, 마지막 날을 출력
first_day_1 = first_day - relativedelta(months=1)
year_1 = first_day_1.year #전 월의 년도
month_1 = first_day_1.month
last_day = calendar.monthrange(year_1,month_1)[1]

print(year_1)
print(month_1)
print(first_day_1)
print(last_day)
runfile('C:/Users/B180093/.spyder-py3/test3.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/before_month_worklog_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(data['worklog_timespent'].sum())
print(len(data_resource))
runfile('C:/Users/B180093/.spyder-py3/before_month_worklog_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(url)
runfile('C:/Users/B180093/.spyder-py3/test3.py', wdir='C:/Users/B180093/.spyder-py3')
print(url_1)
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(len(data))
runfile('C:/Users/B180093/.spyder-py3/before_month_worklog_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(len(data))
print(data['worklog_timespent'].sum())
runfile('C:/Users/B180093/.spyder-py3/before_month_worklog_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Fri May 22 09:20:29 2020)---
runfile('C:/Users/B180093/.spyder-py3/before_month_worklog_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(len(data_resource[0]))
print(data_resource[0])
runfile('C:/Users/B180093/.spyder-py3/before_month_worklog_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')
print(data_resource[0])
print(len(data_resource[0]))
runfile('C:/Users/B180093/.spyder-py3/before_month_worklog_DB_create.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Mon May 25 16:30:07 2020)---
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(team_code.index[0])
print(team_code.index[1])
print(team_code.index)
print(team_code.index(0))
print(team_code.loc[0]
print(team_code.loc[0])
print(team_code.loc[0]['issue_dhip'])
print(team_code.loc[0]['issue_chip'])
print(team_code.loc[0])
print(team_code.loc[16])
print(team_code.loc[15])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(team_code[15]['issue_chip'])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Tue May 26 11:35:42 2020)---
runfile('C:/Users/B180093/.spyder-py3/month_worklog_DBcreate.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/worklogdata_recalculate.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/unit_test_origindata2.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test3.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Wed May 27 10:14:37 2020)---
runfile('C:/Users/B180093/.spyder-py3/test3.py', wdir='C:/Users/B180093/.spyder-py3')
print(data_resource[data_resource['auto/ce'] == 'ce'])
print(data_resource[data_resource['resource_category'] == '기타'])
print(data_resource[data_resource['auto/ce'] == 'auto'])
runfile('C:/Users/B180093/.spyder-py3/test3.py', wdir='C:/Users/B180093/.spyder-py3')
print(data_resource[data_resource['auto_ce'] == 'ce'])
print(data_resource[data_resource['resource_category'] == '기타'])
print(data_resource[data_resource['resource_category'] == '개발'])
print(data_resource[data_resource['resource_category'] == '지원'])
runfile('C:/Users/B180093/.spyder-py3/test3.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/month_worklog_DBcreate.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Wed May 27 13:10:36 2020)---
runfile('C:/Users/B180093/.spyder-py3/month_worklog_DBcreate.py', wdir='C:/Users/B180093/.spyder-py3')
runfile('C:/Users/B180093/.spyder-py3/test3.py', wdir='C:/Users/B180093/.spyder-py3')
print(data_resource.columns)
runfile('C:/Users/B180093/.spyder-py3/test3.py', wdir='C:/Users/B180093/.spyder-py3')

## ---(Fri May 29 10:57:02 2020)---
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')
print(data['issues'][0])
runfile('C:/Users/B180093/.spyder-py3/test.py', wdir='C:/Users/B180093/.spyder-py3')