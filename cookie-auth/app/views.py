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

  return render_template('index.html',
                          data=data)

@app.route('/login', methods=["POST"])
def login():
  user = User.get(request.form['username'])
  if user and hash_pass(request.form['password']) == user.password:
    login_user(user, remember=True)
    return redirect(request.args.get("next") or "/")
  else:
    print 'Not authenticated succesfully'
    print user.password
    print hash_pass(request.form['password'])

  return redirect("/index")

@app.route("/logout")
def logout_page():
    logout_user()
    return redirect("/")

@app.route('/restricted')
@login_required
def restrictedPage():
  return render_template('restricted.html')
