import hashlib
import os
import base64

class passmanager:
    @staticmethod
    def hash_password(password):
        salt = b'abcdefgh'
        passw = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        hashed_password = passw + salt
        return base64.b64encode(hashed_password).decode('utf-8')

if __name__ == '__main__':
    password = input("Enter a password: ")
    stored_password = passmanager.hash_password(password)
    print(f"The stored password is: {stored_password}")