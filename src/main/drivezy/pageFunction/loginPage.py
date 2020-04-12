from src.main.drivezy.pageLocators.login import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def click_user_icon(self):
        self.driver.find_element_by_xpath(Locators.user_icon_xpath).click()

    # def login(self):
    #     Locators.user_icon(self)

    def enter_username(self, username):
        self.driver.find_element_by_name(Locators.username_textbox_name).clear()
        self.driver.find_element_by_name(Locators.username_textbox_name).send_keys(username)

    def click_process_button(self):
        self.driver.find_element_by_css_selector(Locators.process_textbox_selector).click()

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(Locators.password_textbox_selector).clear()
        self.driver.find_element_by_css_selector(Locators.password_textbox_selector).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_css_selector(Locators.login_textbox_selector).click()
