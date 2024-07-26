import sqlite3
import os

DB_NAME = 'cat_facts.db'

def get_db_path():
    return os.path.join(os.path.dirname(__file__), DB_NAME)

