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

def build_page(textarea_content):
	username = "<label>Username</label>"
	username_input = "<input type='text' name='username'/>"
    
	password = "<label>Password</label>"
	password_input = "<input type='text' name='password'/>"
    
	verify = "<label>Verify Password</label>"
	verify_input = "<input type='text' name='verify'/>"
    
	email = "<label>Email (optional)</label>"
	email_input = "<input type='text' name='email'/>"

	submit = "<input type='submit' value='Submit Query'/>"
	form = "<form method='post'>" + username + "<br>"  + username_input + "<br>" + password + "<br>"  + password_input + "<br>" + verify + "<br>"  + verify_input + "<br>" + email + "<br>"  + email_input + "<br>" + submit + "</form>"

	header = "<h2>Signup</h2>"
    
	return header + form    
    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
