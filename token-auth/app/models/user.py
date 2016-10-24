from app import app

from datetime import datetime
from datetime import timedelta
import jwt
import md5

'''
Create mini in-memory data-base
'''
def hash_pass(password):
  salted_password = password + app.secret_key
  return md5.new(salted_password).hexdigest()

USERS = [("piotr", hash_pass("password123"))]

class User():

  def __init__(self, user_id, password):
    self.id = user_id
    self.password = password

  @staticmethod
  def get(user_id):
    print 'Looking for user'
    for user in USERS:
      if user[0] == user_id:
        return User(user[0], user[1])

# JWT Helpers
def create_token(user):
  payload = {
    'sub': user.id, # subject
    'iat': datetime.utcnow(), # issued at
    'exp': datetime.utcnow() + timedelta(days=1) # expiration
  }
  token = jwt.encode(payload, app.secret_key, algorithm='HS256')
  return token.decode('unicode_escape')

def parse_token(req):
  token = req.headers.get('Authorization').split()[1]
  return jwt.decode(token, app.secret_key, algorithm='HS256')
