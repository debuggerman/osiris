import datetime
import webapp2
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import mail

class Overtime(db.Model):
    projectName      = db.StringProperty()
    isApproved       = db.BooleanProperty()
    approvedHours    = db.FloatProperty()
    approvedComments = db.StringProperty()
    approvedMonth    = db.StringProperty()