import os
#from config import config
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
import webapp2


#from controllers.models import *

class MainHandler(webapp2.RequestHandler):
	
    def get(self): 
    	user = users.get_current_user()

    	if user is None:
    		loginUrl = users.create_login_url(self.request.path)
    		self.redirect(loginUrl)
    		return
    	else:
    		self.response.out.write('in else')
