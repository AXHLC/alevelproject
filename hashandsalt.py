import hashlib
import base64
import os
import random
import string
import myvalidator


class passmanager:
    @staticmethod
    def hash_password(password):
        # Create a salt
        salt = os.urandom(16)
        # Use the salt and the password to create a hashed password
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        # Base64 encode the salt and hashed password
        salt = base64.b64encode(salt).decode('utf-8')  # Can only base64 encode bytes
        hashed_password = base64.b64encode(hashed_password).decode('utf-8')  # Can only base64 encode bytes
        return salt, hashed_password

    @staticmethod
    def verify_password(salt, hashed_password, entered_password):
        # Decode the base64 encoded salt
        salt = base64.b64decode(salt)
        # Use the salt and the entered password to create a hashed password
        new_hashed_password = hashlib.pbkdf2_hmac('sha256', entered_password.encode(), salt, 100000)
        # Base64 encode the new hashed password
        new_hashed_password = base64.b64encode(new_hashed_password).decode('utf-8')  # Can only base64 encode bytes
        # Check if the new hashed password matches the original hashed password
        return hashed_password == new_hashed_password

    @staticmethod
    def randompassword():
        validator = myvalidator.TheValidation()  # Create an instance of TheValidation class
        while True:
            password = ''.join(
                random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))
            if validator.passcheck(password):  # Call passcheck method on the validator instance
                return password


if __name__ == '__main__':

    password = input("Enter a password: ")
    salt, hashed_password = passmanager.hash_password(password)
    print(f"The salt is: {salt}")
    print(f"The hashed password is: {hashed_password}")

    entered_password = input("Enter the password again to verify: ")
    if passmanager.verify_password(salt, hashed_password, entered_password):
        print("The password is correct.")
        randompassword = passmanager.randompassword()
        print(f"Random password: {randompassword}")
    else:
        print("The password is incorrect.")
        randompassword = passmanager.randompassword()
        print(f"Random password: {randompassword}")
