""" models.py contains all database models used """

from application import db 
from datetime import datetime



class User(db.Model):
	""" Define all column for the User model in the database """
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False) # nullable because input/data needed 
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
	password = db.Column(db.String(80), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		""" representation of User """
		return f"User( '{self.username}','{self.email}','{self.image_file}' )" 

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # "user" lower case because reference to table/col name
	
	def __repr__(self):
		""" representation of Post """
		return f"Post('{self.title}', '{self.date_posted}', '{self.content}')"