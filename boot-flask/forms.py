from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FileField, TelField, TextAreaField
from wtforms.validators import DataRequired
from validators import NumberRange, LengthRange, Email
from email_validator import validate_email




class MyForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Please enter your Email"})
    Password = PasswordField('Password', validators=[DataRequired(), LengthRange(min=8, max=20, message="Field must be between 8  and 20 characters")], render_kw={"placeholder": "Please enter your password"})
    #age = DateField('age', validators=[DataRequired()])
    #profilepic = FileField('profilepic', validators=[DataRequired()])
    #phone = TelField('phone', validators=[DataRequired()])
    #message = TextAreaField('message', validators=[DataRequired()])
    submit = SubmitField('Login')
