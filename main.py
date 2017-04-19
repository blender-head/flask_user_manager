from app import app, db 
from app.users.controllers import user_routes
from app.categories.controllers import category_routes

api_version_url = app.config['API_VERSION_URL']

app.register_blueprint(user_routes, url_prefix=api_version_url + '/users')
app.register_blueprint(category_routes, url_prefix=api_version_url + '/categories')

if __name__ == '__main__':
	app.run()