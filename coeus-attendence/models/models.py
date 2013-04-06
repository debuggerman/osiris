import datetime
import webapp2
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import mail

class Employee(db.Model):
	id = db.IntegerProperty()
	name = db.StringProperty()
	email = db.EmailProperty()
	designation = db.StringProperty()
	phone = db.StringListProperty()
	address = db.StringListProperty()
	joiningDate = db.DateProperty()
	CNIC = db.StringProperty()
	DOB = db.DateProperty()
	bloodGroup = db.StringProperty()
	NTN = db.StringProperty()
	DRI = db.EmailProperty()


class Leave(db.Model):
	leaveSubmissionDate = db.DateProperty()
	leaveStartDate = db.DateProperty()
	leaveEndDate = db.DateProperty()
	leaveType = db.StringProperty()
	leaveApproverEmail = db.StringProperty()
	comments = db.StringProperty()
	contactNumber = db.StringProperty()
	addressOnLeave = db.StringProperty()
	approversComments = db.StringProperty()
	leaveStatus = db.StringProperty()

	def createApproveUrl(self, request):
		return request.host_url + "/respond_leave.do/" + str(self.key().id())  + "/approve"

	def createRejectUrl(self, request):
		return request.host_url + "/respond_leave.do/"  + str(self.key().id())  + "/reject"

