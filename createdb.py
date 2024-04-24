import sqlite3 as sql

conn = sql.connect('database.db')
print("Database opened successfully")

conn.execute("CREATE TABLE reservations (name TEXT, checkin, checkout, roomtype TEXT)")
print("table created successfully")

conn.close()