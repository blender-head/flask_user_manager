import datetime

from app import db

class Categories(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	
	created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)

	modified_timestamp = db.Column(
		db.DateTime,
		default=datetime.datetime.now,
		onupdate=datetime.datetime.now
	)