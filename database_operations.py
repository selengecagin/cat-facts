import sqlite3
import os

DB_NAME = 'cat_facts.db'

def get_db_path():
    return os.path.join(os.path.dirname(__file__), DB_NAME)

def create_table():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cat_facts
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
     fact TEXT NOT NULL,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

def insert_fact(fact):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cat_facts (fact) VALUES (?)", (fact,))
    conn.commit()
    conn.close()

def get_all_facts():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cat_facts")
    facts = cursor.fetchall()
    conn.close()
    return facts