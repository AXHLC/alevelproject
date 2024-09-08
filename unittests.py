import unittest
from modules.myvalidator import TheValidation

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

class testpasscheck(unittest.TestCase):

    def setUp(self):
        self.validator = TheValidation()

    def validpass(self,):
        valid_passwords = [
            'MenuSir56&',
            'Ahmed9%',
            'Elyas8£',
            'Benjamin7+',
            'Gustavo6#',
            'heLLOO5&',
            'bYebYe4%',
            'cAtipillar3£',
            'Konichiwa2+',
            'Thisisright1#',
        ]

        for password in valid_passwords:
            # Tests valid passwords
            self.assertTrue(self.validator.passcheck(password))

    def invalidpass(self,):
        invalid_passwords = [
            'password1',
            'ALLCAPS',
            'nonumberscaps?',
            'less6',
            'plain',
            'bob>?',
            'El-y-12',
            'fa778',
            'AC',
            '1',
        ]

        for password in invalid_passwords:
            # Tests invalid passwords
            self.assertFalse(self.validator.passcheck(password))

class testrangecheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_range_lower_boundary(self):
        self.assertTrue(self.validator.rangecheck(5, 5, 10), "Failed on lower boundary")

    def test_range_upper_boundary(self):
        self.assertTrue(self.validator.rangecheck(10, 5, 10), "Failed on upper boundary")

    def test_range_within_range(self):
        self.assertTrue(self.validator.rangecheck(7, 5, 10), "Failed within range")

    def test_range_below_range(self):
        self.assertFalse(self.validator.rangecheck(4, 5, 10), "Failed below range")

    def test_range_above_range(self):
        self.assertFalse(self.validator.rangecheck(11, 5, 10), "Failed above range")

class testprescheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_pres_with_input(self):
        self.assertTrue(self.validator.prescheck("Hello"), "Failed with input")

    def test_pres_without_input(self):
        self.assertFalse(self.validator.prescheck(""), "Failed without input")

class testagecheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_age_valid_age(self):
        self.assertTrue(self.validator.age("25"), "Failed with valid age")

    def test_age_invalid_age(self):
        self.assertFalse(self.validator.age("200"), "Failed with invalid age")

    def test_age_non_numeric_input(self):
        self.assertFalse(self.validator.age("twenty"), "Failed with non-numeric input")

class testdatecheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_date_valid_date(self):
        self.assertTrue(self.validator.datecheck("25/12/2020"), "Failed with valid date")

    def test_date_invalid_date(self):
        self.assertFalse(self.validator.datecheck("30/02/2020"), "Failed with invalid date")

    def test_date_invalid_format(self):
        self.assertFalse(self.validator.datecheck("2020/12/25"), "Failed with invalid format")
class testleapyearcheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_leapyear_is_leap_year(self):
        self.assertTrue(self.validator.leapyearcheck(2020), "Failed with leap year")

    def test_leapyear_non_leap_year(self):
        self.assertFalse(self.validator.leapyearcheck(2021), "Failed with non-leap year")
class testdaycheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_day_valid_day(self):
        self.assertTrue(self.validator.daycheck(15, 5, 2020))

    def test_day_invalid_day(self):
        self.assertFalse(self.validator.daycheck(31, 4, 2020))

    def test_day_february_leap_year(self):
        self.assertTrue(self.validator.daycheck(29, 2, 2020))

    def test_day_february_non_leap_year(self):
        self.assertFalse(self.validator.daycheck(29, 2, 2019))
class testmonthcheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_month_valid_month(self):
        self.assertTrue(self.validator.monthcheck(5))

    def test_month_invalid_month(self):
        self.assertFalse(self.validator.monthcheck(13))
class testyearcheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_year_valid_year(self):
        self.assertTrue(self.validator.yearcheck(2020))

    def test_year_invalid_year(self):
        self.assertFalse(self.validator.yearcheck(1899))

    def test_year_future_year(self):
        self.assertFalse(self.validator.yearcheck(2100))
class testbirthdaycheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_birthday_valid_birthday(self):
        self.assertTrue(self.validator.birthdaycheck("2000/05/15"))

    def test_birthday_invalid_birthday(self):
        self.assertFalse(self.validator.birthdaycheck("1899/04/31"))

    def test_birthday_invalid_format(self):
        self.assertFalse(self.validator.birthdaycheck("15-05-2000"))
class testphonecheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_phone_valid_phone(self):
        self.assertTrue(self.validator.phonecheck("+44 1234 567 890"))

    def test_phone_invalid_phone(self):
        self.assertFalse(self.validator.phonecheck("1234567890"))
class testnamecheck(unittest.TestCase):
    def setUp(self):
        self.validator = TheValidation()

    def test_name_valid_name(self):
        self.assertTrue(self.validator.namecheck("Ahmed Chaal"))

    def test_name_invalid_name(self):
        self.assertFalse(self.validator.namecheck("Ahmed123"))

# testing
if __name__ == '__main__':
    unittest.main()

