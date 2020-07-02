from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get('http://newtours.demoaut.com/')  # opneing url takes same time

driver.implicitly_wait(10)  # seconds

assert 'Welcome: Mercury Tours' in driver.title

links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links", len(links))

for link in links:
    print(link)
