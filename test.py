import tkinter as tk
from tkinter import messagebox
import sqlite3
import myvalidator as mv

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        # Create the validator object
        self.validator = mv.TheValidation()

        self.create_widgets()
        self.place_widgets()

        # Start the main loop
        self.master.mainloop()

    def create_widgets(self):
        # Create the widget for username
        self.label_username = tk.Label(self.master, text='Username')
        self.entry_username = tk.Entry(self.master)

        # Create the widget for password
        self.label_password = tk.Label(self.master, text='Password')
        self.entry_password = tk.Entry(self.master, show='*')

        # Create the submit button
        self.submit_button = tk.Button(self.master, text='Submit', command=self.validate)

        # Create the close button
        self.close_button = tk.Button(self.master, text='Close', command=self.master.destroy)

        # Create the forgot password button
        self.forgot_password_button = tk.Button(self.master, text='Forgot Password', command=self.forgot_password)

    def place_widgets(self):
        self.label_username.grid(row=0, column=0)
        self.entry_username.grid(row=0, column=1)
        self.label_password.grid(row=1, column=0)
        self.entry_password.grid(row=1, column=1)
        self.submit_button.grid(row=2, column=0, columnspan=2)
        self.close_button.grid(row=3, column=0, columnspan=2)
        self.forgot_password_button.grid(row=4, column=0, columnspan=2)

    def validate(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not self.validator.usernamecheck(username):
            messagebox.showerror("Error", "Invalid username format")
            return

        if not self.validator.passcheck(password):
            messagebox.showerror("Error", "Invalid password format")
            return

        conn = sqlite3.connect('basketball_tracker.db')
        cursor = conn.cursor()

        # Check in Users table
        cursor.execute("SELECT password, role FROM Users WHERE username=?", (username,))
        user = cursor.fetchone()

        if user:
            stored_password, role = user
            if stored_password == password:
                if role == 'player':
                    self.open_player_menu()
                elif role == 'coach':
                    self.open_coach_menu()
            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            self.open_registration_window(username)

        conn.close()

    def open_coach_menu(self):
        messagebox.showinfo("Login Successful", "Welcome Coach!")
        # Implement coach menu logic here

    def open_player_menu(self):
        messagebox.showinfo("Login Successful", "Welcome Player!")
        # Implement player menu logic here

    def open_registration_window(self, username):
        registration_window = tk.Toplevel(self.master)
        registration_window.title("Register")

        tk.Label(registration_window, text="First Name").grid(row=0, column=0)
        tk.Label(registration_window, text="Last Name").grid(row=1, column=0)
        tk.Label(registration_window, text="Password").grid(row=2, column=0)
        tk.Label(registration_window, text="Role").grid(row=3, column=0)

        first_name_entry = tk.Entry(registration_window)
        last_name_entry = tk.Entry(registration_window)
        password_entry = tk.Entry(registration_window, show="*")

        first_name_entry.grid(row=0, column=1)
        last_name_entry.grid(row=1, column=1)
        password_entry.grid(row=2, column=1)

        role_var = tk.StringVar(value="player")
        tk.Radiobutton(registration_window, text="Player", variable=role_var, value="player").grid(row=3, column=1)
        tk.Radiobutton(registration_window, text="Coach", variable=role_var, value="coach").grid(row=3, column=2)

        tk.Button(registration_window, text="Register", command=lambda: self.register_user(first_name_entry.get(), last_name_entry.get(), password_entry.get(), role_var.get(), registration_window)).grid(row=4, column=0, columnspan=3)

    def register_user(self, first_name, last_name, password, role, window):
        if not self.validator.passcheck(password):
            messagebox.showerror("Error", "Invalid password format")
            return

        try:
            username = self.validator.generate_username(first_name, last_name)
            messagebox.showinfo("Generated Username", f"Your username is: {username}")

            conn = sqlite3.connect('basketball_tracker.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Users (username, first_name, last_name, password, role) VALUES (?, ?, ?, ?, ?)", (username, first_name, last_name, password, role))
            conn.commit()
            conn.close()
            window.destroy()
            messagebox.showinfo("Registration Successful", "You can now log in with your new account")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def forgot_password(self):
        # Implement forgot password logic here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()