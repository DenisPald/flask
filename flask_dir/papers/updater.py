import sqlite3


def updater():
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        news = []
        for i in cur.execute("""SELECT * FROM paper"""):
            news.append(i)
    return news