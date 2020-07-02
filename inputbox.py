from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from init import Init

driver = webdriver.Chrome(executable_path=Init.driver)
# driver = webdriver.Firefox(executable_path=Init.driverFirefox)
# driver = webdriver.Safari(executable_path=Init.driverSafari)
driver.get('https://web.drivezytest.com')

driver.implicitly_wait(10)

user_icon_xpath = '//*[@id="root"]/div/div[1]/div/div/div[2]/div[5]'
# username enter
username_textbox_name = 'name'
# Process button click
process_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div.button-section > button'
# Password enter
password_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div:nth-child(3) > input'
# Login button click
login_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div.button-section > button'

driver.find_element_by_xpath(user_icon_xpath).click()
driver.find_element(By.NAME, username_textbox_name).send_keys('govind.patidar@drivezy.com')
driver.find_element(By.CSS_SELECTOR, process_textbox_selector).click()

driver.find_element(By.CSS_SELECTOR, password_textbox_selector).clear()
driver.find_element(By.CSS_SELECTOR, password_textbox_selector).send_keys('Brother794')
driver.find_element(By.CSS_SELECTOR, login_textbox_selector).click()

# click justconnect
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div[1]/span/div').click()
driver.find_element(By.XPATH, '//*[@id="popover-basic"]/div[2]/span/div/div[2]/div').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div[2]').click()

# Buy and existing vehicle list
time.sleep(5)
exit = '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/label/span[1]'
print(driver.find_element(By.XPATH, exit).is_selected())
driver.find_element(By.XPATH, exit).click()
print(driver.find_element(By.XPATH, exit).is_selected())

# justconnect form
name = '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/input'
middle = '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/input'
last = '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/input'

firstName = driver.find_element(By.XPATH, name)
middleName = driver.find_element(By.XPATH, middle)
lastName = driver.find_element(By.XPATH, last)

status = firstName.is_displayed()
print("Displayed or not ", status)

status = firstName.is_enabled()
print("Enabled or not ", status)

firstName.clear()
firstName.send_keys('Sonam')
middleName.clear()
middleName.send_keys('Patidar')
lastName.clear()
lastName.send_keys('Gothi')

# drop and down
location = '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/div/div/div[1]'
element = driver.find_element(By.XPATH, location).click()
# drop = Select(element)
''
# element.select_by_visible_text('Bengaluru')
# drop.select_by_index(2)
element.select_by_value('Bengaluru')

driver.quit()
