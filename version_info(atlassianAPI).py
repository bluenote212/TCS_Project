from atlassian import Confluence
from atlassian import Jira
import time

# 현재 시간정보
now = time.localtime()
s = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)

# 프로젝트 Key
project1 = 'TPD'


# jira auth
jira = Jira(
    url='https://tcs.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')


# Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')


# TCS 버전정보 Get
tcs_r = jira.get_project_versions(project1, expand=None)
print(tcs_r)

# 해당 프로젝트에 입력된 모든 버전의 name, releaseDate, overdue 출력
data = ''
for i in range(0, len(tcs_r)):
    if 'releaseDate' in tcs_r[i]:
        r = '<p>'+ '마일스톤 : ' + tcs_r[i]['name'] + '</p>'+ '<p>' + '종료일 : ' + tcs_r[i]['releaseDate'] + '</p>'
    else:
        r = '<p>'+ '마일스톤 : ' + tcs_r[i]['name'] + '</p>'+ '<p>' + '종료일 : 없음' + '</p>'
    if 'overdue' in tcs_r[i]:
        if tcs_r[i]['overdue'] is True:
            r = r + '<p>상태 : <strong><span style="color: rgb(255,0,0);">지연</span></strong></p>'
            data = data + r + '<p><br /></p>'
        else:
            if tcs_r[i]['released'] is True:
                r = r + '<p>상태 : <strong><span style="color: rgb(0,0,255);">완료</span></strong></p>'
                data = data + r + '<p><br /></p>'
            else:
                r = r + '<p>상태 : <strong><span style="color: rgb(0,0,255);">진행중</span></strong></p>'
                data = data + r + '<p><br /></p>'
    else:
        if tcs_r[i]['released'] is True:
            r = r + '<p>상태 : <strong><span style="color: rgb(0,0,255);">완료</span></strong></p>'
            data = data + r + '<p><br /></p>'
        else:
            data = data + r + '<p><br /></p>'

print(data)

# Wiki 특정 페이지 하위에 data를 본문에 넣어서 신규 생성
confluence.create_page(
        space='~B180093',
        title='주간보고 (' + s + ')',
        body='{0}'.format(data),
        parent_id=77172264,
        type='page'
    )
