from selenium import webdriver
from init import Init

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url11)
driver.implicitly_wait(10)
driver.maximize_window()

# driver.save_screenshot('/Users/govind794/Documents/GitHub/SeleniumAutomation/driver/home.png')

driver.get_screenshot_as_file('/Users/govind794/Documents/GitHub/SeleniumAutomation/driver/home.png')
