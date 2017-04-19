from flask import Blueprint, jsonify
from libraries.json_output import JsonOutput
from app.users.query import Query

user_routes = Blueprint('user_routes', __name__,)

query = Query()

@user_routes.route('/', methods=['GET'])
def index():
	users = query.get_all()

	output = JsonOutput(0, message="Success", data=users, http_code=200)
   	
   	return jsonify(output.serialize())

@user_routes.route('/register', methods=['POST'])
def register():
   return '<h1>Add User</h1>'

@user_routes.route('/update', methods=['PUT'])
def update():
   return '<h1>Update User</h1>'

@user_routes.route('/delete', methods=['DELETE'])
def delete():
	return '<h1>Delete User</h1>'