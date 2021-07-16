from slugify import slugify
from flask_login import UserMixin

from .dataconnect.start_connect import cur
from flask_dir.login import login_manager


class Paper():
    def __init__(self, title: str, text: str, tags_names: list):
        self.tags_names = tags_names

        self.slug = slugify(title)
        q = """INSERT INTO paper (title, text, slug) VALUES (?, ?, ?);"""
        cur.execute(q, (title, text, self.slug))
        self.add_req()

    def add_req(self):
        q = """SELECT * FROM paper WHERE slug = ?;"""
        papers_id = []
        for i in cur.execute(q, [self.slug]):
            papers_id.append(i[0])

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
        for paper_id in papers_id:
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

class User(UserMixin):
    def __init__(self, name, password):
        q = """INSERT INTO users (name, password) VALUES (?, ?)"""
        cur.execute(q, (name, password))


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)