from flask_dir.app import app
import flask_dir.view
from flask_dir.papers.blueprint import papers as blueprint_paper


app.register_blueprint(blueprint_paper, url_prefix="/news")

if __name__ == '__main__':
    app.run()
