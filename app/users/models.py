import datetime

from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100))
	email = db.Column(db.String(100), unique=True)
	created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)

	modified_timestamp = db.Column(
		db.DateTime,
		default=datetime.datetime.now,
		onupdate=datetime.datetime.now
	)