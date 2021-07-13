from slugify import slugify

from app import cur


class Paper():
    def __init__(self, title: str, text: str):
        slug = slugify(title)
        q = """INSERT INTO paper (title, text, slug) VALUES (?, ?, ?)"""
        cur.execute(q, (title, text, slug))
