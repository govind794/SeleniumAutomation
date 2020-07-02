import unittest


class SignupTest(unittest.TestCase):
    def test_signupByEmail(self):
        print("Signup viwa email")
        self.assertTrue(True)

    def test_signupByFacebook(self):
        print("Signup viwa facebook")
        self.assertTrue(True)

    def test_signupByGmail(self):
        print("Signup viwa gmail")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
