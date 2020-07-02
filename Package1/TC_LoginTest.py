import unittest


class LoginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print("Login viwa email")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("Login viwa facebook")
        self.assertTrue(True)

    def test_loginByGmail(self):
        print("Login viwa gmail")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
