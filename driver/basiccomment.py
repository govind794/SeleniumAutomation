from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://web.drivezytest.com/Bengaluru")
print(driver.title)  # return the title of the page
print(driver.current_url)  # return the current url in the page

driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[2]/div[3]/span/div').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="popover-basic"]/div[2]/span/div/a[1]/div').click()

# driver.close() #close currently focused browser
driver.quit()  # close all browser
