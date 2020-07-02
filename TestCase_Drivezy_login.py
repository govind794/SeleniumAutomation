from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest
import HtmlTestRunner
import time

from init import Init


class Drivezy_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=Init.driver)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_homePageTitle(self):
        self.driver.get(Init.url4)

        drivezy_title = 'Self Drive Car, Scooter & Bike Rentals in Bangalore | Drivezy'
        self.assertEqual(drivezy_title, self.driver.title, 'webpage title not matching')

    def test_login(self):
        self.driver.get(Init.url4)

        user_icon_xpath = '//*[@id="root"]/div/div[1]/div/div/div[2]/div[5]'
        # username enter
        username_textbox_name = 'name'
        # Process button click
        process_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div.button-section > button'
        # Password enter
        password_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div:nth-child(3) > input'
        # Login button click
        login_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div.button-section > button'

        self.driver.find_element_by_xpath(user_icon_xpath).click()
        self.driver.find_element(By.NAME, username_textbox_name).send_keys('govind.patidar@drivezy.com')
        self.driver.find_element(By.CSS_SELECTOR, process_textbox_selector).click()

        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, password_textbox_selector).clear()
        self.driver.find_element(By.CSS_SELECTOR, password_textbox_selector).send_keys('Brother794')
        self.driver.find_element(By.CSS_SELECTOR, login_textbox_selector).click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("\n......Test completed......")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='/Users/govind794/Documents/GitHub/SeleniumAutomation/driver/reports'))
