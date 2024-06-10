import tkinter as tk
from tkinter import Menu


def clickMe():

    print("You have clicked Me")
def changeFont():
    print("Change font pressed")

def basic_2():
# root window
    win = tk.Tk()  # creates a window
    win.title('Basic Menu Demo') # set window title
    menubar = Menu(win) # create a menubar (called menubar here)
    win.config(menu=menubar)

    # create a menu
    accounts_menu = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Accounts", menu=accounts_menu )
# add more
    accounts_menu.add_command(label='clickMe', command=lambda: clickMe())
    accounts_menu.add_command(label='New')
    accounts_menu.add_command(label='Update')
    accounts_menu.add_command(label='Remove')
    accounts_menu.add_command(label='Change Password')

    # create settings menu
    settings_menu = Menu(menubar, tearoff=False)
    settings_menu.add_command(label='Fonts', command=lambda: changeFont())
    menubar.add_cascade(label="Settings", menu=settings_menu )
    settings_menu.add_command(label='Colours')
    settings_menu.add_command(label='Italic')
    settings_menu.add_command(label='screen size')

    win.mainloop()
if __name__=="__main__":
    basic_2()