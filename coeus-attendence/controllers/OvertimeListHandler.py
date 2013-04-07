import os
#from config import config
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
from models import Employee
from models import Overtime
import webapp2

class OvertimeHandler(webapp2.RequestHandler):

	def get(self):
		user = users.get_current_user()

		if user is None:
			loginUrl = users.create_login_url(self.request.path)
			self.redirect(loginUrl)
			return
		q = Employee.gql("WHERE email =:email",email=user.email())
		employee = q.get()
		
		path =  os.path.join(os.path.dirname(__file__),'../views', 'overtimeList.html')
		self.response.write(template.render(path, {"timelogs": employee.employee_timelogs,"back_url":"/"}))