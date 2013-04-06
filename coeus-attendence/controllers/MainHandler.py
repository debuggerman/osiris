import os
#from config import config
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template

import webapp2


from models.models import *

class MainHandler(webapp2.RequestHandler):
	
    def get(self): 
    	user = users.get_current_user()

    	if user is None:
    		loginUrl = users.create_login_url("/")
    		self.redirect(loginUrl)
    		return
    	else:
			q = Employee.gql("WHERE email =:email",email=user.email())
			result = q.get()
			
			if result is None:
				self.response.out.write('NO User')
				path =  os.path.join(os.path.dirname(__file__),'../views', 'register.html')
				self.response.write(template.render(path,{'employee_name':user.nickname(),'employee_email':user.email()}))
			else:
				path =  os.path.join(os.path.dirname(__file__),'../views', 'index.html')
                self.response.write(template.render(path,None))
			
    		
