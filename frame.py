from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get('https://www.selenium.dev/selenium/docs/api/java/')

driver.switch_to_frame('packageListFrame')

driver.find_element(By.LINK_TEXT, 'org.openqa.selenium').click()

driver.switch_to_default_content()

driver.switch_to_frame('packageFrame')

driver.find_element(By.LINK_TEXT, 'Action').click()


