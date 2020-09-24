from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/B180093/python_test/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(2)

driver.get('http://192.168.33.15:8080/')
driver.implicitly_wait(1)

driver.find_element_by_id('login_username').send_keys('admin')
driver.find_element_by_id('login_password').send_keys('qwer1234!')
driver.implicitly_wait(1)
driver.find_element_by_id('login_button_container').click()

driver.implicitly_wait(10)

#html_id = driver.find_element_by_id('db_list')
#html_xpath = driver.find_element_by_xpath('//*[@id="db_list"]')
html_css = driver.find_element_by_css_selector('#db_list_contents > table')


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.find_all('td'))
