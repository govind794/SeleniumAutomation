'''
scroll down the page by pixel
driver.execute_script('window.scrollBy(0,500)', '')
Scroll down the page till element found
driver.execute_script('arg[0].scrollIntoView();', Element)
Scroll the end of the page
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from init import Init

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url4)
print(driver.title)

# driver.execute_script('window.scrollBy(0,1500)', '')

# support = driver.find_element(By.XPATH, '//*[@id="footer"]/div/div[1]/div[1]/div[2]/div[1]/a')
# driver.execute_script('arguments[0].scrollIntoView();', support)

# driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
# driver.quit()
