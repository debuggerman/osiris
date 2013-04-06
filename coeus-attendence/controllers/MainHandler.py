import os
#from config import config
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template
import time
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
                path =  os.path.join(os.path.dirname(__file__),'../views', 'register.html')
                self.response.write(template.render(path,{'employee_name':user.nickname(),'employee_email':user.email()}))
            else:
                timelog_query=TimeLog.gql("WHERE user= :1 and submissionDate= :2 ORDER BY submissionDate", users.get_current_user().nickname(), datetime.datetime.now().date())
                log = timelog_query.get()
                
                if log is None or log.checkoutTime:
                    button_text = 'Check in'
                else:
                    button_text = 'Check out'
                
               

                path =  os.path.join(os.path.dirname(__file__),'../views', 'index.html')
                self.response.write(template.render(path,{'username':user.nickname(),'employee_email':user.email(), 'user': users.get_current_user().nickname(), 'button_text':button_text}))

    def post(self):
        
        timelog_query=TimeLog.gql("WHERE user= :1 and submissionDate= :2", users.get_current_user().nickname(), datetime.datetime.now().date())
        existingLog = timelog_query.get()
        if existingLog is None or existingLog.checkoutTime:
            newlog = TimeLog()
            newlog.user = users.get_current_user().nickname()
            newlog.submissionDate=datetime.datetime.now().date()
            newlog.checkinTime=datetime.datetime.now()
            newlog.put()
        else:
            existingLog.checkoutTime=datetime.datetime.now()
            existingLog.checkoutComment=self.request.get('comment')
            existingLog.put()
        
        time.sleep(3)
        self.redirect(self.request.path)
