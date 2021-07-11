from flask import Flask
import sqlite3

from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)


with sqlite3.connect('data.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS paper(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title STRING(128) NOT NULL,
        text TEXT NOT NULL,
        slug STRING(128) NOT NULL UNIQUE
        )""")
