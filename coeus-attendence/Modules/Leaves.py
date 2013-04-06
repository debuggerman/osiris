import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Employee(db.Model):
	name = db.StringProperty(required=True)
	email = db.StringProperty(required=True)

class Leave(db.Model):
	leaveSubmissionDate = datetime.date
	# leaveStartDate = datetime.date(required=True)
	# leaveEndDate = datetime.date(required=True)
	# leaveType = db.StringListProperty(required=True)
	# leaveApprover = Employee(required=True)
	# comments = db.StringProperty(required=False)
	# contactNumber = db.StringProperty(required=True)
	# addressOnLeave = db.StringProperty(required=True)
	# approversComments = db.StringProperty(required=True)
	# leaveStatus = db.StringProperty(required=True)
