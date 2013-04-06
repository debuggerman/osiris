import datetime
import webapp2
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import mail

class Employee(db.Model):
	name = db.StringProperty(required=True)
	email = db.StringProperty(required=True)

class Leave(db.Model):
	leaveSubmissionDate = db.DateProperty()
	leaveStartDate = db.DateProperty()
	leaveEndDate = db.DateProperty()
	leaveType = db.StringListProperty()
	leaveApproverEmail = db.StringProperty()
	comments = db.StringProperty()
	contactNumber = db.StringProperty()
	addressOnLeave = db.StringProperty()
	approversComments = db.StringProperty()
	leaveStatus = db.StringProperty()


class LeaveRequestHandler(webapp2.RequestHandler):
	def post(self):
		
		user = users.get_current_user();
		
		if user is None:
			login_url = users.create_login_url(self.request.path)
			self.redirect(login_url)
			return

		to_addr = self.request.get("leaveApproverEmail")
			# Error message
			pass

		message = mail.EmailMessage()
		message.sender = user.email()
		message.to = to_addr
		message.body = """
			Someone requires your approval for the leaves
		"""
		message.send()

