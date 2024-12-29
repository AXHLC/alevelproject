import bcrypt
import os


class passmanager:
    def hash_password(password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return hashed_password
    


if __name__ == '__main__':

    password = input("Enter a password: ")
    hashed_password = passmanager.hash_password(password)
    print(f"The hashed password is: {hashed_password}")

