from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, RadioField, FileField, IntegerField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileRequired, FileAllowed

# reference lines 7-19, lecture12
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(message="username is required")])
	password = PasswordField('Password', validators=[DataRequired(message="password is required")])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')
	
class SignupForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(message="username is required")])
	email = StringField('Email', validators=[DataRequired(message="email is required")])
	password = PasswordField('Password', validators=[DataRequired(message="password is required")])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(message="password is required")])
	accept_rules = BooleanField('I accept the site rules', validators=[DataRequired(message="you need accept the rules")])
	submit = SubmitField('Register')
	
class ProfileForm(FlaskForm):
	dob = DateField ('Date of Birth (YYYY-MM-DD)', format='%Y-%m-%d', validators = [DataRequired(message="date of birth is required")])
	gender = RadioField('Gender', choices = [('0','Male'),('1','Female'),('2','Secret')], validators=[DataRequired(message="gender is required")])
	cv = FileField('Your CV', validators = [FileAllowed(['pdf'], 'Only PDF files please')])
	photo = FileField('Your avatar', validators = [FileAllowed(['png', 'jpg', 'JPG', 'PNG', 'bmp'], 'Only png, jpg or bmp files please')])
	submit = SubmitField('Update Profile')
	
		
class PostForm(FlaskForm):
	title = StringField('Post title', validators=[DataRequired(message="please enter post title")])
	area = RadioField('Post Area', choices=[('0','Teaching Building 4'),('1','Teaching Building 3'),('2','Play Ground'),('3','Library')],validators=[DataRequired()])
	body = StringField('Post Body', validators=[DataRequired(message="please enter post body")])
	photo = FileField('Photo', validators = [FileAllowed(['png', 'jpg', 'JPG', 'PNG', 'bmp'], 'Only png, jpg or bmp files please')])
	submit = SubmitField('Update Post')

class CommentForm(FlaskForm):
	content = StringField('comment content', validators=[DataRequired()])
	submit = SubmitField('Add Comment')