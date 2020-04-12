from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# class Initiate():
#      webdriver.driver = None
#
#      def Initiate(self):

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# driver = webdriver.Firefox(executable_path='')
driver.get('https://drivezy.com')

# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath('//*[@id="offers"]').click()
time.sleep(5)

# driver.close()  # currently focuse browser
driver.quit()  # close all tab
