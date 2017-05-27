from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from config import config

csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from main import main_blueprint

    csrf.exempt(main_blueprint)

    app.register_blueprint(main_blueprint)

    return app
