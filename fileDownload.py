from selenium import webdriver
from selenium.webdriver.common.by import By
from init import Init
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.chrome.options import Options

chromeOption = Options()
chromeOption.add_experimental_option('prefs', {'download.default_directory': '/Users/govind794/Desktop/Postman_reports'})

driver = webdriver.Chrome(executable_path=Init.driver, chrome_options=chromeOption)

driver.get(Init.url10)
driver.implicitly_wait(10)
driver.maximize_window()

# driver.find_element(By.XPATH, '//*[@id="textbox"]').send_keys("govind patidar")
# driver.find_element(By.XPATH, '//*[@id="createTxt"]').click()
# driver.find_element(By.XPATH, '//*[@id="link-to-download"]').click()

# pdf file download
driver.find_element(By.ID, 'pdfbox').send_keys("Selenium webdriver")
driver.find_element(By.XPATH, '//*[@id="createPdf"]').click()
driver.find_element(By.XPATH, '//*[@id="pdf-link-to-download"]').click()
