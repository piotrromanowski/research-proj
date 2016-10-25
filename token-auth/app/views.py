from app import app
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import request

from models.user import User
from models.user import create_token
from models.user import hash_pass

from utils.authentication import auth_required

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
  user = User.get(request.form['username'])
  if user and hash_pass(request.form['password']) == user.password:
    # TODO: Insert token into header
    token = create_token(user)
    return make_response(
                jsonify({'token': token}))
  else:
    response = make_response(
      jsonify({'message': 'invalid user/password'})
    )
    response.status_code = 401
    return response

  return redirect("/index")

@app.route('/restricted')
@auth_required
def restricted():
  return make_response(
    jsonify({'message': 'you got to my secret message!'})
  )
