# Python
import sqlite3

class Database:
    def __init__(self, db_name='tracker.db'):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def create_player_table(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS Players(
                    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL);
                ''')
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"An error occurred: {e}")

    def create_coach_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Coach (
                coach_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL);
            ''')
            self.conn.commit()

    def create_skill_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Skills (
                skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                level INTEGER NOT NULL);
            ''')
            self.conn.commit()
    
    def create_result_table(self):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Results (
                result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                level INTEGER NOT NULL,
                player_id INTEGER,
                skill_id INTEGER,
                FOREIGN KEY (player_id) REFERENCES Players(player_id),
                FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
            );
            ''')
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()

# Usage
if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_coach_table()
    db.create_player_table()
    db.create_skill_table()
    db.create_result_table()
    db.close()