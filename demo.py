import tkinter as tk
from tkinter import Menu
# pandas for chart designs
class Menus:
    def __init__(self, aors):
        # root window has been made a class variable
        self.win = tk.Tk()
        # creates a window and made it a class variable
        self.win.title(aors)
        # set window title to what is passed in the class whether admin menu or student menu
        self.menubar = Menu(self.win)
        # this creates the bar for the menu
        self.win.config(menu=self.menubar)

        # Create 'Settings' menu
        self.settings_tab = Menu(self.menubar, tearoff=False)
        self.settings_tab.add_command(label='colours', command=lambda: self.colours())
        self.settings_tab.add_command(label='Fonts', command=lambda: self.fonts())
        self.menubar.add_cascade(label="Settings", menu=self.settings_tab)

    def coachmenu(self):
        # creates Accounts tab
        self.accounts_tab = Menu(self.menubar, tearoff=False)
        self.accounts_tab.add_command(label='New', command=lambda: self.new())
        self.accounts_tab.add_command(label='Update', command=lambda: self.update())
        self.accounts_tab.add_command(label='Remove', command=lambda: self.remove())
        self.accounts_tab.add_command(label='Change Password', command=lambda: self.changepass())
        self.menubar.add_cascade(label="Accounts", menu=self.accounts_tab)

        # creates profile management tab
        self.profile_tab = Menu(self.menubar, tearoff=False)
        self.profile_tab.add_command(label='View Profile', command=lambda: self.viewprofile())
        self.profile_tab.add_command(label='Enter Performance', command=lambda: self.enterperf())
        self.profile_tab.add_command(label='Set Targets', command=lambda: self.settargets())
        self.menubar.add_cascade(label="Profiles", menu=self.profile_tab)

        self.win.mainloop()


    def colours(self):
        s = "Colours"
        print("You have clicked " + s)
    def fonts(self):
        s = "Fonts"
        print("You have clicked " + s)
    def new(self):
        s = "New"
        print("You have clicked " + s)
    def update(self):
        s = "Update"
        print("You have clicked " + s)
    def remove(self):
        s = "Remove"
        print("You have clicked " + s)
    def changepass(self):
        s = "Change Password"
        print("You have clicked " + s)
    def viewprofile(self):
        s = "View Profile"
        print("You have clicked " + s)
    def enterperf(self):
        s = "Enter Performance"
        print("You have clicked " + s)

    def settargets(self):
        s = "Set Targets"
        print("You have clicked " + s)



Menus('Coach').coachmenu()