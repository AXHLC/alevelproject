import hashlib
import base64
import os
import random
import string
import myvalidator


class passmanager:
    @staticmethod
    def hash_password(password):
        salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        combined = salt + hashed_password
        return base64.b64encode(combined).decode('utf-8')

    @staticmethod
    def verify_password(stored_password, entered_password):
        combined = base64.b64decode(stored_password)
        salt = combined[:16]
        stored_hashed_password = combined[16:]
        new_hashed_password = hashlib.pbkdf2_hmac('sha256', entered_password.encode(), salt, 100000)
        return new_hashed_password == stored_hashed_password


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
    stored_password = passmanager.hash_password(password)
    print(f"The stored password is: {stored_password}")

    entered_password = input("Enter the password again to verify: ")
    if passmanager.verify_password(stored_password, entered_password):
        print("The password is correct.")
    else:
        print("The password is incorrect.")
