from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms import DataRequired

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField()

    