from atlassian import Confluence
import time

now = time.localtime()
s = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)

# Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

data = '<p style="text-align: center;">★ : 완료,&nbsp;<span style="color: rgb(51,102,255);">★</span>&nbsp;: 진행중,&nbsp;<span style="color: rgb(255,0,0);">★</span>&nbsp;: 지연</p>\
<table><colgroup><col /><col /><col /><col /><col /><col /></colgroup>\
<tbody><tr><th style="text-align: center;">Milestone</th><th style="text-align: center;">종료일</th>\
<th style="text-align: center;" colspan="1">상태</th><th style="text-align: center;">미해결 이슈</th>\
<th style="text-align: center;">전체 이슈</th><th style="text-align: center;">특이사항</th></tr>\
<tr><td style="text-align: center;"><a href="https://tcs.telechips.com:8443/browse/TPD/fixforversion/10491">TCCXXXX Linux 1st Release</a></td>\
<td style="text-align: center;">2019/05/31</td>\
<td style="text-align: center;" colspan="1">진행중</td>\
<td style="text-align: center;">10</td>\
<td style="text-align: center;">20</td>\
<td></td></tr>\
<tr><td style="text-align: center;" colspan="1"><a href="https://tcs.telechips.com:8443/browse/TPD/fixforversion/10492">TCCXXXX Linux 2st Release</a></td>\
<td style="text-align: center;" colspan="1">2019/07/31</td>\
<td style="text-align: center;" colspan="1">진행중</td>\
<td style="text-align: center;" colspan="1">29</td>\
<td style="text-align: center;" colspan="1">32</td>\
<td colspan="1"><br /></td></tr>\
<tr><td style="text-align: center;" colspan="1"><a href="https://tcs.telechips.com:8443/browse/TPD/fixforversion/10494">TCCXXXX Linux 3rd Release</a></td>\
<td style="text-align: center;" colspan="1">2019/06/10</td>\
<td style="text-align: center;" colspan="1">지연</td>\
<td style="text-align: center;" colspan="1">0</td>\
<td style="text-align: center;" colspan="1">3</td>\
<td colspan="1"><br /></td></tr>\
</tbody></table><p class="auto-cursor-target"><br /></p><p><br />\
</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="85959282-270a-481c-a73b-82a3b37d96c7">\
<ac:parameter ac:name="title">TCCXXXX Linux 1st Release 마일스톤에서 지연중인 이슈</ac:parameter>\
<ac:rich-text-body><p><ac:structured-macro ac:name="jira" ac:schema-version="1" ac:macro-id="394c50ba-1b13-4a13-9fff-7ff8f112ebe3">\
<ac:parameter ac:name="server">TCS (Telechips Collaboration System)</ac:parameter>\
<ac:parameter ac:name="columns">key,type,priority,summary,status,creator,assignee,created,updated,start date,due</ac:parameter>\
<ac:parameter ac:name="maximumIssues">20</ac:parameter>\
<ac:parameter ac:name="jqlQuery">fixVersion = 10491 AND status not in(Resolved,closed) and due &lt; now() ORDER BY due ASC </ac:parameter>\
<ac:parameter ac:name="serverId">1aff8ec6-5d59-3004-8410-8dc6eceba71e</ac:parameter></ac:structured-macro>\
</p></ac:rich-text-body></ac:structured-macro><p><br /></p>\
<ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9553c4bf-26ff-4b5a-b5db-c198339b4c87">\
<ac:parameter ac:name="title">TCCXXXX Linux 2st Release 마일스톤에서 지연중인 이슈</ac:parameter>\
<ac:rich-text-body><p><ac:structured-macro ac:name="jira" ac:schema-version="1" ac:macro-id="c7ab5435-ea03-4841-aa1f-5649f9f723ad">\
<ac:parameter ac:name="server">TCS (Telechips Collaboration System)</ac:parameter>\
<ac:parameter ac:name="columns">key,type,priority,summary,status,creator,assignee,created,updated,start date,due</ac:parameter>\
<ac:parameter ac:name="maximumIssues">20</ac:parameter>\
<ac:parameter ac:name="jqlQuery">fixVersion = 10492 AND status not in(Resolved,closed) and due &lt; now() ORDER BY due ASC </ac:parameter>\
<ac:parameter ac:name="serverId">1aff8ec6-5d59-3004-8410-8dc6eceba71e</ac:parameter></ac:structured-macro>\
</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>'

# Wiki 특정 페이지 하위에 data를 본문에 넣어서 신규 생성
confluence.create_page(
        space='~B180093',
        title='주간보고 (' + s + ')',
        body='{0}'.format(data),
        parent_id=77172264,
        type='page'
    )