import webapp2
import cgi
import re

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
      .error {color: red}
    </style>
</head>
<body>
    <h2>Signup</h2>
"""

page_footer = """
</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)
    
PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return USER_RE.match(password)
    
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)

page_form = """
<form action='/' method='post'>
    <table>
        <tr>
            <td><label>Username</label></td>
            <td>
            <input type='text' name='username' value='%(username)s' required/>
            </td>
            <td>
            <div class = 'error'>%(user_error)s</div>
            </td>
        </tr>
        <tr>
            <td><label>Password</label></td>
            <td>
            <input type='password' name='password' value="" required/>
            </td>
            <td>
            <div class = 'error'>%(password_error)s</div>
            </td>
        </tr>
        <tr>
            <td><label>Verify Password</label></td>
            <td>
            <input type='password' name='verify' value="" required/>
            </td>
            <td>
            <div class = 'error'>%(verify_error)s</div>
            </td>
        </tr>
        <tr>
            <td><label>Email (optional)</label></td>
            <td>
            <input type='text' name='email' value="%(email)s"/>
            </td>
            <td>
            <div class = 'error'>%(email_error)s</div>
            </td>
        </tr>
    </table>
    <input type='submit' value='Submit'/>
</form>
"""

class MainHandler(webapp2.RequestHandler):

    def write_form(self, username="", email="", user_error="", password_error="", verify_error="", email_error=""):
        content = page_header + page_form + page_footer
        self.response.write(content % {"username": username, "email": email, "user_error": user_error, "password_error": password_error, "verify_error": verify_error, "email_error": email_error})
    
    def get(self):
        self.write_form()
    
    def post(self):
        is_error = False
        user_username = self.request.get("username")
        user_email = self.request.get("email")
        password = self.request.get("password")
        verify = self.request.get("verify")
        error = self.request.get("error")
        user_error = ""
        password_error = ""
        verify_error = ""
        email_error = ""
        
        username = valid_username(user_username)
        # password = valid_password(password)
        # verify = valid_password(verify)
        email = valid_email(user_email)
            
        if not username:            
            user_error = "Please enter a valid username"
            is_error = True
            
        if not valid_password(password):
            password_error = "Please enter a valid password"
            is_error = True
            
        if verify != password:
            verify_error = "Your passwords do not match"
            is_error = True
        
        if user_email and not email:
            email_error = "Please enter a valid email address"
            is_error = True
            
        if is_error:
            self.write_form(username = user_username, email=user_email, user_error=user_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
        else:
            self.redirect("/welcome" + "?username=" + user_username)
        

class Welcome(webapp2.RequestHandler):        
    def get(self):
        user_username = self.request.get("username")
        welcome_message = "<h2>Welcome, " + user_username + "</h2>"
        self.response.write(welcome_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
