class JsonOutput():

	def __init__(self, error_code, message, data, http_code):
		self.error_code = error_code
		self.message = message
		self.data = data
		self.http_code = http_code

	def serialize(self):
		return {
			'error_code': self.error_code,
			'message': self.message,
			'data': self.data,
			'http_code': self.http_code
		}