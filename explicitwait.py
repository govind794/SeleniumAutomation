from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

driver.get('https://www.expedia.com/')

driver.implicitly_wait(5)
driver.maximize_window()

# checkin = driver.find_element_by_id('tab-flight-tab-hp').click()

driver.find_element(By.ID, 'tab-flight-tab-hp').click()  # flight button
driver.find_element(By.ID, 'flight-type-roundtrip-label-hp-flight')  # round trip button

driver.find_element(By.ID, 'flight-origin-hp-flight').send_keys('Indore (IDR-Devi Ahilyabai Holkar Intl.)')
time.sleep(5)

driver.find_element(By.ID, 'flight-destination-hp-flight').clear()
driver.find_element(By.ID, 'flight-destination-hp-flight').send_keys('Bengaluru (BLR-Kempegowda Intl.)')

driver.find_element(By.ID, 'flight-departing-hp-flight').clear()
# driver.find_element(By.ID, 'flight-departing-hp-flight').send_keys('06/11/2020')

driver.find_element(By.ID, 'flight-departing-hp-flight').click()
driver.find_element(By.XPATH,'//*[@id="flight-departing-wrapper-single-hp-flight"]/div/div[2]/button[2]').click()
driver.find_element(By.XPATH, '//*[@id="flight-departing-wrapper-single-hp-flight"]/div/div[2]/div[3]/table/tbody/tr[2]/td[5]/button').click()
# time.sleep(2)

# driver.find_element(By.ID, 'flight-returning-hp-flight').clear()
# driver.find_element(By.ID, 'flight-returning-hp-flight').send_keys('06/12/2020')
#
# driver.find_element(By.XPATH, '//*[@id="gcw-flights-form-hp-flight"]/div[8]/label/button').click()
#
# wait = WebDriverWait(driver, 10)
#
# element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stopFilter_stops-1"]'))).click()
# time.sleep(3)

# driver.quit()
