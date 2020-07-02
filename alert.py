from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# driver = webdriver.Ie(executable_path=)
driver.get('http://testautomationpractice.blogspot.com/')

driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()

time.sleep(4)
# driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()
