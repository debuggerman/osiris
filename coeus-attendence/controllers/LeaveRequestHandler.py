import os
#from config import config
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
import webapp2

class LeaveRequestHandler(webapp2.RequestHandler):

	def get(self):
		user = users.get_current_user()

		if user is None:
			loginUrl = users.create_login_url(self.request.path)
			self.redirect(loginUrl)
			return
			
		path =  os.path.join(os.path.dirname(__file__),'../views', 'leaveRequest.html')
		self.response.write(template.render(path, None))



	def post(self):
		
		user = users.get_current_user();
		
		if user is None:
			login_url = users.create_login_url(self.request.path)
			self.redirect(login_url)
			return

		to_addr = self.request.get("leaveApproverEmail")

		message = mail.EmailMessage()
		message.sender = user.email()
		message.to = to_addr
		message.body = """
			Someone requires your approval for the leaves
		"""
		message.send()
