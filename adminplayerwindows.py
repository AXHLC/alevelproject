from tkinter import Tk, Label, Entry, Button, messagebox, Menu, Toplevel, Frame
import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import date
from datetime import datetime, timedelta
import sqlite3
from barchart import plot_week_summary
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import barchart
from database import Database
from hashandsalt import passmanager
import bcrypt

matplotlib.use('TkAgg')


class BaseWindow:
    def __init__(self, role):
        self.win = Tk()

        # Set the window title based on the role
        if role == 'coach':
            self.win.title("Coach Window")
        elif role == 'player':
            self.win.title("Player Window")
        else:
            raise ValueError("Invalid role. Enter 'coach' for admin menu or 'player' for student menu.")

        # Set the default window size with golden ratio 1.6
        self.win.geometry("640x400")

        # Make the window unresizable
        self.win.resizable(False, False)

        # Initialize the menubar
        self.menubar = Menu(self.win)
        self.win.config(menu=self.menubar)

        # Ensure the window appears on the screen
        self.win.deiconify()

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
        print("Arial font button clicked")
        self.win.option_add("*Font", "Arial 12")
        self.update_all_widgets_font("Arial 12")

    def times_font(self):
        print("Times font button clicked")
        self.win.option_add("*Font", "Times 12")
        self.update_all_widgets_font("Times 12")

    def courier_font(self):
        print("Courier font button clicked")
        self.win.option_add("*Font", "Courier 12")
        self.update_all_widgets_font("Courier 12")

    def apply_font_original(self):
        print("Original font button clicked")
        self.win.option_add("*Font", "Helvetica 12")
        self.update_all_widgets_font("Helvetica 12")

    def update_all_widgets_font(self, font):
        print(f"Updating all widgets to font: {font}")
        self._update_widget_font(self.win, font)
        self.win.update_idletasks()

    def _update_widget_font(self, widget, font):
        if 'font' in widget.keys():
            widget.configure(font=font)
        for child in widget.winfo_children():
            self._update_widget_font(child, font)

    def update_all_widgets_color(self, bg_color, fg_color):
        def configure_widget(widget):
            try:
                widget.configure(bg=bg_color, fg=fg_color)
            except TclError:
                pass
            for child in widget.winfo_children():
                configure_widget(child)

        # Update the main window
        self.win.configure(bg=bg_color)
        configure_widget(self.win)

        # Update ttk styles
        style = ttk.Style()
        style.configure('TFrame', background=bg_color, foreground=fg_color)
        style.configure('TLabel', background=bg_color, foreground=fg_color)
        style.configure('TButton', background=bg_color, foreground=fg_color)
        style.configure('TNotebook', background=bg_color, foreground=fg_color)
        style.configure('TNotebook.Tab', background=bg_color, foreground=fg_color)
        style.configure('TCombobox', background=bg_color, foreground=fg_color)
        style.configure('TEntry', background=bg_color, foreground=fg_color)
        style.configure('TMenubutton', background=bg_color, foreground=fg_color)
        style.configure('TCheckbutton', background=bg_color, foreground=fg_color)
        style.configure('TRadiobutton', background=bg_color, foreground=fg_color)


    def darkmode(self):
        self.update_all_widgets_color(bg_color='black', fg_color='white')

    def lightmode(self):
        self.update_all_widgets_color(bg_color='white', fg_color='black')

    def contrastmode(self):
        self.update_all_widgets_color(bg_color='yellow', fg_color='blue')

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
        Button(self.profiles_frame, text='Enter Performance', command=self.enter_performance).pack(pady=10, anchor='center')
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
        profile_window.title('Profile and Performance')
        profile_window.geometry('800x600')  # Adjust size to accommodate the chart

        # Define the font with size increased by a factor of 1.5
        base_font_size = 10
        larger_font = ('Helvetica', int(base_font_size * 1.5))

        # Display the player's details
        Label(profile_window, text=f"Username: {player[1]}", font=larger_font).pack(pady=10)
        Label(profile_window, text=f"First Name: {player[2]}", font=larger_font).pack(pady=10)
        Label(profile_window, text=f"Last Name: {player[3]}", font=larger_font).pack(pady=10)
        Label(profile_window, text=f"Role: {player[5]}", font=larger_font).pack(pady=10)

        # Integrate bar chart using barchart.py
        username = player[1]  # Extract the player's username
        fig = barchart.plot_week_summary(username)  # Generate the chart for the player

        if fig is None:
            # No data available for the player, show a message
            Label(profile_window, text=f"No data available for {username} in the past week.", font=larger_font).pack(pady=20)
        else:
            # Embed the plot in the profile window
            canvas = FigureCanvasTkAgg(fig, master=profile_window)
            canvas.draw()
            canvas.get_tk_widget().pack()

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
        hashed_password = passmanager.hash_password(password)
        # Insert the new player into the database
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Users (username, first_name, last_name, password, role)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, first_name, last_name, hashed_password, role))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', 'New player added successfully')
        window.destroy()

    def update(self):
        # Create a new window to display the list of players
        self.update_window = Toplevel(self.win)
        self.update_window.title("Update Player")
        self.update_window.geometry("400x300")
        self.update_window.resizable(False, False)

        # Retrieve all player usernames
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username FROM Users WHERE role='player'")
        self.players = cursor.fetchall()
        conn.close()

        if not self.players:
            messagebox.showinfo('No Players', 'There are no players to update.')
            self.update_window.destroy()
            return

        # Create a listbox to display the players
        self.player_listbox = Listbox(self.update_window)
        self.player_listbox.pack(fill='both', expand=True, padx=10, pady=10)

        for user_id, username in self.players:
            self.player_listbox.insert(END, f"{username} (ID: {user_id})")

        # Add a button to select the player for updating
        Button(self.update_window, text="Select", command=self.select_player_for_update).pack(pady=10)

    def select_player_for_update(self):
        selected_index = self.player_listbox.curselection()
        if not selected_index:
            messagebox.showwarning('No Selection', 'Please select a player to update.')
            return

        selected_player = self.players[selected_index[0]]
        self.user_id_to_update = selected_player[0]

        # Retrieve the selected player's details
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username, first_name, last_name FROM Users WHERE user_id=?", (self.user_id_to_update,))
        user_details = cursor.fetchone()
        conn.close()

        if user_details:
            username, first_name, last_name = user_details

            # Create a new window to display the player's details for editing
            self.edit_window = Toplevel(self.win)
            self.edit_window.title("Edit Player Details")
            self.edit_window.geometry("400x300")
            self.edit_window.resizable(False, False)

            Label(self.edit_window, text="Username:").pack(pady=5)
            self.entry_username = Entry(self.edit_window)
            self.entry_username.pack(pady=5)
            self.entry_username.insert(0, username)

            Label(self.edit_window, text="First Name:").pack(pady=5)
            self.entry_first_name = Entry(self.edit_window)
            self.entry_first_name.pack(pady=5)
            self.entry_first_name.insert(0, first_name)

            Label(self.edit_window, text="Last Name:").pack(pady=5)
            self.entry_last_name = Entry(self.edit_window)
            self.entry_last_name.pack(pady=5)
            self.entry_last_name.insert(0, last_name)

            Button(self.edit_window, text="Save", command=self.save_updated_player_details).pack(pady=10)
    
    def save_updated_player_details(self):
        username = self.entry_username.get()
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()

        if not username or not first_name or not last_name:
            messagebox.showerror('Error', 'All fields are required.')
            return


        # Update the player's details in the database
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Users
            SET username=?, first_name=?, last_name=?
            WHERE user_id=?
        ''', (username, first_name, last_name, self.user_id_to_update))
        conn.commit()
        conn.close()

        messagebox.showinfo('Success', 'Player details updated successfully.')
        self.edit_window.destroy()
        self.update_window.destroy()


    def remove(self):
        # Create a new window to display the list of players
        self.remove_window = Toplevel(self.win)
        self.remove_window.title("Remove Player")
        self.remove_window.geometry("400x300")
        self.remove_window.resizable(False, False)

        # Retrieve all player usernames
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username FROM Users WHERE role='player'")
        self.players = cursor.fetchall()
        conn.close()

        if not self.players:
            messagebox.showinfo('No Players', 'There are no players to remove.')
            self.remove_window.destroy()
            return

        # Create a listbox to display the players
        self.player_listbox = Listbox(self.remove_window)
        self.player_listbox.pack(fill='both', expand=True, padx=10, pady=10)

        for user_id, username in self.players:
            self.player_listbox.insert(END, f"{username} (ID: {user_id})")

        # Add a button to delete the selected player
        Button(self.remove_window, text="Delete", command=self.delete_selected_player).pack(pady=10)

    def delete_selected_player(self):
        selected_index = self.player_listbox.curselection()
        if not selected_index:
            messagebox.showwarning('No Selection', 'Please select a player to delete.')
            return

        selected_player = self.players[selected_index[0]]
        self.user_id_to_delete = selected_player[0]

        # Show verification dialog
        self.show_confirmation_dialog()
    
    def show_confirmation_dialog(self):
        # Create a new window for confirmation
        self.confirmation_window = Toplevel(self.win)
        self.confirmation_window.title("Confirm Deletion")
        self.confirmation_window.geometry("300x150")
        self.confirmation_window.resizable(False, False)

        Label(self.confirmation_window, text="Are you sure you want to delete this player?").pack(pady=10)

        Button(self.confirmation_window, text="Yes", command=self.confirm_deletion).pack(side=LEFT, padx=20, pady=10)
        Button(self.confirmation_window, text="No", command=self.confirmation_window.destroy).pack(side=RIGHT, padx=20, pady=10)

    def confirm_deletion(self):
        self.confirmation_window.destroy()
        self.show_verification_dialog()

    def show_verification_dialog(self):
        # Create a new window for verification
        self.verification_window = Toplevel(self.win)
        self.verification_window.title("Verify Coach")
        self.verification_window.geometry("300x200")
        self.verification_window.resizable(False, False)

        Label(self.verification_window, text="Enter Coach Username:").pack(pady=5)
        self.coach_username_entry = Entry(self.verification_window)
        self.coach_username_entry.pack(pady=5)

        Label(self.verification_window, text="Enter Coach Password:").pack(pady=5)
        self.coach_password_entry = Entry(self.verification_window, show='*')
        self.coach_password_entry.pack(pady=5)

        Button(self.verification_window, text="Verify", command=self.verify_coach_credentials).pack(pady=10)

    def verify_coach_credentials(self):
        username = self.coach_username_entry.get()
        password = self.coach_password_entry.get()


        # Verify the credentials against the database
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM Users WHERE username=? AND role='admin'", (username,))
        coach = cursor.fetchone()
        conn.close()

        if coach:
            stored_hashed_password = coach[0]
            print(f"Stored Hashed Password: {stored_hashed_password}")

            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                self.verification_window.destroy()
                self.delete_player_after_verification()
            else:
                messagebox.showerror('Error', 'Invalid credentials. Please try again.')
        else:
            messagebox.showerror('Error', 'Invalid credentials. Please try again.')

    def delete_player_after_verification(self):
        # Delete the player from the database
        db = Database('basketball_tracker.db')
        db.DeleteRecord(self.user_id_to_delete)
        db.close()

        messagebox.showinfo('Success', 'Player deleted successfully.')
        self.remove_window.destroy()

    def changepass(self):
        self.create_change_password_ui()

    def create_change_password_ui(self):
        self.change_password_window = Toplevel(self.win)
        self.change_password_window.title("Change Password")

        Label(self.change_password_window, text="Select Player:").pack(pady=5)
        self.player_selection = ttk.Combobox(self.change_password_window, values=self.get_player_list())
        self.player_selection.pack(pady=5)

        Label(self.change_password_window, text="Current Password:").pack(pady=5)
        self.current_password_entry = Entry(self.change_password_window, show='*')
        self.current_password_entry.pack(pady=5)

        Label(self.change_password_window, text="New Password:").pack(pady=5)
        self.new_password_entry = Entry(self.change_password_window, show='*')
        self.new_password_entry.pack(pady=5)

        Label(self.change_password_window, text="Confirm New Password:").pack(pady=5)
        self.confirm_new_password_entry = Entry(self.change_password_window, show='*')
        self.confirm_new_password_entry.pack(pady=5)

        Button(self.change_password_window, text="Change Password", command=self.verify_current_password).pack(pady=10)

    def get_player_list(self):
        # Fetch the list of players from the database
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM Users WHERE role='player'")
        players = [row[0] for row in cursor.fetchall()]
        conn.close()
        return players

    def verify_current_password(self):
        username = self.player_selection.get()
        current_password = self.current_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_new_password = self.confirm_new_password_entry.get()

        if new_password != confirm_new_password:
            messagebox.showerror('Error', 'New passwords do not match.')
            return

        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM Users WHERE username=? AND role='player'", (username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            stored_hashed_password = result[0]
            if bcrypt.checkpw(current_password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                self.open_admin_verification_window(username, new_password)
            else:
                messagebox.showerror('Error', 'Current password is incorrect.')
        else:
            messagebox.showerror('Error', 'Player not found.')

    def open_admin_verification_window(self, username, new_password):
        self.admin_verification_window = Toplevel(self.win)
        self.admin_verification_window.title("Admin Verification")

        Label(self.admin_verification_window, text="Admin Username:").pack(pady=5)
        self.admin_username_entry = Entry(self.admin_verification_window)
        self.admin_username_entry.pack(pady=5)

        Label(self.admin_verification_window, text="Admin Password:").pack(pady=5)
        self.admin_password_entry = Entry(self.admin_verification_window, show='*')
        self.admin_password_entry.pack(pady=5)

        self.username_to_update = username
        self.new_password_to_update = new_password

        Button(self.admin_verification_window, text="Verify", command=self.verify_admin_credentials_for_password_change).pack(pady=10)

    def verify_admin_credentials_for_password_change(self):
        admin_username = self.admin_username_entry.get()
        admin_password = self.admin_password_entry.get()

        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM Users WHERE username=? AND role='admin'", (admin_username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            stored_hashed_password = result[0]
            if bcrypt.checkpw(admin_password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                self.update_password(self.username_to_update, self.new_password_to_update)
                self.admin_verification_window.destroy()
            else:
                messagebox.showerror('Error', 'Invalid admin credentials.')
        else:
            messagebox.showerror('Error', 'Admin not found.')

    def update_password(self, username, new_password):
        hashed_password = passmanager.hash_password(new_password)
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE Users SET password=? WHERE username=? AND role='player'", (hashed_password, username))
        conn.commit()
        conn.close()

        messagebox.showinfo('Success', 'Password updated successfully.')
        self.change_password_window.destroy()

    def viewprofile(self):
        # Create a new child window
        self.profile_window = Toplevel(self.win)
        self.profile_window.title("Player Performance")
        self.profile_window.geometry("850x600")
        self.profile_window.resizable(False, False)

        # Retrieve all player usernames
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM Users WHERE role='player'")
        self.players = [row[0] for row in cursor.fetchall()]
        conn.close()

        if not self.players:
            messagebox.showinfo('No Players', 'There are no players to display.')
            self.profile_window.destroy()
            return

        self.player_index = 0  # Initialize the current player index

        # Display the bar chart for the first player
        self.show_player_chart()

    def show_player_chart(self):
        # Clear the profile window
        for widget in self.profile_window.winfo_children():
            widget.destroy()

        # Get the current player's username
        username = self.players[self.player_index]

        # Generate the bar chart figure
        fig = plot_week_summary(username)

        if fig:
            # Create a frame for the canvas
            canvas_frame = Frame(self.profile_window)
            canvas_frame.pack(fill='both', expand=True)

            # Embed the figure in the Tkinter canvas
            canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
        else:
            Label(self.profile_window, text=f"No data available for {username} in the past week.").pack()

        # Add navigation buttons at the bottom
        btn_frame = Frame(self.profile_window)
        btn_frame.pack(fill='x', pady=10)

        if self.player_index < len(self.players) - 1:
            Button(btn_frame, text='Next', command=self.next_player).pack(side='right', padx=5)
        else:
            Button(btn_frame, text='Done', command=self.close_profile_window).pack(side='right', padx=5)
            
    def next_player(self):
        self.player_index += 1
        self.show_player_chart()

    def close_profile_window(self):
        # Remove the profile_frame from the window
        self.profile_window.destroy()

    def enter_performance(self):
        # Retrieve all player user_ids and usernames from the database
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username FROM Users WHERE role='player'")
        self.players = cursor.fetchall()  # List of tuples: (user_id, username)
        
        # Retrieve skill_ids for shooting, dribbling, and passing
        cursor.execute("SELECT skill_id, skill_name FROM Skills WHERE skill_name IN ('shooting', 'dribbling', 'passing')")
        skills = cursor.fetchall()  # List of tuples: (skill_id, skill_name)
        conn.close()
        
        # Create a dictionary to map skill_name to skill_id
        self.skill_ids = {skill_name: skill_id for skill_id, skill_name in skills}

        self.player_index = 0  # Initialize index to keep track of current player

        # Initialize performance entry window
        self.perf_window = Toplevel(self.win)
        self.perf_window.title('Enter Performance')
        self.perf_window.geometry('400x300')

        self.performance_data = []  # List to store performance data

        self.display_performance_entry()

    def display_performance_entry(self):
        # Clear the window
        for widget in self.perf_window.winfo_children():
            widget.destroy()

        # Get current player's user_id and username
        user_id, username = self.players[self.player_index]
        
        # Display player's username
        Label(self.perf_window, text=f"Enter Performance for {username}", font=('Helvetica', 14, 'bold')).pack(pady=10)

        # Create entry fields for scores
        Label(self.perf_window, text='Shooting (out of 10):').pack()
        self.shooting_entry = Entry(self.perf_window)
        self.shooting_entry.pack()

        Label(self.perf_window, text='Dribbling (out of 10):').pack()
        self.dribbling_entry = Entry(self.perf_window)
        self.dribbling_entry.pack()

        Label(self.perf_window, text='Passing (out of 10):').pack()
        self.passing_entry = Entry(self.perf_window)
        self.passing_entry.pack()

        # Determine if this is the last player
        if self.player_index < len(self.players) - 1:
            # Show NEXT button
            Button(self.perf_window, text='NEXT', command=self.save_and_next).pack(pady=20)
        else:
            # Show DONE button
            Button(self.perf_window, text='DONE', command=self.save_and_finish).pack(pady=20)

    def save_and_next(self):
        if self.save_performance_data():
            # Move to next player
            self.player_index += 1
            self.display_performance_entry()

    def save_and_finish(self):
        if self.save_performance_data():
            # All data collected; save to database
            self.save_all_performance_data()
            self.perf_window.destroy()
            messagebox.showinfo('Success', 'Performance data saved successfully.')

    def save_performance_data(self):
        # Get entered scores
        shooting = self.shooting_entry.get()
        dribbling = self.dribbling_entry.get()
        passing = self.passing_entry.get()

        # Validate inputs
        if not (shooting.isdigit() and dribbling.isdigit() and passing.isdigit()):
            messagebox.showerror('Error', 'Please enter valid numeric scores between 0 and 10.')
            return False
        if not (0 <= int(shooting) <= 10 and 0 <= int(dribbling) <= 10 and 0 <= int(passing) <= 10):
            messagebox.showerror('Error', 'Scores must be between 0 and 10.')
            return False

        # Get current player's user_id
        user_id, username = self.players[self.player_index]

        # Append data to performance_data list for each skill
        self.performance_data.append({
            'user_id': user_id,
            'skill_id': self.skill_ids['shooting'],
            'score': int(shooting),
            'date': date.today().strftime('%Y-%m-%d')
        })
        self.performance_data.append({
            'user_id': user_id,
            'skill_id': self.skill_ids['dribbling'],
            'score': int(dribbling),
            'date': date.today().strftime('%Y-%m-%d')
        })
        self.performance_data.append({
            'user_id': user_id,
            'skill_id': self.skill_ids['passing'],
            'score': int(passing),
            'date': date.today().strftime('%Y-%m-%d')
        })

        return True

    def save_all_performance_data(self):
        # Save all performance data to the database
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO Results (user_id, skill_id, score, date)
            VALUES (:user_id, :skill_id, :score, :date)
        ''', self.performance_data)
        conn.commit()
        conn.close()


    def settargets(self):
        # Retrieve all player user_ids and usernames
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username FROM Users WHERE role='player'")
        self.players = cursor.fetchall()  # List of tuples: (user_id, username)

        # Retrieve skill IDs for skills
        cursor.execute("SELECT skill_id, LOWER(skill_name) FROM Skills")
        skills = cursor.fetchall()  # List of tuples: (skill_id, skill_name)
        conn.close()

        # Create a dictionary to map skill_name to skill_id
        self.skill_ids = {skill_name: skill_id for skill_id, skill_name in skills}

        if not self.players:
            messagebox.showinfo('No Players', 'There are no players to set targets for.')
            return

        self.player_index = 0  # Initialize index to keep track of current player

        # Initialize target entry window
        self.targets_window = Toplevel(self.win)
        self.targets_window.title('Set Targets')
        self.targets_window.geometry('300x250')
        self.targets_window.resizable(False, False)

        # Start setting targets for the first player
        self.display_target_entry()


    def display_target_entry(self):
        # Clear the window if there are existing widgets
        for widget in self.targets_window.winfo_children():
            widget.destroy()

        # Get the current player's information
        user_id, username = self.players[self.player_index]

        # Display the player's name
        Label(self.targets_window, text=f"Set targets for {username}", font=('Arial', 12)).pack(pady=10)

        # Create input fields for each skill (targets out of 10)
        self.target_entries = {}
        for skill_name in ['Shooting', 'Dribbling', 'Passing']:
            frame = Frame(self.targets_window)
            frame.pack(pady=5)
            Label(frame, text=f"{skill_name} Target (0-10):").pack(side='left')
            entry = Entry(frame, width=5)
            entry.pack(side='left')
            self.target_entries[skill_name.lower()] = entry

        # Add 'Save and Next' button
        Button(self.targets_window, text='Save and Next', command=self.save_and_next_target).pack(pady=15)

    def save_and_next_target(self):
        if self.save_target_data():
            # Move to next player
            self.player_index += 1
            if self.player_index < len(self.players):
                self.display_target_entry()
            else:
                # All players have been processed
                self.targets_window.destroy()
                messagebox.showinfo('Success', 'Targets set successfully.')
    
    def save_target_data(self):
        user_id, username = self.players[self.player_index]
        targets = {}
        for skill_name, entry in self.target_entries.items():
            try:
                target = float(entry.get())
                if 0 <= target <= 10:
                    targets[skill_name] = target
                else:
                    messagebox.showerror('Invalid Input', f'Please enter a target between 0 and 10 for {skill_name.capitalize()}.')
                    return False  # Do not proceed to next player
            except ValueError:
                messagebox.showerror('Invalid Input', f'Please enter a valid number for {skill_name.capitalize()}.')
                return False  # Do not proceed to next player

        # Save the target data to the database
        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()
        date_entered = datetime.now().date()
        for skill_name, target in targets.items():
            skill_id = self.get_skill_id(skill_name)
            # Insert or update the target in the database
            cursor.execute('''
                INSERT OR REPLACE INTO Target (user_id, skill_id, target_score, date_entered)
                VALUES (?, ?, ?, ?)
            ''', (user_id, skill_id, target, date_entered))
        conn.commit()
        conn.close()
        return True  # Proceed to next player
    
    def get_skill_id(self, skill_name):
        # Assuming you have self.skill_ids defined as in previous methods
        return self.skill_ids.get(skill_name.lower())

