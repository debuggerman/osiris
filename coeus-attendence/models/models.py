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

