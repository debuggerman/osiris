#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import datetime
from Modules import Leaves

class MainHandler(webapp2.RequestHandler):
	
    def get(self):
    	e = Leaves.Employee(name="zaki", email="zaki.shaheen@coeus-solutions.de")
    	e.put()

    	e2 = Leaves.Employee(name="TL", email = "TL@coeus-solutions.de")
    	e2.put()

    	l = Leaves.Leave(parent=e)
    	l.submissionDate = datetime.datetime.now().date()
    	l.comments = "going home for marriage"
    	l.leaveStatus = "pending"
    	l.leaveApproverEmail = e2.email
    	l.put()


        self.response.write('It works!')

app = webapp2.WSGIApplication( [ ('/*', MainHandler) ], debug=True)
