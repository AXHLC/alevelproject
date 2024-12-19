import hashlib
import os


class passmanager:
    def hash_password(password):
        salt = b'abcdefgh'
        passw = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        hashed_password = salt + passw
        return hashed_password


if __name__ == '__main__':

    password = input("Enter a password: ")
    entered_password = passmanager.hash_password(password)
    print(f"The stored password is: {entered_password}")
    again = passmanager.hash_password(password)
    print(f"The stored password is: {again}")

