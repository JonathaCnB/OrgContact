from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.security import generate_password_hash
from wtforms.fields import PasswordField

from . import db
from .models import Book, Profile, User


class UserView(ModelView):
    column_editable_list = ("name", "email", "books")
    form_edit_rules = {"name", "email", "books"}
    column_searchable_list = ["name", "email"]
    edit_modal = True
    form_extra_fields = {"password": PasswordField("Password")}
    column_exclude_list = ("password",)
    column_list = ["name", "email", "books"]

    inline_models = [Book]

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(form.password.data)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))


def init_app(admin):
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Profile, db.session))
