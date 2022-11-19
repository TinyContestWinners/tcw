from flask import Flask
from tcw import BASEDIR
from tcw.config import Development, Production
from tcw.database import init_db


def create_app(name='', config=None):
    if config is None:
        config = Development

    app = Flask(name, root_path=BASEDIR)
    # app = Flask(name)
    configure_app(app, config)
    load_filters(app)
    load_blueprints(app)
    load_views()
    return app


def configure_app(app, config):
    init_db(config.SQLALCHEMY_DATABASE_URI, config.DEBUG)
    app.config.from_object(config)


def load_blueprints(app):
    from tcw.apps.contest.views import bp as contest

    app.register_blueprint(contest)


def load_views():
    from tcw.apps.contest import views


def load_filters(app):
    from tcw.filters import md_to_html
    app.jinja_env.filters['markdown'] = md_to_html
