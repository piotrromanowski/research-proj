from flask import render_template
from app import app
from utils.authentication import requires_auth

@app.route('/')
@app.route('/index')
def index():
  # render index page route
  data = { 'title': 'Flask Basic Auth Example',
           'header': 'Basic Auth Home'}
  return render_template('index.html',data=data)

@app.route('/restricted')
@requires_auth
def restrictedPage():
  # route to the restricted that requires authentication
  return render_template('restricted.html')
