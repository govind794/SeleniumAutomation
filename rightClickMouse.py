from selenium import webdriver
from selenium.webdriver.common.by import By
from init import Init
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url9)
driver.implicitly_wait(10)
driver.maximize_window()

username = '//*[@id="exampleInputEmail1"]'
password = '//*[@id="exampleInputPassword1"]'
login = '//*[@id="parent-admin-element"]/div[1]/div/div[1]/div/form/div[2]/button'

driver.find_element(By.XPATH, username).clear()
driver.find_element(By.XPATH, password).clear()

driver.find_element(By.XPATH, username).send_keys(Init.username)
driver.find_element(By.XPATH, password).send_keys(Init.password)
driver.find_element(By.XPATH, login).click()

header = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/span/div/div')

actions = ActionChains(driver)
actions.context_click(header).perform()
