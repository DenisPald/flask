from flask import Blueprint, render_template, request, redirect, url_for

from .dataconnect import paper_updater, tag_updater, TagToPaper, PaperToTag

from .form import NewPaper
from .models import Paper

papers = Blueprint("papers", __name__, template_folder='templates')


@papers.route('/')
def index():
    news = paper_updater()
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
        title = str(request.form.get("title"))
        text = str(request.form.get("text"))
        tags = request.form.get("tags").split()
        Paper(title, text, tags)
        return redirect(url_for('papers.index'))

    return render_template('papers/create_paper.html', form=form)

@papers.route("/tag/<slug>")
def tag(slug):
    tags = tag_updater()
    tag = []
    for cur_tag in tags:
        if cur_tag[2] == slug:
            tag.append(cur_tag)
    if tag:
        paper_for_tag = TagToPaper([tag]).tag_to_paper()
    else:
        paper_for_tag = ''
    return render_template('papers/index.html', news=paper_for_tag)


@papers.route("/<slug>")
def paper(slug):
    news = paper_updater()
    for new in news:
        if new[3] == slug:
            current_new = new

    tags = PaperToTag([current_new]).paper_to_tag()

    return render_template("papers/paper.html", new=current_new, tags=tags)
