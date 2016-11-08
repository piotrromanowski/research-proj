from app import app
from models.user import User
from models.user import hash_pass

from flask import render_template, request, redirect
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user

@app.route('/')
@app.route('/index')
def index():
  data = {'title': 'Flask Basic Auth Example',
          'header': 'Basic Auth Home'}
  # render the index (home) page
  return render_template('index.html',
                          data=data)

@app.route('/login', methods=["POST"])
def login():
  # This route is used to login, and retrieve the correct cookies
  # Check if user was found in the form and if the password submitted
  # in the form matches the user stored in the in-memory database
  if user and hash_pass(request.form['password']) == user.password:
    # If valid, set the cookie and send user to the requested route or
    # to the homepage. At this point the user will have a valid cookie
    # set in their header and will be able to access restricted routes
    login_user(user, remember=True)
    return redirect(request.args.get("next") or "/")
  else:
    # Credentials were invalid, log a message with the invalid credentials
    print "Invalid username and password {data}".format(data=user)
    # Finally, redirect user back to index (home) page
    return redirect("/index")

@app.route("/logout")
def logout_page():
    # If <host>/logout route is hit, remove cookie from header and
    # redirect the user to the index (home) page
    logout_user()
    return redirect("/index")

@app.route('/restricted')
@login_required
def restrictedPage():
  # Route that requires a user with valid cookie in header
  return render_template('restricted.html')
