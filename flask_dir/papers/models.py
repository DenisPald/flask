from slugify import slugify

import sqlite3


class Paper():
    def __init__(self, title: str, text: str):
        with sqlite3.connect('data.db') as con:
            cur = con.cursor()
            slug = slugify(title)
            q = """INSERT INTO paper (title, text, slug) VALUES (?, ?, ?)"""
            cur.execute(q, (title, text, slug))
