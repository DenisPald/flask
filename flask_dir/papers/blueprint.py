from flask import Blueprint, render_template, request

import sqlite3

papers = Blueprint("papers", __name__, template_folder='templates')

with sqlite3.connect('data.db') as con:
    cur = con.cursor()
    news = []
    for i in cur.execute("""SELECT * FROM paper"""):
        news.append(i)


@papers.route('/')
def index():
    search = request.args.get('search')
    if search:
        search = search.lower().strip()
        searched_news = []
        for i in news:
            if (search in i[1].lower().strip()) or (search
                                                    in i[2].lower().strip()):
                searched_news.append(i)
        return render_template("papers/index.html", news=searched_news)

    return render_template("papers/index.html", news=news)


@papers.route("<slug>")
def paper(slug):
    for new in news:
        if new[3] == slug:
            current_new = new

    return render_template("papers/new.html", new=current_new)
