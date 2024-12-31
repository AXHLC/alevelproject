from tkinter import Tk, Label, Entry, Button, messagebox, Radiobutton, StringVar
from tkinter import Tk, messagebox
from adminplayerwindows import CoachWindow, PlayerWindow
import myvalidator as mv
import sqlite3
import bcrypt


class loginui:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Login')
        self.parent.geometry('480x300')
        self.parent.resizable(False, False)

        self.label_username = Label(parent, text='Username:')
        self.label_password = Label(parent, text='Password:')
        self.entry_username = Entry(parent)
        self.entry_password = Entry(parent, show='*')
        self.submit_button = Button(parent, text='Submit', command=self.submit)
        self.close_button = Button(parent, text='Close', command=parent.quit)
        self.forgot_password_button = Button(parent, text='Forgot Password', command=self.forgot_password)

        # Place the username widget on the window
        self.label_username.place(x=120, y=50)
        self.entry_username.place(x=190, y=50)

        # Place the password widget on the window
        self.label_password.place(x=120, y=100)
        self.entry_password.place(x=190, y=100)

        # Place the submit and close buttons on the window
        self.close_button.place(x=160, y=210)
        self.submit_button.place(x=300, y=210)
        self.forgot_password_button.place(x=200, y=160)
    
    def submit(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if self.validate(username, password):
            self.verify_user(username, password)
    
    def validate(self, username, password):
        # Implement validation logic here
        validator = mv.TheValidation()
        if not validator.prescheck(username):
            messagebox.showerror('Error', 'Username is required')
            return False
        if not validator.prescheck(password):
            messagebox.showerror('Error', 'Password is required')
            return False
        if not validator.lengthscheck(username, 8, 3):
            messagebox.showerror('Error', 'Username must less than 8 characters long')
            return False
        if not validator.usernamecheck(username):
            messagebox.showerror('Error', 'Username must have at least 3 consecutive letters')
            return False
        if not validator.passcheck(password):
            messagebox.showerror('Error', 'Password must contain at least one digit, one uppercase letter, and one special character')
            return False
        return True

    def verify_user(self, username: str, password: str):
        # Retrieve the stored password from the database
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM Users WHERE username=?", (username,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            return False
        result = result[0]
        if result:
            if password == result or bcrypt.checkpw(password.encode("utf-8"), result.encode("utf-8")):
                self.next_window(username)
                return True
        messagebox.showerror('Login', 'Invalid username or password')
        return False
        
    def forgot_password(self):
        # Implement forgot password logic here
        messagebox.showinfo('Forgot Password', 'Forgot password functionality is not implemented yet.')
        pass 

    def next_window(self, username):
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT role FROM Users WHERE username=?', (username,))
        user = cursor.fetchone()
        conn.close()
        if user:
            role = user[0]
            if role == 'admin':
                messagebox.showinfo('Login', 'Login successful')
                self.parent.destroy()
                CoachWindow()
            elif role == 'player':
                messagebox.showinfo('Login', 'Login successful')
                self.parent.destroy()
                PlayerWindow()
            else:
                messagebox.showerror('Login', 'Invalid role')
        else:
            messagebox.showerror('Login', 'Invalid username or password')

if __name__ == '__main__':
    parent = Tk()
    login_ui = loginui(parent)
    parent.mainloop()