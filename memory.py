import sqlite3

class Memory:
    def __init__(self, db_name='memory.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute('''CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY,
                user_input TEXT,
                bot_response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )''')

    def add_conversation(self, user_input, bot_response):
        with self.connection:
            self.connection.execute('INSERT INTO conversations (user_input, bot_response) VALUES (?, ?)',
                                    (user_input, bot_response))

    def fetch_conversations(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM conversations')
        return cursor.fetchall()

    def close(self):
        self.connection.close()