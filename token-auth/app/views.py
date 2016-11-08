from flask import jsonify
from flask import make_response
from flask import render_template
from flask import request

from app import app
from models.user import User
from models.user import create_token
from models.user import hash_pass
from utils.authentication import auth_required

@app.route('/')
@app.route('/index')
def index():
  # Index (home) page
  return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
  # Login route that is used to pass the credentials to in order to
  # retrieve a jwt token
  user = User.get(request.form['username'])
  if user and hash_pass(request.form['password']) == user.password:
    # If valid, create a token and return it to the user in the response
    token = create_token(user)
    return make_response(
                jsonify({'token': token}))
  else:
    # Return a response indicating that the request had invalid credentials
    response = make_response(
      jsonify({'message': 'invalid user/password'})
    )
    response.status_code = 401
    return response

@app.route('/restricted')
@auth_required
def restricted():
  # Restricted route that returns json conaining the secret message.
  # The route is wrapped with the auth_required decorator to verify that
  # a valid token exists in the request.
  return make_response(
    jsonify({'message': 'you got to my secret message!'})
  )
