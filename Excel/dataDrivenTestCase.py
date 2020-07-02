import openpyxl
import Excel.xlUtis
from selenium import webdriver
from init import Init
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url5)
driver.implicitly_wait(10)
driver.maximize_window()

path = '/Users/govind794/Documents/GitHub/SeleniumAutomation/driver/Testing2.xlsx'

workbook = openpyxl.load_workbook(path)

rows = Excel.xlUtis.getRowCount(path, 'Sheet1')

for r in range(2, rows + 1):
    username = Excel.xlUtis.readData(path, 'Sheet1', r, 1)
    password = Excel.xlUtis.readData(path, 'Sheet1', r, 2)

    driver.find_element(By.NAME, 'userName').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)

    driver.find_element(By.NAME, 'login').click()
    print(driver.title)
    if driver.title == 'Find a Flight: Mercury Tours:':
        print("Test Pass")
        Excel.xlUtis.writeData(path, 'Sheet1', r, 3, 'Test Passed')
    else:
        print('Test Failed')
        Excel.xlUtis.writeData(path, 'Sheet1', r, 3, 'Test Failed')

    driver.find_element(By.LINK_TEXT, 'Home').click()

    print(Excel.xlUtis.readData(path, 'Sheet1', r, 3), end="    ")
    print()
