import re
import calendar


# This class is used to validate the input of the user
class TheValidation:

    def __init__(self):
        pass

    # length check
    def lengthscheck(self, string, nums, option):
        # string = the string we are checking the length of
        # nums = the number we are comparing the length to
        # option = 1 for equal, 2 for greater than, 3 for less than
        if option == 1:
            if len(string) == nums:
                return True
            return False
        elif option == 2:
            if len(string) >= nums:
                return True
            return False
        elif option == 3:
            if len(string) <= nums:
                return True
            return False

    # email check
    def emailcheck(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        else:
            return False

    # password check
    def passcheck(self, password):
        # Checks that the variable password has at least one digit, one uppercase letter, one special character, and a minimum length of 8
        return bool(re.search(r'^(?=.*\d)(?=.*[A-Z])(?=.*[+?#£%&]).{8,}$', password))

    # range check
    def rangecheck(self, number, lower, upper):
        # Check the value of the number to be between two other values
        return lower <= number <= upper

    # presence check
    def prescheck(self, inp):
        # Checks something has been inputted
        return bool(inp)

    # age check
    def age(self, data):
        if re.match(r'^[0-9]+$', data) and 0 < int(data) < 150:
            return True
        return False


    # date check
    def datecheck(self, date):
        # This function checks if the given date is in the format DD/MM/YYYY.
        # date can only be between the years 1900 and 2099
        pattern = r'^([0-2][0-9]|(3)[0-1])/(0?[1-9]|1[012])/((19|20)\d\d)$'
        if re.fullmatch(pattern, date):
            day, month, year = map(int, date.split('/'))
            if self.monthcheck(month) and self.yearcheck(year):
                if month == 2 and day == 29 and not self.leapyearcheck(year):
                    return False
                elif self.daycheck(day, month, year):
                    return True
            return False
        else:
            return False

    # leap year check
    def leapyearcheck(self, lyear):
        # This function checks if the given year is a leap year.
        # year: the year to check
        return calendar.isleap(lyear)

    # day check
    def daycheck(self, day, month, year):
        # This function checks if the given day is valid.
        # day: the day to check
        # month: the month to check
        # year: the year to check (for leap years)
        if month in [4, 6, 9, 11]:
            return 1 <= day <= 30
        elif month == 2:
            if self.leapyearcheck(year):
                return 1 <= day <= 29
            else:
                return 1 <= day <= 28
        else:
            return 1 <= day <= 31

    # month check
    def monthcheck(self, month):
        # This function checks if the given month is valid.
        # month: the month to check
        return 1 <= month <= 12

    # year check
    def yearcheck(self, year):
        # This function checks if the given year is valid.
        # year: the year to check
        return 1900 <= year <= 2099

    # birthday check
    def birthdaycheck(self, birth):
        if re.match(r'^\d{4}/\d{2}/\d{2}$', birth) and 1900 < int(birth[:4]) < 2020 and 0 < int(
                birth[5:7]) < 13 and 0 < int(birth[8:10]) < 32:
            return True
        return False

    # phone check
    def phonecheck(self, contact):
        # Checks weather the number is a valid UK phone number
        pattern = r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$'
        return bool(re.fullmatch(pattern, contact))

    # name check
    def namecheck(self, name):
        pattern = r'^[a-zA-Z]+(?:[ -][a-zA-Z]+)*$'
        return bool(re.fullmatch(pattern, name))

    # username check
    def usernamecheck(self, username):
        # Can have any combination of lowercase letters, digits, underscores, dots, or hyphens
        # Must have 3 consecutive letters
        username = username.lower()
        pattern = r'[a-z]{3}'
        if len(username) <= 8 and re.search(pattern, username):
            return True
        return False


# testing


if __name__ == "__main__":
    validator = TheValidation()
    # print(validator.lengthscheck("b3338", 10, 3))
    # print(validator.emailcheck("dirguh@dfklj.com"))
    # print(validator.passcheck("thhhhhs"))
    # print(validator.rangecheck(23, 2, 60))
    # print(validator.prescheck(""))
    # print(validator.usernamecheck("achl06."))
