import unittest


class PaymentTest(unittest.TestCase):
    def test_paymentByDoller(self):
        print("Payment by doller")
        self.assertTrue(True)

    def test_paymentByupess(self):
        print("Payment by rupess")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
