from ext import app
from models import db, Post, User, Comment

with app.app_context():
    db.create_all()
    admin_user = User("admin", "admin@mail.com", "admin_password", "Male", 31, "admin", "admin_image.png")
    post1 = Post(
        title="math riddle #1",
        question="This is the first post.",
        theme="მათემატიკა",
        file="riddle1.jpg",
        user_id=1
    )

    post2 = Post(
        title="მეცნიერება",
        question="This is the second post.",
        theme="მეცნიერება",
        file="riddle3.jpg",
        user_id=2
    )

    post3 = Post(
        title="ხელოვნება",
        question="This is the third post.",
        theme="ხელოვნება",
        file="riddle5.jpg",
        user_id=1
    )

    post4 = Post(
        title="სპორტი",
        question="This is the fourth post.",
        theme="სპორტი",
        file="riddle4.jpg",
        user_id=3
    )

    post5 = Post(
        title="მუსიკა",
        question="This is the fifth post.",
        theme="მუსიკა",
        file="riddle2.jpg",
        user_id=2
    )
    user1 = User(
        name="Alice",
        mail="alice@mail.com",
        password="alice_password",
        gender="Female",
        age=28,
        role="Guest",
        image="default.png"
    )

    user2 = User(
        name="Bob",
        mail="bob@mail.com",
        password="bob_password",
        gender="Male",
        age=32,
        role="Guest",
        image="user2.jpg"
    )

    user3 = User(
        name="Eve",
        mail="eve@mail.com",
        password="eve_password",
        gender="Female",
        age=25,
        role="Guest",
        image="user3.jpg"
    )

    user4 = User(
        name="Charlie",
        mail="charlie@mail.com",
        password="charlie_password",
        gender="Male",
        age=30,
        role="Guest",
        image="user4.png"
    )

    db.session.add_all([user1, user2, user3, user4])
    db.session.add_all([post1, post2, post3, post4, post5])
    db.session.commit()
    db.session.add(admin_user)
    db.session.commit()
