from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get('http://newtours.demoaut.com/')

userName = driver.find_element_by_name('userName')

print(userName.is_displayed())  # return true/false based on element status
print(userName.is_enabled())  # return true/false based on element status

password = driver.find_element_by_name('password')
print(userName.is_displayed())  # return true/false based on element status
print(userName.is_enabled())  # return true/false based on element status

userName.send_keys('mercury')
password.send_keys('mercury')

driver.find_element_by_name('login').click()

roundtrip = driver.find_element_by_css_selector('input[value=roundtrip]')
print(roundtrip.is_selected())  # status of radio button round trip

oneway = driver.find_element_by_css_selector('input[value=oneway]')
print(oneway.is_selected())  # status of radio button round trip


# selected_element = [x for x in roundtrip if x.get_attribute('value') ==' roundtrip']
# if len(selected_element):
#     print(selected_element.is_selected())


driver.quit()
