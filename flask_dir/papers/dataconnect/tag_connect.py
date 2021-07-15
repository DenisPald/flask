from .start_connect import cur

def tag_updater():
    tags = []
    for i in cur.execute("""SELECT * FROM tag;"""):
        tags.append(i)
    return tags