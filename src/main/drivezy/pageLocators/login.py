from selenium.webdriver.common.by import By


class Locators():
    def __init__(self, driver):
        self.driver = driver

    # user icon click
    user_icon_xpath = '//*[@id="root"]/div/div[1]/div/div/div[2]/div[5]'
    # user_icon = By.XPATH = '//*[@id="root"]/div/div[1]/div/div/div[2]/div[5]'
    # def user_icon(self):
    #     return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div[5]').click()

    # username enter
    username_textbox_name = 'name'
    # Process button click
    process_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div.button-section > button'
    # Password enter
    password_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div:nth-child(3) > input'
    # Login button click
    login_textbox_selector = 'body > div.atlaskit-portal-container > div > div > div:nth-child(3) > div.css-1m0lomi > div > div > div > div.modal-body > div > div > div.username-container > div > div > div > div.button-section > button'
