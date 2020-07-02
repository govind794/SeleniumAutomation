from selenium import webdriver
from selenium.webdriver.common.by import By
from init import Init
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url1)
# driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="field1"]').clear()
field = driver.find_element(By.XPATH, '//*[@id="field1"]').send_keys('selenium')

element = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')

actions = ActionChains(driver)
actions.double_click(element).perform()
