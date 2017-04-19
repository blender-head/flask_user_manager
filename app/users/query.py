import psycopg2
from psycopg2.extras import RealDictCursor

from libraries.base_query import BaseQuery

from app.users.models import Users

class Query(BaseQuery):

	def __init__(self):
		self.connection = self.connect()

	def get_all(self):

		try:

			query = "SELECT id, username, email FROM users;"
			cursor = self.connection.cursor(cursor_factory=RealDictCursor)
			cursor.execute(query)
			data = cursor.fetchall()

			return data
				

		finally:
			self.connection.close()