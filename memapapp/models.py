from datetime import datetime
from memapapp import db

# reference lines 5-36, lecture12
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	profile = db.relationship('Profile', backref='user', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	area = db.Column(db.Integer)
	title = db.Column(db.String(64))
	body = db.Column(db.String(256))
	photo = db.Column(db.String(256))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post {}>'.format(self.body)
	
class Profile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dob = db.Column(db.DateTime, index=True)
	gender = db.Column(db.String(10), index=True)
	cv = db.Column(db.String(256))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return '<Profile for user: {}, gender: {}, birthday: {}>'.format(self.user_id, self.dob, self.dob)
	
class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(256))
	create_time = db.Column(db.DateTime, index=True, default=datetime.now)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

	def __repr__(self):
		return '<Comment for content: {}, user: {}, post: {}>'.format(self.content, self.user_id, self.post_id)

class Follow(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	friend_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Friends for user: {}, friend: {}>'.format(self.user_id, self.friend_id)