from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed



from flask_login import current_user
from company_blog.models import User



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_email(self, email):
        # Check if not None for that user email!
        if User.query.filter_by(email=email.data).first() is None:
            raise ValidationError('Email address not found!')
        
    # def validate_password(self,field):
    #    if self.user is None:
    #        raise ValidationError() #just to be sure
    #    if not self.user.check_password: #passcheck embedded into user model
    #        raise ValidationError(_("Password incorrect"))

    


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, email):
        # Check if not None for that user email!
        if User.query.filter_by(email=email.data).first():
            raise ValidationError(f'Your email has been registered already!')

    def validate_username(self, username):
        # Check if not None for that username!
        if User.query.filter_by(username=username.data).first():
            raise ValidationError(f'Sorry, that username is taken!')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            email=User.query.filter_by(email=email.data).first()
            if email:
                 raise ValidationError('Your email has been registered already!')

    def validate_username(self, username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Sorry, that username is taken!')



# class UpdateUserForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(),Email()])
#     username = StringField('Username', validators=[DataRequired()])
#     picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
#     submit = SubmitField('Update')

#     def validate_email(self, field):
#         # Check if not None for that user email!
#         if User.query.filter_by(email=field.data).first():
#             raise ValidationError('Your email has been registered already!')

#     def validate_username(self, field):
#         # Check if not None for that username!
#         if User.query.filter_by(username=field.data).first():
#             raise ValidationError('Sorry, that username is taken!')