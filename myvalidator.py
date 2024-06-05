import re


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
        # Checks that the variable password has the characters necessary
        return bool(re.search(r'(?=.*\d)(?=.*[A-Z])(?=.*[+?#£%&])', password))

    # range check
    def rangecheck(self, number, lower, upper):
        # Check the value of the number to be between two other values
        return lower <= number <= upper

    # presence check
    def prescheck(self, inp):
        # Checks something has been inputted
        return bool(inp)

    # date check
    # leap year check
    # day check
    # month check
    # year check
    # birthday check
    def birthdate(self, birth):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', birth) and 1900 < int(birth[:4]) < 2020 and 0 < int(
                birth[5:7]) < 13 and 0 < int(birth[8:10]) < 32:
            return True
        return False

    # phone check
    def phone(self, contact):
        # Checks weather the number is a valid UK phone number
        pattern = r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$'
        return bool(re.fullmatch(pattern, contact))

    # name check
    def name(self, name):
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
        else:
            return False

    # age check
    # birthday check [make sure they are withing age range 0-150, valid date format from first function]

# testing


if __name__ == "__main__":
    validator = TheValidation()
    # print(validator.lengthscheck("b3338", 10, 3))
    # print(validator.emailcheck("dirguh@dfklj.com"))
    # print(validator.passcheck("t8hareeAnonu?ms"))
    # print(validator.rangecheck(23, 2, 60))
    # print(validator.prescheck(""))
    # print(validator.usernamecheck("achl06."))
