from tkinter import Tk, Label, Entry, Button, messagebox, Menu, Toplevel
from tkinter import ttk
import sqlite3

class BaseWindow:
    def __init__(self, role):
        self.win = Tk()
        self.win.title(f'{role.capitalize()} Dashboard')
        self.win.geometry('600x600')
        self.win.resizable(False, False)
        self.menubar = Menu(self.win)
        self.win.config(menu=self.menubar)

    def initialize_settings_tab(self):
        # creates Settings tab
        self.settings_tab = Menu(self.menubar, tearoff=False)
        
        # Create 'Fonts' sub tab
        self.fonts_submenu = Menu(self.settings_tab, tearoff=0)
        self.fonts_submenu.add_command(label='Arial', command=self.arial_font)
        self.fonts_submenu.add_command(label='Times New Roman', command=self.times_font)
        self.fonts_submenu.add_command(label='Courier New', command=self.courier_font)
        self.fonts_submenu.add_command(label='Original', command=self.apply_font_original)

        # Create 'Colours' sub tab
        self.colours_submenu = Menu(self.settings_tab, tearoff=0)
        self.colours_submenu.add_command(label='Dark Mode', command=self.darkmode)
        self.colours_submenu.add_command(label='Light Mode', command=self.lightmode)
        self.colours_submenu.add_command(label='Contrast Mode', command=self.contrastmode)

        # Add submenus to settings tab
        self.settings_tab.add_cascade(label='Colours', menu=self.colours_submenu)
        self.settings_tab.add_cascade(label='Fonts', menu=self.fonts_submenu)
        self.settings_tab.add_command(label='Exit', command=self.win.destroy)
        self.menubar.add_cascade(label="Settings", menu=self.settings_tab)

    def arial_font(self):
        pass

    def times_font(self):
        pass

    def courier_font(self):
        pass

    def apply_font_original(self):
        pass

    def darkmode(self):
        pass

    def lightmode(self):
        pass

    def contrastmode(self):
        pass

class CoachWindow(BaseWindow):
    def __init__(self):
        super().__init__('coach')
        self.create_notebook()
        self.create_search_player_section()
        self.win.mainloop()

    def create_notebook(self):
        # Create a notebook widget
        self.notebook = ttk.Notebook(self.win)
        self.notebook.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Create frames for Accounts and Profiles
        self.accounts_frame = ttk.Frame(self.notebook)
        self.profiles_frame = ttk.Frame(self.notebook)

        # Add frames to the notebook as tabs
        self.notebook.add(self.accounts_frame, text='Accounts')
        self.notebook.add(self.profiles_frame, text='Profiles')

        # Add content to the Accounts tab
        Button(self.accounts_frame, text='New', command=self.new).grid(row=0, column=0, padx=10, pady=10)
        Button(self.accounts_frame, text='Update', command=self.update).grid(row=1, column=0, padx=10, pady=10)
        Button(self.accounts_frame, text='Remove', command=self.remove).grid(row=2, column=0, padx=10, pady=10)
        Button(self.accounts_frame, text='Change Password', command=self.changepass).grid(row=3, column=0, padx=10, pady=10)

        # Add content to the Profiles tab
        Button(self.profiles_frame, text='View Profile', command=self.viewprofile).grid(row=0, column=0, padx=10, pady=10)
        Button(self.profiles_frame, text='Enter Performance', command=self.enterperf).grid(row=1, column=0, padx=10, pady=10)
        Button(self.profiles_frame, text='Set Targets', command=self.settargets).grid(row=2, column=0, padx=10, pady=10)

        # Initialize settings tab last
        self.initialize_settings_tab()

    def create_search_player_section(self):
        # Define the font with size increased by a factor of 1.5
        base_font_size = 10
        larger_font = ('Helvetica', int(base_font_size * 1.5))

        # Create labels and entry widgets for player search
        Label(self.win, text='Search Player by Username:', font=larger_font).grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.username_entry = Entry(self.win, font=larger_font)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Bind the Enter key to the search function
        self.username_entry.bind('<Return>', self.search_player_by_username)

        # Create a button to search for the player
        search_button = Button(self.win, text='Search', font=larger_font, command=self.search_player_by_username)
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    def search_player_by_username(self, event=None):
        username = self.username_entry.get()
        # Query the database for the player with the matching username
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
        player = cursor.fetchone()
        conn.close()

        if player:
            self.open_profile_window(player)
        else:
            messagebox.showerror('Error', 'Player not found')

    def open_profile_window(self, player):
        # Create a new window to display the player's profile
        profile_window = Toplevel(self.win)
        profile_window.title('Profile')
        profile_window.geometry('400x300')

        # Define the font with size increased by a factor of 1.5
        base_font_size = 10
        larger_font = ('Helvetica', int(base_font_size * 1.5))

        # Display the player's details
        Label(profile_window, text=f"Username: {player[1]}", font=larger_font).pack(pady=10)
        Label(profile_window, text=f"First Name: {player[2]}", font=larger_font).pack(pady=10)
        Label(profile_window, text=f"Last Name: {player[3]}", font=larger_font).pack(pady=10)
        Label(profile_window, text=f"Role: {player[5]}", font=larger_font).pack(pady=10)

    def new(self):
        # Create a new window for adding a new player
        new_player_window = Toplevel(self.win)
        new_player_window.title('Add New Player')
        new_player_window.geometry('400x300')

        # Define the font with size increased by a factor of 1.5
        base_font_size = 10
        larger_font = ('Helvetica', int(base_font_size * 1.5))

        # Create labels and entry widgets for player details
        Label(new_player_window, text='Username:', font=larger_font).grid(row=0, column=0, padx=10, pady=10)
        username_entry = Entry(new_player_window, font=larger_font)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(new_player_window, text='First Name:', font=larger_font).grid(row=1, column=0, padx=10, pady=10)
        first_name_entry = Entry(new_player_window, font=larger_font)
        first_name_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(new_player_window, text='Last Name:', font=larger_font).grid(row=2, column=0, padx=10, pady=10)
        last_name_entry = Entry(new_player_window, font=larger_font)
        last_name_entry.grid(row=2, column=1, padx=10, pady=10)

        Label(new_player_window, text='Password:', font=larger_font).grid(row=3, column=0, padx=10, pady=10)
        password_entry = Entry(new_player_window, show='*', font=larger_font)
        password_entry.grid(row=3, column=1, padx=10, pady=10)

        Label(new_player_window, text='Role:', font=larger_font).grid(row=4, column=0, padx=10, pady=10)
        role_entry = Entry(new_player_window, font=larger_font)
        role_entry.grid(row=4, column=1, padx=10, pady=10)

        # Create a button to save the new player
        save_button = Button(new_player_window, text='Save', font=larger_font, command=lambda: self.save_new_player(username_entry.get(), first_name_entry.get(), last_name_entry.get(), password_entry.get(), role_entry.get(), new_player_window))
        save_button.grid(row=5, column=0, columnspan=2, pady=20)

    def save_new_player(self, username, first_name, last_name, password, role, window):
        # Insert the new player into the database
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Users (username, first_name, last_name, password, role)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, first_name, last_name, password, role))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'New player added successfully')
        window.destroy()

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

if __name__ == '__main__':
    coach_window = CoachWindow()