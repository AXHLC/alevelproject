import tkinter as tk
from tkinter import Tk, Menu, messagebox
# pandas for chart designs


class Menus:
    def __init__(self, aors):
        # 'aors' stands for admin or student
        # root window has been made a class variable
        self.win = tk.Tk()
        self.win.title(aors)
        self.win.geometry('800x600')
        # creates a window and made it a class variable
        self.win.title(aors)
        # set window title to what is passed in the class whether admin menu or student menu
        self.menubar = Menu(self.win)
        # this creates the bar for the menu
        self.win.config(menu=self.menubar)

        # this is the mainloop for the window
        while True:
            if aors == 'coach':
                self.win.title('Coach')
                self.coachmenu()
                break
            elif aors == 'player':
                self.win.title('Player')
                self.playermenu()
                break
            else:
                print("Invalid input")
                aors = choice()

        # Create 'Settings' tab in coach and player menus
        self.settings_tab = Menu(self.menubar, tearoff=False)

        # Create 'colours' sub tab
        self.colours_submenu = Menu(self.settings_tab, tearoff=0)
        self.colours_submenu.add_command(label='Light Mode', command=lambda: self.lightmode())
        self.colours_submenu.add_command(label='Dark Mode', command=lambda: self.darkmode())
        self.colours_submenu.add_command(label='Contrast Mode', command=lambda: self.contrastmode())

        # Create 'Fonts' sub tab
        self.fonts_submenu = Menu(self.settings_tab, tearoff=0)
        self.fonts_submenu.add_command(label='Arial')
        self.fonts_submenu.add_command(label='Times New Roman')
        self.fonts_submenu.add_command(label='Courier New')

        # Settings tab with 'colours' sub menu
        self.settings_tab.add_cascade(label='colours', menu=self.colours_submenu)
        self.settings_tab.add_cascade(label='Fonts', menu=self.fonts_submenu)
        self.settings_tab.add_command(label='Exit', command=self.win.destroy)
        self.menubar.add_cascade(label="Settings", menu=self.settings_tab)

        self.win.mainloop()


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



    def playermenu(self):

        # creates View tab
        self.view_tab = Menu(self.menubar, tearoff=False)
        self.view_tab.add_command(label='Current Level', command=lambda: self.current())
        self.view_tab.add_command(label='Overall Level', command=lambda: self.overall())
        self.view_tab.add_command(label='My Targets', command=lambda: self.mytargets())
        self.menubar.add_cascade(label="View", menu=self.view_tab)






    def lightmode(self):
        s = "Light Mode"
        print("You have clicked " + s)
    def darkmode(self):
        s = "Dark Mode"
        print("You have clicked " + s)
    def contrastmode(self):
        s = "Contrast Mode"
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
    def current(self):
        s = "Current Level"
        print("You have clicked " + s)
    def overall(self):
        s = "Overall Level"
        print("You have clicked " + s)
    def mytargets(self):
        s = "My Targets"
        print("You have clicked " + s)




if __name__ == '__main__':
    def choice():
        x = input("Enter 'coach' for admin menu or 'player' for student menu: ")
        return x
    z = choice()
    Menus(z)

