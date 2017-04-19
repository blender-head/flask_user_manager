from flask import Blueprint

category_routes = Blueprint('category_routes', __name__,)

@category_routes.route('/')
def index():
   return '<h1>Category Index</h1>'

@category_routes.route('/add')
def add():
   return '<h1>Add Category</h1>'

@category_routes.route('/update')
def update():
   return '<h1>Update Category</h1>'

@category_routes.route('/delete')
def delete():
	return '<h1>Delete Category</h1>'