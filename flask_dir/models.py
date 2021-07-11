from app import cur


class Paper():
    def __init__(self, title: str, text: str, slug: str):
        q = """INSERT INTO paper (title, text, slug) VALUES (?, ?, ?)"""
        cur.execute(q, (title, text, slug))
