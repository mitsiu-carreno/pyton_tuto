import urllib2
import json

class FacebookInfo:
	fid=""
	username = ""

	def __init__(self, response):
		self.fid = response.id
		self.username = response.username

response = urllib2.urlopen('https://graph.facebook.com/v2.2/TakisUSA?access_token=CAAVmG3HrgLoBAOQUiwAgGPqbcK05EUdCVBQZCBwEMzYEj8xQUdNjeNJh9Jn8XESuRshAYkVKD1bz30IW09dAZCdihwRUXAzRZASpTZCEsUZBZAXHZBPIkChNBYW2OCzdn0pwA1wTp0BWrM9hl9RyQKBmy65ipWHr18imWYRnohhF8WbpkFUd5fVd1hZBhLlZB2WMZD')
data = json.load(response)
print data['id']
#test = FacebookInfo(response)
#print"%d" % test.fid
