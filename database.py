import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_users_table()
        self.create_skills_table()
        self.create_results_table()
        self.create_target_table()
        self.insert_default_skills()

    def create_users_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                password BLOB NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('player', 'admin'))
            );
            ''')
            admin_user = ('admin', 'Admin', 'User', 'adminpassword', 'admin')
            cursor.execute('''
            INSERT OR IGNORE INTO Users (username, first_name, last_name, password, role) VALUES (?, ?, ?, ?, ?)
            ''', admin_user)
            self.conn.commit()

    def create_skills_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Skills (
                skill_id INTEGER PRIMARY KEY,
                skill_name TEXT NOT NULL UNIQUE
            );
            ''')
            self.conn.commit()

    def create_results_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Results (
                user_id INTEGER,
                skill_id TEXT,
                score INTEGER NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES Users(user_id),
                FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
            );
            ''')
            self.conn.commit()
    
    def create_target_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Target (
                user_id INTEGER,
                skill_id TEXT,
                target_score INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES Users(user_id),
                FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
                
            );
            ''')
            self.conn.commit()

    def insert_default_skills(self):
        if self.conn:
            cursor = self.conn.cursor()
            skills = [
                ('01', 'shooting'),
                ('02', 'dribbling'),
                ('03', 'passing')
            ]
            cursor.executemany('''
            INSERT OR IGNORE INTO Skills (skill_id, skill_name) VALUES (?, ?)
            ''', skills)
            self.conn.commit()

    #def insert_default_admin(self):
        #if self.conn:
            #cursor = self.conn.cursor()
            #admin_user = ('admin', 'Admin', 'User', 'adminpassword', 'admin')
            #cursor.execute('''
            #INSERT OR IGNORE INTO Users (username, first_name, last_name, password, role) VALUES (?, ?, ?, ?, ?)
            #''', admin_user)
            #self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
    
    def InsertData(self, username, first_name, last_name, password, role):
        conn = sqlite3.connect('basketball_tracker.db')
        # insert data into database table
        conn.execute('''INSERT INTO users  (username, first_name, last_name, password, role) values (?, ?, ?, ?, ?)''',
            (username, first_name, last_name, password, role))
        conn.commit()  
        conn.close()
    
    def UpdateUsername(self, userid, newusername):
        conn = sqlite3.connect('basketball_tracker.db')
        conn.execute('''UPDATE users SET username = ? WHERE user_id = ?''', (newusername, userid))
        print(f"Updated username to {newusername} for user_id {userid}")
        conn.commit()
        conn.close()

    def UpdateFirstName(self, userid, newfn):
        conn = sqlite3.connect('basketball_tracker.db')
        conn.execute('''UPDATE users SET username = ? WHERE user_id = ?''', (newfn, userid))
        print(f"Updated username to {newfn} for user_id {userid}")
        conn.commit()
        conn.close()

    def UpdateLastName(self, userid, newln):
        conn = sqlite3.connect('basketball_tracker.db')
        conn.execute('''UPDATE users SET username = ? WHERE user_id = ?''', (newln, userid))
        print(f"Updated username to {newln} for user_id {userid}")
        conn.commit()
        conn.close()
    
    def UpdatePassword(self, userid, newpass):
        conn = sqlite3.connect('basketball_tracker.db')
        conn.execute('''UPDATE users SET username = ? WHERE user_id = ?''', (newpass, userid))
        print(f"Updated username to {newpass} for user_id {userid}")
        conn.commit()
        conn.close()
    
    def UpdateRole(self, userid, newrole):
        conn = sqlite3.connect('basketball_tracker.db')
        conn.execute('''UPDATE users SET username = ? WHERE user_id = ?''', (newrole, userid))
        print(f"Updated username to {newrole} for user_id {userid}")
        conn.commit()
        conn.close() 

    def DeleteRecord(self, userid):
        conn = sqlite3.connect('basketball_tracker.db')
        conn.execute("DELETE FROM users WHERE  user_id=?",(userid ,) )
        conn.execute("DELETE FROM results WHERE  user_id=?",(userid ,) )
        conn.execute("DELETE FROM target WHERE  user_id=?",(userid ,) )
        conn.commit()
        conn.close()

    def check_user(username, password):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password = ?
        ''', (username, password ))
        user = cursor.fetchone()
        conn.close()
        if user:
            return user[0]
        else:
            return None

# Example usage
if __name__ == "__main__":
    db = Database('basketball_tracker.db')
    #db.InsertData('manjack', 'MAN', 'JACK', 'pass', 'player')
    #db.InsertData('juniroyal', 'Junior', 'royal', 'word', 'player')
    #db.UpdateUsername(6, 'juniroyal')
    db.DeleteRecord(11)
    #db.insert_default_admin()
    db.close()