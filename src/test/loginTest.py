from selenium import webdriver
import unittest
from src.main.drivezy.pageFunction.loginPage import LoginPage
from src.main.drivezy.config.initialdata import Initialdata
from src.main.drivezy.head.Initiate import Initiate
import sys
import os

sys.path.append((os.path.join(os.path.dirname(__file__), "...", "...")))


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver')
        Initiate().initialisedriver()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        self.driver.get(Initialdata.url)
        # assert "Self Drive Car Rentals in Bangalore | Rent a car in Bangalore | Drivezy" in self.driver.title
        login = LoginPage(driver)
        # login.login(self)
        login.click_user_icon()
        login.enter_username(Initialdata.username)
        login.click_process_button()
        login.enter_password(Initialdata.password)
        login.click_login_button()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Login")


if __name__ == '__main__':
    unittest.main()

# testRunner=HtmlTestRunner.HTMLTestRunner(
#         output='/Users/govind794/PycharmProjects/AutomationTesting/driver/htmlReport')
