import os
#from config import config
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
import webapp2
from models.models import *
from dateutil.parser import *

class LeaveRequestHandler(webapp2.RequestHandler):

	def get(self):
		user = users.get_current_user()

		if user is None:
			loginUrl = users.create_login_url(self.request.path)
			self.redirect(loginUrl)
			return

		path =  os.path.join(os.path.dirname(__file__),'../views', 'leaveRequest.html')
		self.response.write(template.render(path, {"current_date": datetime.now()}))



	def post(self):
		
		user = users.get_current_user();
		
		if user is None:
			login_url = users.create_login_url(self.request.path)
			self.redirect(login_url)
			return

		#leaveStartDate
		#leaveEndDate
		#leaveType
		#leaveApproverEmail
		#leaveContactNumber
		#leaveAddressOnLeave
		leaveStartDate = parse(self.request.get("leaveStartDate"))
		leaveEndDate = parse(self.request.get("leaveEndDate"))
		leaveType = self.request.get("leaveType")
		leaveApproverEmail = self.request.get("leaveApproverEmail")
		leaveAddressOnLeave = self.request.get("leaveAddressOnLeave")
		leaveContactNumber = self.request.get("leaveContactNumber")
		leaveStatus = "pending"

		leave = Leave()
		leave.leaveSubmissionDate = datetime.datetime.now().date()
		leave.leaveStartDate = leaveStartDate.date()
		leave.leaveEndDate = leaveEndDate.date()
		leave.leaveApproverEmail = leaveApproverEmail
		leave.leaveType = leaveType
		leave.leaveStatus = leaveStatus
		leave.put()

		self.response.write("Submited")
		# message = mail.EmailMessage()
		# message.sender = user.email()
		# message.to = to_addr
		# message.body = """
		# 	Someone requires your approval for the leaves
		# """
		# message.send()
