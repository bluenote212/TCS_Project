from atlassian import Confluence
import pandas as pd
import sqlite3
#from bs4 import BeautifulSoup

con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()

#Wiki auth
confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password=user_info[0][1])

page_info_body1 = confluence.get_page_by_id(122588081, expand='space,body.view,version,container')

print(page_info_body1)
