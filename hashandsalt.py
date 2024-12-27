import hashlib
import os
import base64

class passmanager:
    @staticmethod
    def hash_password(password: str, salt: bytes = None):
        if salt is None:
            salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + hashed_password

    @staticmethod
    def verify_password(stored_password: bytes, input_password: str):
        salt = stored_password[:16]
        stored_hash = stored_password[16:]
        input_hash = hashlib.pbkdf2_hmac('sha256', input_password.encode('utf-8'), salt, 100000)
        return stored_hash == input_hash

if __name__ == '__main__':
    password = input("Enter a password: ")
    stored_password = passmanager.hash_password(password)
    print(f"The stored password is: {stored_password}")