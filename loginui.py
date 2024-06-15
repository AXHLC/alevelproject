import tkinter as tk
from tkinter import Tk, messagebox

class UserTypeUI:
    def __init__(self, master):
        self.master = master
        self.master.title('User Type')
        self.master.geometry('400x100')

        # Create a frame to hold the buttons
        self.frame = tk.Frame(self.master)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.coach_button = tk.Button(self.frame, text='Coach', command=self.open_admin_login)
        self.player_button = tk.Button(self.frame, text='Player', command=self.open_player_login)

        # Place the buttons in the frame
        self.coach_button.grid(row=0, column=0, padx=10)  # padx adds space between the buttons
        self.player_button.grid(row=0, column=1, padx=10)

        self.master.mainloop()

    def open_admin_login(self):
        self.master.destroy()
        root = Tk()
        adminloginui(root)

    def open_player_login(self):
        self.master.destroy()
        root = Tk()
        playerloginui(root)

class loginui:
    def __init__(self, master):
        # Create the main application window
        self.master = master
        self.master.title('Login')
        self.master.geometry('400x250')
        # Create the validator object
        self.create_widgets()
        self.place_widgets()
        # Start the main loop
        self.master.mainloop()

    def create_widgets(self):
        # Create the widget for username
        self.label_username = tk.Label(self.master, text='Username')
        self.entry_username = tk.Entry(self.master)
        # Create the widget for password
        self.label_password = tk.Label(self.master, text='Password')
        self.entry_password = tk.Entry(self.master, show='*')
        # Create the submit button
        self.submit_button = tk.Button(self.master, text='Submit', command=self.validate)
        # Create the close button
        self.close_button = tk.Button(self.master, text='Close', command=self.master.destroy)
        # Create the forgot password button
        self.forgot_password_button = tk.Button(self.master, text='Forgotten password?')

    def place_widgets(self):
        # Place the username widget on the window
        self.label_username.place(x=50, y=50)
        self.entry_username.place(x=150, y=50)
        # Place the password widget on the window
        self.label_password.place(x=50, y=100)
        self.entry_password.place(x=150, y=100)
        # Place the submit and close buttons on the window
        self.close_button.place(x=125, y=210)
        self.submit_button.place(x=250, y=210)
        self.forgot_password_button.place(x=150, y=150)

class adminloginui(loginui):
    def validate(self):
        # Get the username and password from the entry widgets
        username = self.entry_username.get()
        password = self.entry_password.get()
        # Check if the username and password are correct
        if username == 'Coach' and password == 'Coach':
            print('Login successful')
        else:
            # Display an error message if the username or password is incorrect
            messagebox.showerror('Error', 'Incorrect Username or Password')


class playerloginui(loginui):
    def validate(self):
        # Get the username and password from the entry widgets
        username = self.entry_username.get()
        password = self.entry_password.get()
        # Check if the username and password are correct
        if username == 'Player' and password == 'Player':
            print('Login successful')
        else:
            # Display an error message if the username or password is incorrect
            messagebox.showerror('Error', 'Incorrect Username or Password')


if __name__ == '__main__':
    # Test the LoginUI class
    root = Tk()
    UserTypeUI(root)