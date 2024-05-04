import unittest
from myvalidator import TheValidation

class TestLengthsCheck(unittest.TestCase):

    # setUp method is there to set up TheValidation object from myvalidator.py
    def setUp(self):
        self.validator = TheValidation()

    # test_equal_length method is there to test the lengthscheck method from myvalidator.py
    def test_equal_length(self):
        self.assertTrue(self.validator.lengthscheck("hello", 5, 1))
        self.assertFalse(self.validator.lengthscheck("hello", 6, 1))

    # test_greater_than_length method is there to test the lengthscheck method from myvalidator.py
    def test_greater_than_length(self):
        self.assertTrue(self.validator.lengthscheck("hello", 4, 2))
        self.assertFalse(self.validator.lengthscheck("hello", 6, 2))

    # test_less_than_length method is there to test the lengthscheck method from myvalidator.py
    def test_less_than_length(self):
        self.assertTrue(self.validator.lengthscheck("hello", 6, 3))
        self.assertFalse(self.validator.lengthscheck("hello", 4, 3))


# testing
if __name__ == '__main__':
    unittest.main()