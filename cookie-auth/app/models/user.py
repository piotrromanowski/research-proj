from app import app

from flask_login import UserMixin
import md5
from itsdangerous import URLSafeTimedSerializer

login_serializer = URLSafeTimedSerializer(app.secret_key)

'''
Create mini in-memory data-base
'''
def hash_pass(password):
  salted_password = password + app.secret_key
  return md5.new(salted_password).hexdigest()

USERS = [("piotr", hash_pass("password123"))]

class User(UserMixin):

  def __init__(self, user_id, password):
    self.id = user_id
    self.password = password
    print 'app:'
    print app.secret_key

  def get_auth_token(self):
    data = [str(self.id), self.password]
    return login_serializer.dumps(data)

  @staticmethod
  def get(user_id):
    print 'Looking for user'
    for user in USERS:
      if user[0] == user_id:
        return User(user[0], user[1])
