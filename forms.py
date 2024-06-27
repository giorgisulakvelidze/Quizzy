from flask_wtf import FlaskForm
from wtforms import (SubmitField,
                     TextAreaField,
                     SelectField,
                     EmailField,
                     StringField,
                     PasswordField,
                     IntegerField,
                     RadioField)
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    file = FileField('Image File', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'], message='მხოლოდ სურათებია დაშვებული!')])
    title = TextAreaField("სათაური", validators=[DataRequired()])
    question = TextAreaField("დასვით კითხვა", validators=[DataRequired()])
    theme = SelectField("აირჩიეთ ქვიზის თემა",
                        choices=["აირჩიეთ თემა", "მათემატიკა", "მეცნიერება", "ისტორია", "სპორტი", "ხელოვნება", "მუსიკა", "გეოგრაფია", "ზოგადი", "სხვა"],
                        validators=[DataRequired()])
    upload = SubmitField("ატვირთვა")



class Editpost_Form(FlaskForm):
        title = StringField('Title', validators=[DataRequired()])
        question = TextAreaField('Question', validators=[DataRequired()])
        theme = StringField('Theme', validators=[DataRequired()])
        file = FileField('File', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'], 'Images only!')])
        save = SubmitField("Save changes")

class RegisterForm(FlaskForm):
    gmail = EmailField("მომხამრებლის mail", validators=[DataRequired(message="მეილის ველი შესავსებია")])
    username = StringField("მომხმარებლის სახელი", validators=[DataRequired(message="სახელის ველი შესავსებია")])
    password = PasswordField("პაროლი", validators=[DataRequired(), Length(8, 28, message="პაროლი ძალიან მოკლეა, უნდა შეიცავდეს 8-დან 28_მდე სიმბოლოს")])
    rep_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), EqualTo("password", message="პაროლები არ ემთხვევა ერთმანეთს")])
    age = IntegerField("მომხმარებლის ასაკი", validators=[DataRequired(message="ასაკის ველი შესავსებია")])
    gender = RadioField("სქესი", validators=[DataRequired()], choices=["Male", "Female"])
    register = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("მომხმარებლის სახელი", validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired(), Length(8, 28)])
    login = SubmitField("Log_In")

class CommentForm(FlaskForm):
    comment = TextAreaField("დაწერეთ პასუხები აქ")
    submit = SubmitField("კომენტარის ატვირთვა")

class UserForm(FlaskForm):
    username = StringField("მომხმარებლის სახელის შეცვლა")
    file = FileField('Image File', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'], message='მხოლოდ სურათებია დაშვებული!')])
    role = SelectField("პროფესია", choices=["მასწავლებელი", "მოსწავლე", "Guest", "სხვა"])
    submit = SubmitField("ცვლილებების შენახვა")
