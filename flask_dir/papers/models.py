from slugify import slugify

from .dataconnect.start_connect import cur


class Paper():
    def __init__(self, title: str, text: str, tags_names: list):
        self.tags_names = tags_names

        slug = slugify(title)
        q = """INSERT INTO paper (title, text, slug) VALUES (?, ?, ?);"""
        cur.execute(q, (title, text, slug))
        self.add_req()

    def add_req(self):
        cur.execute("""SELECT id FROM paper WHERE rowid=last_insert_rowid();""")
        paper_id = cur.fetchall()[0][0]

        q = """SELECT * FROM tag WHERE name = ?;"""
        self.tags_id = []
        for tag_name in self.tags_names:
            flag = False
            for i in cur.execute(q, [tag_name]):
                self.tags_id.append(i[0])
                flag = True
            if not flag:
                self.save_tag(tag_name)

        q = """INSERT INTO paper_tag VALUES (?, ?);"""
        for tag_id in self.tags_id:
            cur.execute(q, [paper_id, tag_id])


    def save_tag(self, tag_name):
        new_tag = Tag(tag_name)
        self.tags_id.append(new_tag.last())

class Tag():
    def __init__(self, name: str):
        slug = slugify(name)
        q = """INSERT INTO tag (name, slug) VALUES (?, ?)"""
        cur.execute(q, (name, slug))


    def last(self):
        cur.execute("""SELECT id FROM tag WHERE rowid=last_insert_rowid();""")
        last_id = cur.fetchall()[0][0]

        return last_id
