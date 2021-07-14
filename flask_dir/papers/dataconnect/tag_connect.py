from .__init__ import cur

def tag_updater():
    tags = []
    for i in cur.execute("""SELECT * FROM tags;"""):
        tags.append(i)
    return tags