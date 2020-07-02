from selenium import webdriver
from init import Init


driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url11)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

cookie = {'name': 'Mycookies', 'value': '1234559932'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_cookie('Mycookies')

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)