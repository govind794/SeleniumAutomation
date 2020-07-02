from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get('http://newtours.demoaut.com/')  # opneing url takes same time

driver.implicitly_wait(10)  # seconds

assert 'Welcome: Mercury Tours' in driver.title

username = driver.find_element_by_name('userName').send_keys('mercury')
password = driver.find_element_by_name('password').send_keys('mercury')

driver.find_element_by_name('login').click()

driver.quit()
