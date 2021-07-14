import sqlite3

with sqlite3.connect('data.db', check_same_thread=False) as con:
    cur = con.cursor()