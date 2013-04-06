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
from controllers import MainHandler, LeaveRequestHandler,RegisterHandler, LeaveResponseHandler

app = webapp2.WSGIApplication( [ 
	webapp2.Route(r'/', handler=MainHandler, name='home'),
	webapp2.Route(r'/respond_leave.do/<leave_id:\d+>/<method:\w+>', handler=LeaveResponseHandler, name='leaveResponse'),
	webapp2.Route('/employee_register.do', handler=RegisterHandler, name="register"),
	webapp2.Route('/request_leave.do?', handler=LeaveRequestHandler, name="requestLeave"),
	webapp2.Route('/register.do?', handler=RegisterHandler, name="register"),	
 ], debug=True)
 
