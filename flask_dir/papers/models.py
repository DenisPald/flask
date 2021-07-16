from slugify import slugify

import sqlite3

class Paper():
    def __init__(self, title: str, text: str, tags_names: list):
        with sqlite3.connect('data.db') as con:
            self.cur = con.cursor()
            self.tags_names = tags_names

            slug = slugify(title)
            q = """INSERT INTO paper (title, text, slug) VALUES (?, ?, ?);"""
            self.cur.execute(q, (title, text, slug))
            self.add_req()

    def add_req(self):
        self.cur.execute("""SELECT id FROM paper WHERE rowid=last_insert_rowid();""")
        paper_id = self.cur.fetchall()[0][0]

        q = """SELECT * FROM tag WHERE name = ?;"""
        self.tags_id = []
        for tag_name in self.tags_names:
            flag = False
            for i in self.cur.execute(q, [tag_name]):
                self.tags_id.append(i[0])
                flag = True
            if not flag:
                self.tags_id.append(self.save_tag(tag_name))

        q = """INSERT INTO paper_tag VALUES (?, ?);"""
        for tag_id in self.tags_id:
            self.cur.execute(q, [paper_id, tag_id])


    def save_tag(self, tag_name):
        new_tag = Tag(tag_name, self.cur)
        return new_tag.last()

class Tag():
    def __init__(self, name: str, cur):
        self.cur = cur
        slug = slugify(name)
        q = """INSERT INTO tag (name, slug) VALUES (?, ?)"""
        self.cur.execute(q, (name, slug))


    def last(self):
        self.cur.execute("""SELECT id FROM tag WHERE rowid=last_insert_rowid();""")
        last_id = self.cur.fetchall()[0][0]

        return last_id