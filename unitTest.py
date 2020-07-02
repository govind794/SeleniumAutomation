import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def setUpModule():
    print("setupModule")


def tearDownModule():
    print("tearDownModule")


class GoogleTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Application run")

    @classmethod
    def tearDownClass(cls):
        print("Close application")

    @classmethod
    def setUp(self):  # execute before all the test methods
        print("This is login test")

    @classmethod
    def tearDown(self):  # execute after all the test method
        print("This logout test case")

    def test_search(self):
        print("wiki pidiya")

    @unittest.skipIf(1 == 1, "One equel to")
    def test_search_drivezy(self):
        print("Drivezy")

    @unittest.SkipTest
    def test_search_test(self):
        print("youtube")

    @unittest.skip('not working test case')
    def test_googlesearch_test(self):
        print("google search")


if __name__ == '__main__':
    unittest.main()
