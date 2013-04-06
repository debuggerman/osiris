import os
#from config import config
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import webapp2

class MainHandler(webapp2.RequestHandler):
	
    def get(self):    	
    	path =  os.path.join(os.path.dirname(__file__),'../views', 'index.html')
        self.response.write(
        		template.render(path, {
        				"title": "Home Page", 
        				"year": "1999",
        				"domain": "coeus"
        			})

        	)
