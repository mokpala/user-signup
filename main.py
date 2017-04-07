import webapp2
import cgi
import re

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
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
<form action='/welcome' method='post'>
    <table>
        <tr>
            <td><label>Username</label></td>
            <td>
            <input type='text' name='username' value='%(username)s'/>
            </td>
            <td>
            <div style="color: red">%(error)s</div>
            </td>
        </tr>
        <tr>
            <td><label>Password</label></td>
            <td>
            <input type='password' name='password' value=""/>
            </td>
            <td>
            <div style="color: red">%(error)s</div>
            </td>
        </tr>
        <tr>
            <td><label>Verify Password</label></td>
            <td>
            <input type='password' name='verify' value=""/>
            </td>
            <td>
            <div style="color: red">%(error)s</div>
            </td>
        </tr>
        <tr>
            <td><label>Email (optional)</label></td>
            <td>
            <input type='text' name='email' value="%(email)s"/>
            </td>
            <td>
            <div style="color: red">%(error)s</div>
            </td>
        </tr>
    </table>
    <input type='submit' value='Submit'/>
</form>
"""

class MainHandler(webapp2.RequestHandler):

    def write_form(self, username="", error="", email=""):
        self.response.write(page_form % {"username": username, "error": error, "email": email})
    
    def get(self):
        self.write_form()
    
    def post(self):
        user_username = self.request.get("username")
        user_password = self.request.get("password")
        user_verify = self.request.get("verify")
        user_email = self.request.get("email")
        
        username = valid_username(user_username)
        password = valid_password(user_password)
        verify = valid_password(user_verify)
        email = valid_email(user_email)
        
        if username == "":
            self.write_form("Username cannot be blank.", user_username)
        if not valid_username(username):
            self.write_form("Please enter a valid username.", user_username)
            
        if password == "":
            self.write_form("Password cannot be blank.", user_password)
        if not valid_password(password):
            self.write_form("Please enter a valid password.", user_password)
            
        if verify == "":
            self.write_form("Please verify your password.", user_verify)
        if verify != password:
            self.write_form("Your passwords do not match.", user_password, user_verify)
            
        if not valid_email(email):
            self.write_form("Please enter a valid email address.", user_email)
            
        else:
            self.redirect("/welcome")
        
        content = page_header + page_form + page_footer
        self.response.write(content)

class Welcome(webapp2.RequestHandler):        
    def get(self):
        username = valid_username(self.request.get("username"))
        if valid_username(username):
            welcome_message = "<h2>Welcome, " + username + "</h2>"
        self.response.write(welcome_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
