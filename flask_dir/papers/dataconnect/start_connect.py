import sqlite3

with sqlite3.connect('data.db') as con:
    cur = con.cursor()