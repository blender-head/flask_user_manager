import os

APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/findus'

SQLALCHEMY_TRACK_MODIFICATIONS = False

API_VERSION = 1.0

API_VERSION_URL = '/api/v1'
	