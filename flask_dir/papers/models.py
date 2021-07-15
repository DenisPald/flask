from slugify import slugify

import sqlite3


class Paper():
    def __init__(self, title: str, text: str, tags_names: list):
        with sqlite3.connect('data.db') as con:
            self.cur = con.cursor()
            self.tags_names = tags_names

            self.slug = slugify(title)
            q = """INSERT INTO paper (title, text, slug) VALUES (?, ?, ?);"""
            self.cur.execute(q, (title, text, self.slug))
            self.add_req()

    def add_req(self):
        q = """SELECT * FROM paper WHERE slug = ?;"""
        papers_id = []
        for i in self.cur.execute(q, [self.slug]):
            papers_id.append(i[0])
        q = """SELECT * FROM tag WHERE name = ?;"""
        tags_id = []
        for tag_name in self.tags_names:
            for i in self.cur.execute(q, [tag_name]):
                tags_id.append(i[0])

        q = """INSERT INTO paper_tag VALUES (?, ?);"""
        for paper_id in papers_id:
            for tag_id in tags_id:
                self.cur.execute(q, [paper_id, tag_id])

class Tag():
    def __init__(self, title: str):
        slug = slugify(title)
        q = """INSERT INTO tag (title, slug) VALUES (?, ?)"""
        self.cur.execute(q, (title, slug))
