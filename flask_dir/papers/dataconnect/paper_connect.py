from .start_connect import cur


def paper_updater():
    news = []
    for i in cur.execute("""SELECT * FROM paper;"""):
        news.append(i)
    return news