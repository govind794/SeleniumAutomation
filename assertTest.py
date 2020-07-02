import unittest
from selenium import webdriver
from init import Init


class Test(unittest.TestCase):
    def test_google(self):
        # driver = webdriver.Chrome(executable_path=Init.driver)
        # driver.get('https://www.google.com/')
        # google_title = driver.title
        # # self.assertEqual('google', google_title, "title is not same")
        # # self.assertNotEqual('google', google_title)
        # self.assertTrue(google_title == 'Google')
        # self.assertIsNone(driver)
        # self.assertIsNotNone(driver)

        list = ["python", "java", "script"]
        # self.assertIn("java1", list)
        self.assertNotIn('script1', list)


if __name__ == '__main__':
    unittest.main()
