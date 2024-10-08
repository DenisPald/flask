from flask import Flask
import sqlite3

from .config import DevConfig as current_config


app = Flask(__name__)
app.config.from_object(current_config)


with sqlite3.connect('data.db') as con:
    cur = con.cursor()
    cur.execute("""PRAGMA foreign_keys = ON;""")

    cur.execute("""CREATE TABLE IF NOT EXISTS paper(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title STRING(32) NOT NULL,
        text TEXT NOT NULL,
        slug STRING(32) NOT NULL UNIQUE
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tag(
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    name STRING(32) NOT NULL UNIQUE,
	    slug STRING(64) NOT NULL UNIQUE
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS paper_tag(
	    id_paper INTEGER NOT NULL,
	    id_tag INTEGER NOT NULL,
	    FOREIGN KEY("id_tag") REFERENCES "tag"("id"),
	    FOREIGN KEY("id_paper") REFERENCES "paper"("id")
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    name STRING(64) NOT NULL UNIQUE,
	    password INTEGER NOT NULL
        );""")

    cur.close()