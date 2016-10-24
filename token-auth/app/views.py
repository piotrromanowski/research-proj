from app import app
from flask import render_template

from models.user import User
from models.user import hash_pass

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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
