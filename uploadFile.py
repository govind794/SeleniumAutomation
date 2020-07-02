from selenium import webdriver
from selenium.webdriver.common.by import By
from init import Init
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url1)
driver.implicitly_wait(10)
driver.maximize_window()

driver.switch_to_frame(0)
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="RESULT_FileUpload-10"]').send_keys(
    'file:///Users/govind794/Desktop/License.png')
