from tkinter import Tk, Label, Entry, Button, messagebox, Menu, Toplevel, Frame, Text
from tkinter import ttk
import sqlite3

class BaseWindow:
    def __init__(self, role):
        self.win = Tk()
        self.win.title(f'{role.capitalize()} Dashboard')
        self.win.geometry('1120x700')
        self.win.resizable(False, False)

    def initialize_settings_tab(self):
        # Create frames for Fonts and Colours sections
        fonts_frame = Frame(self.settings_frame)
        fonts_frame.pack(side='left', fill='both', expand=True, padx=20, pady=20)
        colours_frame = Frame(self.settings_frame)
        colours_frame.pack(side='right', fill='both', expand=True, padx=20, pady=20)

        # Create buttons for Fonts section
        Label(fonts_frame, text='Fonts', font=('Helvetica', 16, 'bold')).pack(pady=10)
        Button(fonts_frame, text='Arial', command=self.arial_font).pack(pady=10, anchor='center')
        Button(fonts_frame, text='Times New Roman', command=self.times_font).pack(pady=10, anchor='center')
        Button(fonts_frame, text='Courier New', command=self.courier_font).pack(pady=10, anchor='center')
        Button(fonts_frame, text='Original', command=self.apply_font_original).pack(pady=10, anchor='center')

        # Create buttons for Colours section
        Label(colours_frame, text='Colours', font=('Helvetica', 16, 'bold')).pack(pady=10)
        Button(colours_frame, text='Dark Mode', command=self.darkmode).pack(pady=10, anchor='center')
        Button(colours_frame, text='Light Mode', command=self.lightmode).pack(pady=10, anchor='center')
        Button(colours_frame, text='Contrast Mode', command=self.contrastmode).pack(pady=10, anchor='center')

        # Create Exit button
        Button(self.settings_frame, text='Exit', command=self.win.destroy).pack(pady=10, anchor='center')

    def arial_font(self):
        self.apply_font_arial()

    def apply_font_arial(self):
        self.update_all_widgets_font("Arial 12")

    def times_font(self):
        self.apply_font_times()

    def apply_font_times(self):
        self.update_all_widgets_font("Times 12")

    def courier_font(self):
        self.apply_font_courier()

    def apply_font_courier(self):
        self.update_all_widgets_font("Courier 12")

    def apply_font_original(self):
        self.update_all_widgets_font("Helvetica 10")

    def darkmode(self):
        self.apply_dark_mode()

    def apply_dark_mode(self):
        self.win.config(bg='black')
        self.menubar.config(bg='black', fg='white')
        for menu in self.menubar.winfo_children():
            menu.config(bg='black', fg='white')
        self.update_all_widgets_color('black', 'white')

    def lightmode(self):
        self.apply_light_mode()

    def apply_light_mode(self):
        self.win.config(bg='white')
        self.menubar.config(bg='white', fg='black')
        for menu in self.menubar.winfo_children():
            menu.config(bg='white', fg='black')
        self.update_all_widgets_color('white', 'black')

    def contrastmode(self):
        self.apply_contrast_mode()

    def apply_contrast_mode(self):
        self.win.config(bg='#11189b')
        self.menubar.config(bg='#11189b', fg='white')
        for menu in self.menubar.winfo_children():
            menu.config(bg='#11189b', fg='white')
        self.update_all_widgets_color('#11189b', 'white')

    def update_all_widgets_color(self, bg, fg):
        # Update the background and foreground color for all widgets in the window
        for widget in self.win.winfo_children():
            if isinstance(widget, (Label, Button, Entry, Text, ttk.Notebook)):
                widget.config(bg=bg, fg=fg)
            for child in widget.winfo_children():
                if isinstance(child, (Label, Button, Entry, Text, ttk.Notebook)):
                    child.config(bg=bg, fg=fg)

    def update_all_widgets_font(self, font):
        # Update the font for all widgets in the window
        for widget in self.win.winfo_children():
            if isinstance(widget, (Label, Button, Entry, Text, ttk.Notebook)):
                widget.config(font=font)
            for child in widget.winfo_children():
                if isinstance(child, (Label, Button, Entry, Text, ttk.Notebook)):
                    child.config(font=font)

