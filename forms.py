from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.widgets import TextArea

class InputForm(FlaskForm):
    code = StringField('Code:', widget=TextArea())
    execution = StringField('Execution:', widget=TextArea())
    codesubmit = SubmitField('Submit')



class PostForm(Form):
    title = StringField(u'title', validators=[validators.required()])
    body = StringField(u'Text', widget=TextArea())