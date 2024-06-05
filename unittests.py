import unittest
from myvalidator import TheValidation

# unit test on lengths check method
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

# unit test on email check method
class TestEmailCheck(unittest.TestCase):

    # setUp method is there to set up TheValidation object from myvalidator.py
    def setUp(self):
        self.validator = TheValidation()

    # test_email_check method is there to test the emailcheck method from myvalidator.py
    def validemail(self):
        valid_emails = [
            'user@example.com',
            'email@example.co.jp',
            'firstname-lastname@example.com',
            'email@example.museum',
            'email@example.name',
            '_______@example.com',
            '1234567890@example.com',
            'email@123.123.123.123'
        ]

        for email in valid_emails:
            # Tests valid emails
            self.assertTrue(self.validator.emailcheck(email))


    def invalidemail(self):
        invalid_emails = [
            'plainaddress',
            '@missingusername.com',
            'noat.com',
            'nodotcom.',
            'nodullstop@',
            '124353552555.com',
            'email@11',]

        for email in invalid_emails:
            # Tests invalid emails
            self.assertFalse(self.validator.emailcheck(email))

    def test_email_check(self):
        self.validemail()
        self.invalidemail()

# unit test on username check method
class testusernamecheck(unittest.TestCase):

    def setUp(self):
        self.validator = TheValidation()

    def validusername(self,):
        valid_usernames = [
            'achl06.',
            'AaBbCC',
            'ABC-456',
            'USER123',
            'Pats.3-',
            'kNIt.69',
            'Ely-12',
            'falciat',
            'ABC',
            '12ERT5',
        ]

        for user in valid_usernames:
            # Tests valid usernames
            self.assertTrue(self.validator.usernamecheck(user))

    def invalidusername(self,):
        invalid_usernames = [
            'achl06875687587.',
            '646734365',
            'A54345',
            'a1b2c3',
            ']hh555',
            'kn7it7g]',
            'El-y-12',
            'fa778',
            'AC',
            '1',
        ]

        for user in invalid_usernames:
            # Tests invalid usernames
            self.assertFalse(self.validator.usernamecheck(user))
# testing
if __name__ == '__main__':
    unittest.main()

