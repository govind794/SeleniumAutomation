from selenium import webdriver
from selenium.webdriver.common.by import By
from init import Init

driver = webdriver.Chrome(executable_path=Init.driver)

driver.get(Init.url7)

rows = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr')  # count no of rows
cols = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[1]/th')  # count no of cols
print(len(rows))
print(len(cols))
print("Product" + "  " + "Artical" + " " + "Price")
for r in range(2, len(rows) + 1):
    for c in range(1, len(cols) + 1):
        value = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text
        print(value, end=" ")
    print()

driver.quit()
