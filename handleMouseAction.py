from selenium import webdriver
from selenium.webdriver.common.by import By
from init import Init
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url8)
driver.implicitly_wait(10)

institude = driver.find_element(By.XPATH, '//*[@id="fav-nav"]/div/div[3]/ul/li[2]/a')
admin = driver.find_element(By.XPATH, '//*[@id="fav-nav"]/div/div[3]/ul/li[2]/ul/li[4]/a')
nit = driver.find_element(By.XPATH, '//*[@id="fav-nav"]/div/div[3]/ul/li[2]/ul/li[4]/ul/li[2]')

actions = ActionChains(driver)

actions.move_to_element(institude).move_to_element(admin).move_to_element(nit).click().perform()
