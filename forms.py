from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed

from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError

class PostForm(FlaskForm):
  title = StringField('Title',validators=[DataRequired()])
  content = TextAreaField('content',validators=[DataRequired()])
  submit = SubmitField("Post")

class AnswerForm(FlaskForm):
  content = TextAreaField('content',validators=[DataRequired()])
  name = StringField('name',validators=[DataRequired()])
  submit = SubmitField("Post")