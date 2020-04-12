import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.addCleanup(self.browser.quit)
        self.browser.implicitly_wait(10)
        self.browser.maximize_window()

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.browser.find_element_by_name("q")

        # enter search keyword and submit
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()

        # get the list of elements which are displayed after the search
        # currently on result page usingfind_elements_by_class_namemethod

        lists = self.browser.find_elements_by_class_name("r")
        no = len(lists)
        self.assertEqual(10, len(lists))


if __name__ == '__main__':
    unittest.main(verbosity=2)
