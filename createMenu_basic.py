import tkinter as tk
from tkinter import Menu


def clickMe():
    s = "Clicked me "
    print("You have clicked " + s)
def basic():
# root window
    win = tk.Tk()  # creates a window
    win.title('Basic Menu Demo') # set window title
    menubar = Menu(win) # create a menubar (called menubar here)
    win.config(menu=menubar)

    # create a menu
    accounts_menu = Menu(menubar, tearoff=False)
    # if you set tearoff to True, you will get dashed line, ... try it
    # add a menu item to the menu
    # when the menu is clicked, it calls a function called clikMe()
    accounts_menu.add_command(label='clickMe', command=lambda: clickMe())
    # add the Accounts  menu to the menubar
    menubar.add_cascade(label="Accounts", menu=accounts_menu )

    win.mainloop()
if __name__=="__main__":
    basic()