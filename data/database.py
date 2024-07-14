import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()

cur.execute(f'CREATE TABLE IF NOT EXITS led(pin INTEGER, color TEXT, status INTEGER, datetime TEXT);')
conn.commit()