class CoachWindow(BaseWindow):
    def __init__(self):
        super().__init__('coach')
        self.create_notebook()
        self.win.mainloop()

    def create_notebook(self):
        # Create a notebook widget
        self.notebook = ttk.Notebook(self.win)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Create frames for Accounts, Profiles, and Settings
        self.accounts_frame = ttk.Frame(self.notebook)
        self.profiles_frame = ttk.Frame(self.notebook)
        self.settings_frame = ttk.Frame(self.notebook)

        # Add frames to the notebook as tabs
        self.notebook.add(self.accounts_frame, text='Accounts')
        self.notebook.add(self.profiles_frame, text='Profiles')
        self.notebook.add(self.settings_frame, text='Settings')

        # Add content to the Accounts tab
        self.create_search_player_section(self.accounts_frame)
        Button(self.accounts_frame, text='New', command=self.new).pack(pady=10, anchor='center')
        Button(self.accounts_frame, text='Update', command=self.update).pack(pady=10, anchor='center')
        Button(self.accounts_frame, text='Remove', command=self.remove).pack(pady=10, anchor='center')
        Button(self.accounts_frame, text='Change Password', command=self.changepass).pack(pady=10, anchor='center')

        # Add content to the Profiles tab
        self.create_search_player_section(self.profiles_frame)
        Button(self.profiles_frame, text='View Profile', command=self.viewprofile).pack(pady=10, anchor='center')
        Button(self.profiles_frame, text='Enter Performance', command=self.enterperf).pack(pady=10, anchor='center')
        Button(self.profiles_frame, text='Set Targets', command=self.settargets).pack(pady=10, anchor='center')

        # Initialize settings tab last
        self.initialize_settings_tab()

    def create_search_player_section(self, parent):
        # Define the font with size increased by a factor of 1.5
        base_font_size = 10
        larger_font = ('Helvetica', int(base_font_size * 1.5))

        # Create labels and entry widgets for player search
        Label(parent, text='Search Player by Username:', font=larger_font).pack(pady=10, anchor='center')
        username_entry = Entry(parent, font=larger_font)
        username_entry.pack(pady=10, anchor='center')

        # Bind the Enter key to the search function
        username_entry.bind('<Return>', lambda event: self.search_player_by_username(username_entry))

        # Create a button to search for the player
        search_button = Button(parent, text='Search', font=larger_font, command=lambda: self.search_player_by_username(username_entry))
        search_button.pack(pady=10, anchor='center')

    def search_player_by_username(self, username_entry):
        username = username_entry.get()
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

class PlayerWindow(BaseWindow):
    def __init__(self):
        super().__init__('player')
        self.create_player_tabs()
        self.win.mainloop()

    def create_player_tabs(self):
        # Create a notebook widget
        self.notebook = ttk.Notebook(self.win)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Create frames for View and Settings
        self.view_frame = ttk.Frame(self.notebook)
        self.settings_frame = ttk.Frame(self.notebook)

        # Add frames to the notebook as tabs
        self.notebook.add(self.view_frame, text='View')
        self.notebook.add(self.settings_frame, text='Settings')

        # Add content to the View tab
        Button(self.view_frame, text='Current Level', command=self.current).pack(pady=10, anchor='center')
        Button(self.view_frame, text='Overall Level', command=self.overall).pack(pady=10, anchor='center')
        Button(self.view_frame, text='My Targets', command=self.mytargets).pack(pady=10, anchor='center')

        # Initialize settings tab last
        self.initialize_settings_tab()

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
            window = CoachWindow()
        elif role == 'player':
            PlayerWindow()
        else:
            raise ValueError("Invalid role. Enter 'coach' for admin menu or 'player' for student menu.")
    except ValueError as e:
        print(e)