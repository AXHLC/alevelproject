from tkinter import Tk, Label, Entry, Button, messagebox, Radiobutton, StringVar
from tkinter import Tk, messagebox
from adminplayerwindows import CoachWindow, PlayerWindow
import myvalidator as mv


class loginui:
    def __init__(self, master):
        self.master = master
        self.master.title('Login')
        self.master.geometry('400x300')

        self.label_username = Label(master, text='Username:')
        self.label_password = Label(master, text='Password:')
        self.entry_username = Entry(master)
        self.entry_password = Entry(master, show='*')
        self.submit_button = Button(master, text='Submit', command=self.next_window)
        self.close_button = Button(master, text='Close', command=master.quit)
        self.forgot_password_button = Button(master, text='Forgot Password', command=self.forgot_password)

        # Place the username widget on the window
        self.label_username.place(x=50, y=50)
        self.entry_username.place(x=150, y=50)

        # Place the password widget on the window
        self.label_password.place(x=50, y=100)
        self.entry_password.place(x=150, y=100)

        # Place the submit and close buttons on the window
        self.close_button.place(x=125, y=210)
        self.submit_button.place(x=250, y=210)
        self.forgot_password_button.place(x=150, y=160)
    
    def forgot_password(self):
        # Implement forgot password logic here
        messagebox.showinfo('Forgot Password', 'Forgot password functionality is not implemented yet.')
    def next_window(self):
        # Implement new window logic here
        messagebox.showinfo('New Window', 'New window functionality is not implemented yet.')   


if __name__ == '__main__':
    root = Tk()
    login_ui = loginui(root)
    root.mainloop()