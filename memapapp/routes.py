from flask import render_template, flash, redirect, url_for, session, request, Blueprint
from memapapp import app, db
from memapapp.forms import LoginForm, SignupForm, ProfileForm, PostForm, CommentForm
from memapapp.models import User,Post,Profile,Comment,Follow
from werkzeug.security import generate_password_hash, check_password_hash
from memapapp.config import Config
from flask_paginate import Pagination, get_page_parameter
import os
import datetime

@app.route('/map')
def map():
	if not session.get("USERNAME") is None:
		user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
		return render_template('map.html',user=user_in_db)
	else:
		flash("User needs to either login or signup first")
		return redirect(url_for('login'))

# reference lines 22-57, lecture 11,12
@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user_in_db = User.query.filter(User.username == form.username.data).first()
		if not user_in_db:
			flash('No user found with username: {}'.format(form.username.data))
			return redirect(url_for('login'))
		if (check_password_hash(user_in_db.password_hash, form.password.data)):
			# flash('Login success!')
			session["USERNAME"] = user_in_db.username
			return redirect(url_for('choice'))
		flash('Incorrect Password')
		return redirect(url_for('login'))
	return render_template('login.html', title='Login', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		if form.password.data != form.password2.data:
			flash('Two passwords do not match!')
			return redirect(url_for('signup'))
		user_in_db = User.query.filter(User.username == form.username.data).first()
		if user_in_db:
			flash('This username has been signed up: {}'.format(form.username.data))
			return redirect(url_for('signup'))
		passw_hash = generate_password_hash(form.password.data)
		user = User(username=form.username.data, email=form.email.data, password_hash=passw_hash)
		db.session.add(user)
		db.session.commit()
		flash('User registered with username:{}'.format(form.username.data))
		session["USERNAME"] = user.username
		print(session)
		return redirect(url_for('profile',post_id=-1))
	return render_template('signup.html', title='Register a new user', form=form)

# reference lines 63-70,80-93 lecture 13
@app.route('/profile/<post_id>', methods=['GET', 'POST'])
def profile(post_id):
	form = ProfileForm()
	if not session.get("USERNAME") is None:
		if form.validate_on_submit():
			cv_dir = Config.CV_UPLOAD_DIR
			file_obj = form.cv.data
			cv_filename = session.get("USERNAME") + '_CV.pdf'
			# if user does not change it, it will stay the same
			if file_obj:
				file_obj.save(os.path.join(cv_dir, cv_filename))
			
			photo_dir = Config.PHOTO_UPLOAD_DIR
			file_obj2 = form.photo.data
			photo_filename = session.get("USERNAME") + '_PHOTO.png'
			if file_obj2:
				file_obj2.save(os.path.join(photo_dir, photo_filename))
			
			flash('Personal information uploaded and saved')
			# now we add the object to the database
			user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
			posts = Post.query.filter(Post.user_id == user_in_db.id).all()
			number = Post.query.filter(Post.user_id == user_in_db.id).count()
			#check if user already has a profile
			stored_profile = Profile.query.filter(Profile.user == user_in_db).first()
			if not stored_profile:
				# if no profile exists, add a new object
				profile = Profile(dob=form.dob.data, gender=form.gender.data, cv=cv_filename.encode("utf-8"),user=user_in_db)
				db.session.add(profile)
			else:
				# else, modify the existing object with form data
				stored_profile.dob = form.dob.data
				stored_profile.gender = form.gender.data
			# remember to commit	
			db.session.commit()
			return redirect(url_for('profile',post_id=-1))
		else:
			user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
			
			postsafter = Post.query.filter(Post.user_id == user_in_db.id).all()
			if post_id != '-1':
				if postsafter:
					# both posts exist and post_id exist, then it will excute delete operation
					postde=Post.query.filter(Post.id == post_id).first()
					comments=Comment.query.filter(Comment.post_id == post_id).all()
					photo_dir = Config.PHOTO_UPLOAD_DIR
					# remove relative photo and comments
					os.remove(os.path.join(photo_dir, postde.photo.decode('utf-8')))
					if comments:
						for comment in comments:
							db.session.delete(comment)
					db.session.delete(postde)
					db.session.commit()
			number = Post.query.filter(Post.user_id == user_in_db.id).count()
			posts = Post.query.filter(Post.user_id == user_in_db.id).all()
			stored_profile = Profile.query.filter(Profile.user == user_in_db).first()
			
			if not stored_profile:
				return render_template('profile.html', title='Add your profile', form=form, user=user_in_db, posts=posts,number=number,post_id=-1)
			else:
				form.dob.data = stored_profile.dob
				form.gender.data = stored_profile.gender
				return render_template('profile.html', title='Modify your profile', form=form, user=user_in_db, posts=posts,number=number,post_id=-1)
				
	else:
		flash("User needs to either login or signup first")
		return redirect(url_for('login'))
		
@app.route('/choice')
def choice():
	if not session.get("USERNAME") is None:
		user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
		users = User.query.all()
		prev_posts = Post.query.count()
		search = False
		print("Checking for user: {} with id: {}".format(user_in_db.username, user_in_db.id))
		# every page only show 10 posts
		page = request.args.get(get_page_parameter(),type=int,default=1)
		start = (page-1)* 10
		end = start + 10
		# from start post search to end post
		posts = Post.query.order_by(Post.timestamp.desc()).slice(start,end).all()
		pagination = Pagination(page=page,total=prev_posts,outer_window=2,inner_window=1)
		return render_template('choice.html', posts=posts, user=user_in_db, pagination=pagination, number=prev_posts, users=users)
	else:
		flash("User needs to either login or signup first")
		return redirect(url_for('login'))
		
@app.route('/makepost/<type_id>/', methods=['GET', 'POST'])
def makepost(type_id):
	form = PostForm()
	if not session.get("USERNAME") is None:
		if form.validate_on_submit():
			user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()

			photo_dir = Config.PHOTO_UPLOAD_DIR
			file_obj = form.photo.data
			# set a instinct name for every photo
			photo_filename = session.get("USERNAME") +'_'+ datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S') + '_PHOTO.png'
			file_obj.save(os.path.join(photo_dir, photo_filename))

			user_Id = user_in_db.id
			post = Post(title=form.title.data, area=form.area.data, body=form.body.data, user_id=user_Id, photo=photo_filename.encode("utf-8"))
			db.session.add(post)
			db.session.commit()
			flash('Post uploaded and saved')
			return redirect(url_for('makepost', type_id=0))
		else:
			user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
			print("Checking for user: {} with id: {}".format(user_in_db.username, user_in_db.id))

			return render_template('makepost.html', title='Add/Modify your profile', form=form, user=user_in_db,type_id=type_id)
	else:
		flash("User needs to either login or signup first")
		return redirect(url_for('login'))


@app.route('/p/<post_id>/', methods=['GET', 'POST'])
def post_detail(post_id):
	form = CommentForm()
	if not session.get("USERNAME") is None:
		if form.validate_on_submit():
			user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
			post = Post.query.filter(Post.id == post_id).first()
			comments = Comment.query.filter(Comment.post_id == post_id).all()
			user_auther = User.query.filter(User.id == post.user_id).first()
			if not post:
				return redirect(url_for('choice'))
			
			# creates comments for the post 
			comment = Comment(content = form.content.data, user_id = user_in_db.id, post_id = post_id)
			db.session.add(comment)
			db.session.commit()
			flash('Comment uploaded and saved')
			return redirect(url_for('post_detail', post_id=post_id))
		else:
			user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
			users = User.query.all()
			post = Post.query.filter(Post.id == post_id).first()
			comments = Comment.query.filter(Comment.post_id == post_id).all()
			user_auther = User.query.filter(User.id == post.user_id).first()
			return render_template('post_detail.html', form=form, post=post, users=users, user=user_in_db, usera = user_auther, comments = comments)
		
	else:
		flash("User needs to either login or signup first")
		return redirect(url_for('login'))

@app.route('/follow/<user_id>/')
def follow(user_id):
	if not session.get("USERNAME") is None:
		user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
		if user_id != '0':
			if user_id > '0':
				prefollow = Follow.query.filter(Follow.user_id == user_in_db.id, Follow.friend_id == user_id).all()
				if not prefollow:
					follow = Follow(user_id = user_in_db.id, friend_id = user_id)
					db.session.add(follow)
			else:
				usera_id = user_id.replace('-','')
				unfollow = Follow.query.filter(Follow.user_id == user_in_db.id, Follow.friend_id == usera_id).first()
				if unfollow:
					db.session.delete(unfollow)
			db.session.commit()
		users = User.query.all()
		followedusers = User.query.join(Follow, User.id == Follow.friend_id).filter(Follow.user_id == user_in_db.id).all()
		# followedusers = Friends.query.filter(Friends.user_id == user_in_db.id).all()
		follow = Follow.query.filter(Follow.user_id == user_in_db.id).count()
		followed = Follow.query.filter(Follow.friend_id == user_in_db.id).count()
		posts = Post.query.join(Follow, Post.user_id == Follow.friend_id).order_by(Post.timestamp.desc()).filter(Follow.user_id == user_in_db.id).limit(5).all()
				
		return render_template('follow.html', user=user_in_db, users=users, follow=follow, followed=followed, followedusers=followedusers,posts=posts)
		
	else:
		flash("User needs to either login or signup first")
		return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.pop("USERNAME", None)
	return redirect(url_for('login'))