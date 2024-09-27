import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_users_table()
        self.create_skills_table()
        self.create_results_table()
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
                password TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('player', 'coach'))
            );
            ''')
            self.conn.commit()

    def create_skills_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Skills (
                skill_id TEXT PRIMARY KEY,
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

    def close(self):
        if self.conn:
            self.conn.close()

# Example usage
if __name__ == "__main__":
    db = Database('basketball_tracker.db')
    db.close()