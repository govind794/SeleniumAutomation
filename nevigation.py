from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get('https://drivezy.com')
print(driver.title)

driver.get('https://drivezytest.com')
time.sleep(5)

print(driver.title)

driver.back()
time.sleep(5)

print(driver.title)

driver.forward()
time.sleep(5)

print(driver.title)

driver.quit()