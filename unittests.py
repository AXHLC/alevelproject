import unittest
from myvalidator import lengthscheck  # the lengthscheck function is in the myvalidator.py file

class TestLengthsCheck(unittest.TestCase):

    def test_equal_length(self):
        self.assertTrue(lengthscheck("hello", 5, 1))
        self.assertFalse(lengthscheck("hello", 6, 1))

    def test_greater_than_length(self):
        self.assertTrue(lengthscheck("hello", 4, 2))
        self.assertFalse(lengthscheck("hello", 6, 2))

    def test_less_than_length(self):
        self.assertTrue(lengthscheck("hello", 6, 3))
        self.assertFalse(lengthscheck("hello", 4, 3))

if __name__ == '__main__':
    unittest.main()