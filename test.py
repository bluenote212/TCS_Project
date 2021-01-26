import requests
import sqlite3
import simplejson as json
import pandas as pd
from atlassian import Confluence
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

#id_pw를 가져와서 리스트로 변환
con = sqlite3.connect('C:/Users/B180093/database/tcs.db')
user = pd.read_sql("SELECT * FROM id_pw", con)
user_info = user.values.tolist()
con.close()
id_pw = {'os_username': user_info[0][0], 'os_password': user_info[0][1]}

confluence = Confluence(
    url='https://wiki.telechips.com:8443',
    username = user_info[0][0],
    password = user_info[0][1])


scope = ['https://spreadsheets.google.com/feeds']
json_file_name = 'C:/Users/B180093/Downloads/google_key/intrepid-axe-277609-33a1d1aa400c.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1u6e_rS-6CZ_hKyM8fHNNx-wX2mIuGWe3hWq84Hmp4t4/edit?usp=sharing'

sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet('test')
worksheet.update_acell('A1','=sum(b1:c1)')