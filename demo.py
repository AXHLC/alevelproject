import tkinter as tk
from tkinter import Menu

class tabs:
    def __init__(self):
        # root window has been made a class variable
        self.win = tk.Tk()
        # creates a window and made it a class variable
        self.win.title('title')
        # set window title to 'title'
        self.menubar = Menu(self.win)
        # this creates the bar for the menu
        self.win.config(menu=self.menubar)

        self.accounts_menu = Menu(self.menubar, tearoff=False)
        self.accounts_menu.add_command(label='Settings', command=lambda: self.settings())
        self.menubar.add_cascade(label="Accounts", menu=self.accounts_menu)
# pandas for chart design

        self.win.mainloop()

    def settings(self):
        s = "Settings"
        print("You have clicked " + s)

    def file(self):
        s = "File"
        print("You have clicked " + s)

tabs()