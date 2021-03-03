from app.auth import auth as auth_blueprints
from app.book import book as book_blueprints
from app.users import users as users_blueprints


def init_app(app):
    app.register_blueprint(auth_blueprints)
    app.register_blueprint(book_blueprints)
    app.register_blueprint(users_blueprints)
