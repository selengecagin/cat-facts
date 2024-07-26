import sqlite3
import os

# Determine the path for the database file
db_path = os.path.join(os.path.dirname(__file__), 'cat_facts.db')

# Create a database connection
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS cat_facts
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 fact TEXT NOT NULL,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
''')

# Save changes and close the connection
conn.commit()
conn.close()

print(f"Database and table successfully created: {db_path}")
