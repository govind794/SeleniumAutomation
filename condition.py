from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get("https://drivezy.com")
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[2]/div[5]').click()
time.sleep(1)
name = driver.find_element_by_name("name")

print(name.is_displayed()) #return true/false based of element stauts
print(name.is_enabled()) # return true/flase

name.send_keys("govind.patidar@drivezy.com")
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[9]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]").click()
# driver.find_element_by_class_name("aws-btn aws-btn--btntheme aws-btn--large aws-btn--visible aws-btn--progress").click()
# driver.find_element_by_css_selector("body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div.button-section > button").click()
time.sleep(10)

# password = driver.find_element_by_name("password")
# password = driver.find_element_by_css_selector("body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div:nth-child(3) > input");
# print(password.is_displayed()) #return true/false based of element stauts
# print(password.is_enabled()) # return true/flase
# password.send_keys("Brother794")
#
#
# driver.find_element_by_css_selector("body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div.button-section > button").click()
# time.sleep(3)
#
#
# driver.close()