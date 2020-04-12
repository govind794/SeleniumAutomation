from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import platform
from src.main.drivezy.config.initialdata import Initialdata


class Initiate():
    browserName = Initialdata.browser

    def initialisedriver(self):
        # if platform.system() == "Darwin":
        #     try:
        #         webdriver.Chrome(
        #             executable_path='/Users/govind794/PycharmProjects/AutomationTesting/driver/chromedriver')
        #     except NoSuchElementException:
        #         time.sleep(1)
        # elif platform.system() == "linux":
        #     try:
        #         webdriver.Chrome(
        #             executable_path='/Users/govind794/PycharmProjects/AutomationTesting/driver/chromedriver')
        #     except NoSuchElementException:
        #         time.sleep(1)
        # elif platform.system() == "win64":
        #     try:
        #         webdriver.Chrome(
        #             executable_path='/Users/govind794/PycharmProjects/AutomationTesting/driver/chromedriver')
        #     except NoSuchElementException:
        #         time.sleep(1)

        if platform.system() == "Darwin":
            if self.browserName == 'Chrome':
                options = webdriver.ChromeOptions()
                options.add_argument('--start--fullscreen')
                driver = webdriver.Chrome()
                driver.get(Initialdata.url)
