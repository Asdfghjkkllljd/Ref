import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, referrer_id=None):
        with self.connection:
            if referrer_id != None:
                return self.cursor.execute("INSERT INTO users (user_id, referrer_id) VALUES (?,?)", (user_id, referrer_id,))
            else:
                return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

    def set_payments(self, user_id, payments):
        with self.connection:
            return self.cursor.execute("UPDATE users SET payments = ? WHERE user_id = ?",(payments, user_id,))

    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE users SET signup = ? WHERE user_id = ?", (signup, user_id,))

    def get_payments(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT payments FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                payments = str(row[0])
            return payments

    def get_referrer(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT referrer_id FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                referrer_id = str(row[0])
            return referrer_id

    #def get_user(self, user_id):
        with self.connection:
            admin = '5333250420'
            return self.cursor.execute(f"UPDATE users SET user_count = user_count + 1 WHERE user_id IS {message.from_user.id}")

    def set_active(selfself, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id,))

    def get_user(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id , active FROM users").fetchall()

    def count_reeferals(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT COUNT(id) as count FROM users WHERE referrer_id = ?", (user_id,)).fetchone()[0]