class PlayerWindow(BaseWindow):
    def __init__(self, username):
        self.username = username
        super().__init__('player')
        self.profile_window = Frame(self.win)  # Initialize profile_window
        self.profile_window.pack(fill='both', expand=True)
        self.create_player_tabs()
        self.win.mainloop()

    def create_player_tabs(self):

        for widget in self.profile_window.winfo_children():
            widget.destroy()
            
        # Create a notebook widget
        self.notebook = ttk.Notebook(self.profile_window)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Create frames for View and Settings
        self.view_frame = ttk.Frame(self.notebook)
        self.settings_frame = ttk.Frame(self.notebook)

        # Add frames to the notebook as tabs
        self.notebook.add(self.view_frame, text='View')
        self.notebook.add(self.settings_frame, text='Settings')

        # Add content to the View tab
        Button(self.view_frame, text='This Week', command=self.this_week).pack(pady=10, anchor='center')
        Button(self.view_frame, text='My Targets', command=self.mytargets).pack(pady=10, anchor='center')

        # Initialize settings tab last
        self.initialize_settings_tab()

    def this_week(self):
        # Assuming `self.username` holds the currently logged-in player's username
        username = self.username

        
        for widget in self.profile_window.winfo_children():
            widget.destroy()

        # Create a new frame for the bar chart
        bar_chart_frame = Frame(self.profile_window)
        bar_chart_frame.pack(fill='both', expand=True)

        # Generate the bar chart figure for the current player
        fig = plot_week_summary(username)

        if fig:
            # Create a frame for the canvas
            canvas_frame = Frame(bar_chart_frame)
            canvas_frame.pack(fill='both', expand=True)

            # Embed the figure in the Tkinter canvas
            canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)

            # Add an Exit button to go back to the main player menu
            exit_button_frame = Frame(bar_chart_frame)
            exit_button_frame.pack(fill='x', pady=10)
            Button(exit_button_frame, text='Exit', command=self.create_player_tabs).pack(anchor='center')
        else:
            Label(bar_chart_frame, text=f"No data available for {username} in the past week.").pack()


    def mytargets(self):
        username = self.username  # Assuming self.username is defined
        targets = self.get_player_targets_for_current_week(username)

        if not targets:
            messagebox.showinfo('No Targets', 'There are no targets set for this week.')
            return
        
        for widget in self.profile_window.winfo_children():
            widget.destroy()

        target_frame = Frame(self.profile_window)
        target_frame.pack(fill='both', expand=True)

        Label(target_frame, text=f"Targets for {username}").pack(pady=5)
        Label(target_frame, text=f"Shooting: {targets.get('shooting', 'N/A')}").pack()
        Label(target_frame, text=f"Dribbling: {targets.get('dribbling', 'N/A')}").pack()
        Label(target_frame, text=f"Passing: {targets.get('passing', 'N/A')}").pack()

        Button(target_frame, text='Exit', command=self.create_player_tabs).pack(pady=10)

    def get_player_targets_for_current_week(self, username):
        conn = sqlite3.connect("basketball_tracker.db")
        cursor = conn.cursor()

        today = datetime.now()
        # Calculate the most recent Monday
        week_start = today - timedelta(days=today.weekday())
        week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0)
        # Calculate the upcoming Sunday
        week_end = week_start + timedelta(days=6, hours=23, minutes=59, seconds=59)


        query = """
            SELECT s.skill_name, t.target_score
            FROM Target t
            JOIN Users u ON t.user_id = u.user_id
            JOIN Skills s ON t.skill_id = s.skill_id
            WHERE u.username = ?
            AND t.date_entered >= ?
            AND t.date_entered < ?
        """
        cursor.execute(query, (username, week_start, week_end,))
        rows = cursor.fetchall()

        conn.close()

        targets = {}
        for row in rows:
            skill_name, target_score = row
            targets[skill_name.lower()] = target_score

        return targets





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
