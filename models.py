from ext import db, login_menager
from flask_login import UserMixin, current_user
from werkzeug.security import  check_password_hash, generate_password_hash
class Post(db.Model):
    __tablename__ = "Posts"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    question = db.Column(db.String())
    theme = db.Column(db.String())
    file = db.Column(db.String())
    user_id = db.Column(db.Integer())
    def __init(self, title, question, theme, file):
        self.title = title
        self.question = question
        self.theme = theme
        self.file = file
        self.user_id = current_user.id


class User(db.Model, UserMixin):
    __tablename = "Users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    mail = db.Column(db.String())
    password = db.Column(db.String())
    gender = db.Column(db.String())
    age = db.Column(db.Integer())
    role = db.Column(db.String())
    image = db.Column(db.String())
    def __init__(self, name, mail, password, gender, age, role="Guest", image="default.png"):
        self.name = name
        self.mail = mail
        self.password = generate_password_hash(password)
        self.gender = gender
        self.age = age
        self.role = role
        self.image = image
    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_menager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer(), primary_key=True)
    user_comment = db.Column(db.String())
    user_id = db.Column(db.Integer())
    post_id = db.Column(db.Integer())

    def __init__(self, user_comment, post_id, user_id):
        self.user_comment = user_comment
        self.post_id = post_id
        self.user_id = user_id


