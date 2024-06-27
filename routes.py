from flask import render_template, redirect,url_for
from forms import PostForm, CommentForm, Editpost_Form
from flask_login import current_user
from ext import app
from models import Post, db, Comment, User


@app.route("/", methods=["GET", "POST"])
def render_homepage():
    uploaded_posts = db.session.query(Post, User).join(User, Post.user_id == User.id).all()
    return render_template("homepage.html", uploaded_posts=uploaded_posts)


@app.route("/add_comments/<int:post_id>", methods=["GET", "POST"])
def render_comment(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(
            user_comment=form.comment.data,
            post_id=post.id,
            user_id=current_user.id
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('render_comment', post_id=post.id))
    return render_template("add_comments.html", form=form, post=post, comments=comments)

@app.route('/delete_comment/<int:comment_id>', methods=["GET", "POST"])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('render_comment', post_id=comment.post_id))


@app.route("/filter/<post_theme>")
def render_filtered(post_theme):
    uploaded_posts = db.session.query(Post, User).join(User, Post.user_id == User.id).filter(Post.theme == post_theme).all()
    return render_template("homepage.html", uploaded_posts=uploaded_posts)


@app.route("/about")
def render_about():
    return render_template("about.html")


@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_quiz(post_id):
    post = Post.query.get(post_id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.question = form.question.data
        post.theme = form.theme.data

        db.session.commit()
        return redirect("/")

    return render_template("post_edit.html", form=form, post=post, current_file=post.file)

@app.route("/upload", methods=["GET", "POST"])
def render_upload():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data,
                        question=form.question.data,
                        theme=form.theme.data,
                        user_id=current_user.id,
                        file="noimage.png")
        if form.file.data:
            file = form.file.data
            file.save(f"{app.root_path}\static\{file.filename}")
            new_post.file = file.filename
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")
    return render_template("upload_post.html", form=form)

@app.route("/delete_post/<int:post_id>")
def delete_post(post_id):
    post = Post.query.get(post_id)
    if current_user.role == "admin" or current_user.id == post.user_id:
        db.session.delete(post)
        db.session.commit()
        return redirect("/")
    else:
        return redirect("/")