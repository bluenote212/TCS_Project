from atlassian import Confluence
#from bs4 import BeautifulSoup

#Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username='b180093',
    password='infra4938hc!')

page_info_body1 = confluence.get_page_by_id(51357475, expand='body.storage')

print(page_info_body1['body']['storage']['value'])
