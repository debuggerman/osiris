import os
#from config import config
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
import webapp2
from models.models import *
from dateutil.parser import *

class LeaveResponseHandler(webapp2.RequestHandler):
	def get(self, leave_id, method):

		user = users.get_current_user()

		if user is None:
			loginUrl = users.create_login_url(self.request.path)
			self.redirect(loginUrl)
			return

		path =  os.path.join(os.path.dirname(__file__),'../views', 'leaveRequestApproval.html')
		self.response.write(template.render(path, {"method": method, "leave_id": leave_id}))



class LeaveRequestHandler(webapp2.RequestHandler):

	def get(self):
		user = users.get_current_user()

		if user is None:
			loginUrl = users.create_login_url(self.request.path)
			self.redirect(loginUrl)
			return

		path =  os.path.join(os.path.dirname(__file__),'../views', 'leaveRequest.html')
		self.response.write(template.render(path, {"current_date": datetime.datetime.now()}))



	def post(self):
		
		user = users.get_current_user();
		
		if user is None:
			login_url = users.create_login_url(self.request.path)
			self.redirect(login_url)
			return

		leaveStartDate = parse(self.request.get("leaveStartDate"))
		leaveEndDate = parse(self.request.get("leaveEndDate"))
		leaveType = self.request.get("leaveType")
		leaveApproverEmail = self.request.get("leaveApproverEmail")
		leaveAddressOnLeave = self.request.get("leaveAddressOnLeave")
		leaveContactNumber = self.request.get("leaveContactNumber")
		leaveStatus = "pending"

		#validate approverEmail

		leave = Leave()
		leave.leaveSubmissionDate = datetime.datetime.now().date()
		leave.leaveStartDate = leaveStartDate.date()
		leave.leaveEndDate = leaveEndDate.date()
		leave.leaveApproverEmail = leaveApproverEmail
		leave.leaveType = leaveType
		leave.leaveStatus = leaveStatus
		leave.put()

		template_path =  os.path.join(os.path.dirname(__file__),'../views', 'leaveRequestEmail.html')

		approverName = "Approver"
		senderName = "SenderName"
		leaveType = "Sick Leave"
		leaveDays = "5"

		message = mail.EmailMessage()
		message.sender = user.email()
		message.to = leaveApproverEmail
		message.body = template.render(template_path, {
			"approverName": approverName,
			"senderName": senderName,
			"leaveType": leaveType,
			"days": leaveDays,
			"approveUrl": leave.createApproveUrl(self.request),
			"rejectUrl": leave.createRejectUrl(self.request),
			"dashboardUrl":self.request.host_url})

		#message.send()
		#self.redirect("/")
		self.response.write(message.body)
