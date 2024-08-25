import sqlite3
from config import DATABASE

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                user_id INTEGER,
                payment_id TEXT,
                amount INTEGER,
                currency TEXT,
                PRIMARY KEY (user_id, payment_id)
            )
        ''')
        conn.commit()

def save_payment(user_id, payment_id, amount, currency):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO payments (user_id, payment_id, amount, currency)
            VALUES (?, ?, ?, ?)
        ''', (user_id, payment_id, amount, currency))
        conn.commit()

def get_photo_id(user_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT photo_id FROM payments WHERE user_id = ?', (user_id,))
        row = cursor.fetchone()
        return row[0] if row else None
