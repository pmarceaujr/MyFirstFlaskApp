import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import *

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', f'{config_type}.py')
    app.config.from_pyfile(configuration)
    db.init_app(app)
    bootstrap.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app



