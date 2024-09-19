import tkinter as tk
from tkinter import Tk, Menu, messagebox
# pandas for chart designs

class BaseWindow:
    def __init__(self, role):
        self.win = tk.Tk()

        # Set the window title based on the role
        if role == 'coach':
            self.win.title("Coach Window")
        elif role == 'player':
            self.win.title("Player Window")
        else:
            raise ValueError("Invalid role. Enter 'coach' for admin menu or 'player' for student menu.")

        # Set the default window size
        self.win.geometry("800x700")

        # Make the window unresizable
        self.win.resizable(False, False)

        # Initialize the menubar
        self.menubar = Menu(self.win)
        self.win.config(menu=self.menubar)

        # Ensure the window appears on the screen
        self.win.deiconify()


    def initialize_settings_tab(self):
        # creates Settings tab
        self.settings_tab = Menu(self.menubar, tearoff=False)
        
        # Create 'Fonts' sub tab
        self.fonts_submenu = Menu(self.settings_tab, tearoff=0)
        self.fonts_submenu.add_command(label='Arial')
        self.fonts_submenu.add_command(label='Times New Roman')
        self.fonts_submenu.add_command(label='Courier New')

        # Create 'Colours' sub tab
        self.colours_submenu = Menu(self.settings_tab, tearoff=0)
        self.colours_submenu.add_command(label='Dark Mode', command=self.darkmode)
        #self.colours_submenu.add_command(label='Light Mode', command=self.lightmode)
        #self.colours_submenu.add_command(label='contrast Mode', command=self.contrastmode)

        # Add submenus to settings tab
        self.settings_tab.add_cascade(label='Colours', menu=self.colours_submenu)
        self.settings_tab.add_cascade(label='Fonts', menu=self.fonts_submenu)
        self.settings_tab.add_command(label='Exit', command=self.win.destroy)
        self.menubar.add_cascade(label="Settings", menu=self.settings_tab)

    def apply_dark_mode(self):
        # Change the background and foreground colors for dark mode
        self.win.config(bg='black')
        self.menubar.config(bg='black', fg='white')
        for menu in self.menubar.winfo_children():
            menu.config(bg='black', fg='white')

    def darkmode(self):
        self.apply_dark_mode()
        s = "Dark Mode"
        print("You have clicked " + s)

class CoachWindow(BaseWindow):
    def __init__(self):
        super().__init__('coach')
        self.create_coach_window()
        self.win.mainloop()

    def create_coach_window(self):
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

        # Initialize settings tab last
        self.initialize_settings_tab()

class PlayerWindow(BaseWindow):
    def __init__(self):
        super().__init__('player')
        self.create_player_window()
        self.win.mainloop()

    def create_player_window(self):

        # creates View tab
        self.view_tab = Menu(self.menubar, tearoff=False)
        self.view_tab.add_command(label='Current Level', command=lambda: self.current())
        self.view_tab.add_command(label='Overall Level', command=lambda: self.overall())
        self.view_tab.add_command(label='My Targets', command=lambda: self.mytargets())
        self.menubar.add_cascade(label="View", menu=self.view_tab)

        # Initialize settings tab last
        self.initialize_settings_tab()




    def lightmode(self):
        s = "Light Mode"
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
    role = input("Enter 'coach' for admin menu or 'player' for student menu: ").strip().lower()
    try:
        if role == 'coach':
            CoachWindow()
        elif role == 'player':
            PlayerWindow()
        else:
            raise ValueError("Invalid role. Enter 'coach' for admin menu or 'player' for student menu.")
    except ValueError as e:
        print(e)

