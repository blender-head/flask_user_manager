import psycopg2
import db_config

class BaseQuery():

	def connect(self):
		return psycopg2.connect(host=db_config.DATABASE['DB_HOST'], user=db_config.DATABASE['DB_USER'], password=db_config.DATABASE['DB_PASSWD'], database=db_config.DATABASE['DB_NAME'])