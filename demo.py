import tkinter as tk
from tkinter import Tk, Menu, messagebox

class LoginUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Login')
        self.master.geometry('400x250')

        self.create_widgets()
        self.place_widgets()

        self.master.mainloop()

    def create_widgets(self):
        self.label_username = tk.Label(self.master, text='Username')
        self.entry_username = tk.Entry(self.master)

        self.label_password = tk.Label(self.master, text='Password')
        self.entry_password = tk.Entry(self.master, show='*')

        self.submit_button = tk.Button(self.master, text='Submit', command=self.validate)
        self.close_button = tk.Button(self.master, text='Close', command=self.master.destroy)  # New close button
        self.forgot_password_button = tk.Button(self.master, text='Forgotten password?')

    def place_widgets(self):
        self.label_username.place(x=50, y=50)
        self.entry_username.place(x=150, y=50)

        self.label_password.place(x=50, y=100)
        self.entry_password.place(x=150, y=100)

        self.close_button.place(x=125, y=210)  # Place close button to the left of the submit button
        self.submit_button.place(x=250, y=210)
        self.forgot_password_button.place(x=150, y=150)

    def validate(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == 'admin' and password == 'admin':
            print('Login successful')
        else:
            messagebox.showerror('Error', 'Incorrect Username/Password')

if __name__ == '__main__':
    root = Tk()
    LoginUI(root)