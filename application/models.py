""" models.py contains all database models used in the application """

from application import db, login_manager
from datetime import datetime
from flask_login import UserMixin
# flask login manager 
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

""" User modele class """

class User(db.Model, UserMixin):
	""" Define all column ffor the User model in the database """
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False) # nullable because input/data needed 
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
	password = db.Column(db.String(80), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)
	# represent user data 
	def __repr__(self):
		return f"User( '{self.username}','{self.email}','{self.image_file}' )"

""" Post model class """
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # "user" lower case we reference table/col name
	# represent post data/content
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}', '{self.content}')"