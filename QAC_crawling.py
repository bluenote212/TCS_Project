from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('C:/Users/B180093/python_test/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(2)

driver.get('http://192.168.33.15:8080/')
driver.implicitly_wait(10)

driver.find_element_by_id('login_username').send_keys('admin')
driver.find_element_by_id('login_password').send_keys('qwer1234!')
driver.implicitly_wait(1)
driver.find_element_by_id('login_button_container').click()

driver.implicitly_wait(10)

html_id = driver.find_element_by_id('db_list')
html_id = driver.page_source
soup = BeautifulSoup(html_id, 'html.parser')
table = soup.find(class_='metricsTable')
#driver.quit() #모든탭 종료

tr = table.find_all('tr')

project_list = []
for i in range(0, len(tr)):
    project_list.append(tr[i]['onclick'].split('"')[1])


driver.get('http://192.168.33.15:8080/viewer.html?&db=' + project_list[-1] + \
'&ss=1&bl=&sv=0&sps=#JmFubj0mbWxpc3Q9JnRyZWVpdGVtPSZ0cmVldGFiPTEmYW5ubXNnPSZhbm5saW5lPSZzcz0mYmw9JnNoPTAmc3Y9MCZocD0mc209JnhhPSZobj0mc3BzPSZtZj0=')
driver.implicitly_wait(5)
time.sleep(5)

html_result = driver.find_element_by_css_selector('td.trStAdjCol_1')
driver.implicitly_wait(3)
html_result = driver.page_source
soup_td = BeautifulSoup(html_result, 'html.parser')
result_td1 = soup_td.find_all(class_='trStAdjCol_1')
result_td2 = soup_td.find_all(class_='trStAdjCol_2')

print('Active : ' + result_td1[2].text)
print('Total : ' + result_td2[2].text)