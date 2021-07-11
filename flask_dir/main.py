from app import app
import view
from papers.blueprint import papers as blueprint_paper


app.register_blueprint(blueprint_paper, url_prefix="/news")

if __name__ == '__main__':
    app.run()
