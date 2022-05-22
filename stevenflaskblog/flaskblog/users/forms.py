from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators =[DataRequired(), Email()])
    password = PasswordField('Password',
                        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(),
                        EqualTo('password')])
    submit = SubmitField('Sign Up')

    #custom validation for username
    def validate_username(self, username):
        user = User.query.filter_by(username= username.data).first()
        #if there is a user, get first one, if there isnt, it will return None

        if user: #if user is None, it wont hit this condition
            raise ValidationError('That username is taken. Please choose a different one.')

        #custom validation for email
    def validate_email(self, email):
            #if a user with this email exists,
        user = User.query.filter_by(email= email.data).first()

        if user: #if user is None, it wont hit this condition
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):

    email = StringField('Email',
                        validators =[DataRequired(), Email()])
    password = PasswordField('Password',
                        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators =[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',
                        validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    #custom validation for username
    def validate_username(self, username):
        if username.data != current_user.username:

            user = User.query.filter_by(username= username.data).first()
            #if there is a user, get first one, if there isnt, it will return None

            if user: #if user is None, it wont hit this condition
                raise ValidationError('That username is taken. Please choose a different one.')

        #custom validation for email
    def validate_email(self, email):

        if email.data != current_user.email:
            #if a user with this email exists,
            user = User.query.filter_by(email= email.data).first()

            if user: #if user is None, it wont hit this condition
                raise ValidationError('That email is taken. Please choose a different one.')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators =[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
            #if a user with this email exists,
        user = User.query.filter_by(email= email.data).first()

        if user is None: #if user is None, it wont hit this condition
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(),
                        EqualTo('password')])
    submit = SubmitField('Reset Password')
