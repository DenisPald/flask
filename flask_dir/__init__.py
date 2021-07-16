from .app import app
from .view import *
from .login import *
from .papers.blueprint import papers as blueprint_paper


app.register_blueprint(blueprint_paper, url_prefix="/news")
