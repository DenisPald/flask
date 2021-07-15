from flask import Blueprint, render_template, request, redirect, url_for

from .dataconnect.paper_connect import updater
from flask_dir.papers.dataconnect.connect import tag_to_paper, paper_to_tag

from .form import NewPaper
from .models import Paper

papers = Blueprint("papers", __name__, template_folder='templates')


@papers.route('/')
def index():
    news = updater()
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


@papers.route("/create", methods=["GET", "POST"])
def create():
    form = NewPaper()
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        try:
            Paper(title, text)
        except Exception:
            return 'Что-то пошло не так, повторите попытку позже'
        return redirect(url_for('papers.index'))

    return render_template('papers/create_paper.html', form=form)


@papers.route("/<slug>")
def paper(slug):
    news = updater()
    for new in news:
        if new[3] == slug:
            current_new = new

    tags = paper_to_tag(current_new)

    return render_template("papers/paper.html", new=current_new, tags=tags)
