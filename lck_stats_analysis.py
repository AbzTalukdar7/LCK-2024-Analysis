import sqlite3

conn = sqlite3.connect('LCK_2024_Season.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS players(
    player_id INTEGER PRIMARY KEY AUTOUNCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
)
''')

for row in rows:
    print(row)
    
conn.close()