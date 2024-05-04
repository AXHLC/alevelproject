import unittest
from myvalidator import MyValidators

class TestLengthsCheck(unittest.TestCase):
    def setUp(self):
        self.validator = MyValidators()

    def test_equal_length(self):
        self.assertTrue(self.validator.lengthscheck("hello", 5, 1))
        self.assertFalse(self.validator.lengthscheck("hello", 6, 1))

    def test_greater_than_length(self):
        self.assertTrue(self.validator.lengthscheck("hello", 4, 2))
        self.assertFalse(self.validator.lengthscheck("hello", 6, 2))

    def test_less_than_length(self):
        self.assertTrue(self.validator.lengthscheck("hello", 6, 3))
        self.assertFalse(self.validator.lengthscheck("hello", 4, 3))

if __name__ == '__main__':
    unittest.main()