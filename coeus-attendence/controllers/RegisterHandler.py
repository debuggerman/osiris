import webapp2
import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Employee(db.Model):

    id = db.IntegerProperty()
    name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    designation = db.StringProperty(required=True)
    phone = db.StringListProperty(required=True)
    address = db.StringListProperty(required=True)
    joiningDate = db.DateProperty()
    CNIC = db.IntegerProperty(required=True)
    DOB = db.DateProperty()
    bloodGroup = db.StringProperty()
    NTN = db.IntegerProperty()
    DRI =db.UserProperty()



class RegisterHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user();
		if user is None:
			login_url = users.create_login_url(self.request.path)
			self.redirect(login_url)
			return
		else:
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.out.write('Hello, [' + user.nickname()+']')
		
	
#	def post(self):