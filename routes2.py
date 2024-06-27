import os
from werkzeug.utils import secure_filename
from flask import render_template, redirect
from forms import RegisterForm, LoginForm, UserForm
from flask_login import login_user, logout_user, login_required, current_user
from ext import app
from models import Post, db, User




@app.route("/users")
@login_required
def render_users():
    registered_users = User.query.all()
    return render_template("profiles.html", registered_users=registered_users)


@app.route("/delete_user/<int:user_id>")
def delete__user(user_id):
    if current_user.role == "admin":
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return redirect("/users")
    else:
        return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def render_register():
    form1 = RegisterForm()
    if form1.validate_on_submit():
        if User.query.filter(User.name == form1.username.data).first():
            return redirect("/register")
        else:
            new_user = User(name=form1.username.data, mail=form1.gmail.data, password=form1.password.data,
                            gender=form1.gender.data, age=form1.age.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect("/")

    return render_template("register.html", form=form1)


@app.route("/log_in", methods=["GET", "POST"])
def render_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.name == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    return render_template("log_in.html", form=form)


@app.route("/log_out")
def log_out():
    logout_user()
    return redirect("/")

@app.route("/profile/<int:user_id>", methods=["GET", "POST"])
def render_user_profile(user_id):
    user = User.query.get(user_id)
    myposts = Post.query.filter(Post.user_id == current_user.id).all()
    form = UserForm(username=user.name,
                    file="default.png",
                    about=None,
                    role=user.role)
    if form.validate_on_submit():
        user.name = form.username.data
        user.role = form.role.data
        if form.file.data:
            file = form.file.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.root_path, 'static', filename))
            user.image = filename
        db.session.commit()
    return render_template("profile.html", user=user, myposts=myposts, form=form)

@app.route("/see_profile/<int:user_id>")
@login_required
def see_user_profile(user_id):
    user = User.query.get(user_id)
    posts = Post.query.filter(Post.user_id == user_id).all()
    return render_template("user_profile.html", user=user, posts=posts)
