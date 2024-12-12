import hashlib
import os


class passmanager:
    def hash_password(password):
        salt = b'abcdefgh'
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        hashed_password = salt + key
        return hashed_password


if __name__ == '__main__':

    password = input("Enter a password: ")
    stored_password = passmanager.hash_password(password)
    print(f"The stored password is: {stored_password}")
    again = passmanager.hash_password(password)
    print(f"The stored password is: {again}")

