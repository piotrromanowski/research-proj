import md5
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer

from app import app

login_serializer = URLSafeTimedSerializer(app.secret_key)

def hash_pass(password):
  salted_password = password + app.secret_key
  return md5.new(salted_password).hexdigest()

# Create mini in-memory data-base. In the real world, you would normally
# establish a connection to a database and query for the the users
USERS = [("piotr", hash_pass("password123"))]

class User(UserMixin):
''' User model that will be used to help un-abstract our users from data '''

  def __init__(self, user_id, password):
    self.id = user_id
    self.password = password

  def get_auth_token(self):
    data = [str(self.id), self.password]
    # create token from user data
    return login_serializer.dumps(data)

  @staticmethod
  def get(user_id):
    # Look up user from "in-memory data-base"
    for user in USERS:
      if user[0] == user_id:
        return User(user[0], user[1])
