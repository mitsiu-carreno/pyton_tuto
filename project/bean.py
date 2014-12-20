
class FacebookInfo:
	id=""
	username = ""

	def __init__(self, response):
		self.id = response['id']
		self.username = response['username']

 