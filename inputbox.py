from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get('https://web.drivezytest.com')

user_icon_xpath = '//*[@id="root"]/div/div[1]/div/div/div[2]/div[5]'
# username enter
username_textbox_name = 'name'
# Process button click
process_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div.button-section > button'
# Password enter
# password_textbox_selector = '/html/body/div[3]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[3]/input'
password_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div:nth-child(3) > input'
# Login button click
login_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div.button-section > button'

driver.find_element_by_xpath(user_icon_xpath).click()
driver.find_element(By.NAME, username_textbox_name).send_keys('govind.patidar@drivezy.com')
driver.find_element(By.CSS_SELECTOR, process_textbox_selector).click()
driver.find_element_by_css_selector(password_textbox_selector).send_keys('Brother794@')
# driver.find_element(By.CSS_SELECTOR, password_textbox_selector).send_keys('Brother794@')
driver.find_element(By.CSS_SELECTOR, login_textbox_selector).click()

# input = driver.find_element(By.CLASS_NAME, 'form-input')
#
# print(len(input))
