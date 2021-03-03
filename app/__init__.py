from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
login_manager.login_view = "login.html"
login_manager.login_message_category = "danger"


def creat_app():
    app = Flask(__name__, static_folder="public")
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    from . import admin as administrator

    admin = Admin(app, name="OrgContact", template_mode="bootstrap3")
    administrator.init_app(admin)

    from app import routes

    routes.init_app(app)

    return app
