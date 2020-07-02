from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from init import Init

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url6)

driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title)
    if driver.title == 'Frames & windows':
        driver.close()

driver.quit()
