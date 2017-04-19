from flask import Blueprint

user_routes = Blueprint('user_routes', __name__,)

@user_routes.route('/')
def index():
   return '<h1>User Index</h1>'

@user_routes.route('/add')
def add():
   return '<h1>Add User</h1>'

@user_routes.route('/update')
def update():
   return '<h1>Update User</h1>'

@user_routes.route('/delete')
def delete():
	return '<h1>Delete User</h1>'