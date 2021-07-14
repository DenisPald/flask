from .__init__ import cur


def updater():
    news = []
    for i in cur.execute("""SELECT * FROM paper;"""):
        news.append(i)
    return news