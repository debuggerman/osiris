import os
#from config import config
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
import webapp2

class MainHandler(webapp2.RequestHandler):
	
    def get(self): 
    	user = users.get_current_user()

    	if user is None:
    		loginUrl = users.create_login_url(self.request.path)
    		self.redirect(loginUrl)
    		return

		#query Employee for user.email
		# if not found, render registration.html -> onSubmit redirect to /register_user
    	path =  os.path.join(os.path.dirname(__file__),'../views', 'index.html')
        self.response.write(
        		template.render(path, {
        				"username": user.nickname(), 
        				"logout_url": users.create_logout_url("/")
        			})

        	)
