from tkinter import Tk, Label, Entry, Button, messagebox, Menu, Toplevel, Frame
from tkinter import ttk
from tkinter import *
from datetime import date
import sqlite3
from barchart import plot_week_summary
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import barchart

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

    def apply_font_arial(self):
        # Change the font to Arial
        self.win.option_add("*Font", "Arial 12")
        self.update_all_widgets_font("Arial 12")
    
    def arial_font(self):
        self.apply_font_arial()

    def apply_font_times(self):
        # Change the font to Times New Roman
        self.win.option_add("*Font", "Times 12")
        self.update_all_widgets_font("Times 12")

    def times_font(self):
        self.apply_font_times()

    def apply_font_courier(self):
        # Change the font to Courier New
        self.win.option_add("*Font", "Courier 12")
        self.update_all_widgets_font("Courier 12")
    
    def courier_font(self):
        self.apply_font_courier()

    def apply_font_original(self):
        # Change the font to the original font
        self.win.option_add("*Font", "TkDefaultFont")
        self.update_all_widgets_font("TkDefaultFont")

    def original_font(self):
        self.apply_font_original()

    def apply_dark_mode(self):
        # Change the background and foreground colors for dark mode
        self.win.config(bg='black')
        self.menubar.config(bg='black', fg='white')
        for menu in self.menubar.winfo_children():
            menu.config(bg='black', fg='white')

    def darkmode(self):
        self.apply_dark_mode()

    def apply_light_mode(self):
        # Change the background and foreground colors for light mode
        self.win.config(bg='white')
        self.menubar.config(bg='white', fg='black')
        for menu in self.menubar.winfo_children():
            menu.config(bg='white', fg='black')

    def lightmode(self):
        self.apply_light_mode()

    def apply_contrast_mode(self):
        # Change the background and foreground colors for high contrast mode
        self.win.config(bg='#11189b')
        self.menubar.config(bg='#11189b', fg='white')
        for menu in self.menubar.winfo_children():
            menu.config(bg='#11189b', fg='white')
    
    def contrastmode(self):
        self.apply_contrast_mode()

    def update_all_widgets_font(self, font):
        # Update the font for all widgets in the window
        for widget in self.win.winfo_children():
            widget.config(font=font)
            for child in widget.winfo_children():
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
        s = "Update" # This is a comment
        print("You have clicked " + s)

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

###############################################################################################################

    def delete_selected_player(self):
        selected_index = self.player_listbox.curselection()
        if not selected_index:
            messagebox.showwarning('No Selection', 'Please select a player to delete.')
            return

        selected_player = self.players[selected_index[0]]
        user_id = selected_player[0]

        # Delete the player from the database
        db = Database('basketball_tracker.db')
        db.delete_record(user_id)
        db.close()

        messagebox.showinfo('Success', 'Player deleted successfully.')
        self.remove_window.destroy()

#########################################################################################################

    def changepass(self):
        s = "Change Password"
        print("You have clicked " + s)

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
        for skill_name, target in targets.items():
            skill_id = self.get_skill_id(skill_name)
            # Insert or update the target in the database
            cursor.execute('''
                INSERT OR REPLACE INTO Target (user_id, skill_id, target_score)
                VALUES (?, ?, ?)
            ''', (user_id, skill_id, target))
        conn.commit()
        conn.close()
        return True  # Proceed to next player
    
    def get_skill_id(self, skill_name):
        # Assuming you have self.skill_ids defined as in previous methods
        return self.skill_ids.get(skill_name.lower())









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