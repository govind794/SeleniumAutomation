from selenium import webdriver
from selenium.webdriver.common.by import By
from init import Init
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url1)
driver.implicitly_wait(10)
driver.maximize_window()

source = driver.find_element(By.XPATH, '//*[@id="gallery"]/li[1]/img')
trager = driver.find_element(By.XPATH, '//*[@id="trash"]')

actions = ActionChains(driver)

time.sleep(3)
actions.drag_and_drop(source, trager).perform()
