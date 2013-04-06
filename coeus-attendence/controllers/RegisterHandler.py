import webapp2
import cgi
import datetime
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from models.models import *

from google.appengine.ext.webapp import template


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
		
	
	def post(self):
		employee = Employee()
		employee.name = (cgi.escape(self.request.get('name')))
		employee.email = user.email()
		employee.designation = (cgi.escape(self.request.get('designation')))
		employee.phone = [(cgi.escape(self.request.get('phone1'))),(cgi.escape(self.request.get('phone2')))]
		employee.address = [(cgi.escape(self.request.get('address1'))),(cgi.escape(self.request.get('address2')))]
		employee.joiningDate = (cgi.escape(self.request.get('joining_date')))
		employee.CNIC (cgi.escape(self.request.get('cnic')))
		employee.DOB = (cgi.escape(self.request.get('dob')))
		employee.bloodGroup = (cgi.escape(self.request.get('bloodgroup')))
		employee.NTN= (cgi.escape(self.request.get('ntn')))
		employee.DRI = (cgi.escape(self.request.get('dri')))				
		employee.put()
		self.redirect('/')