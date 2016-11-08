from flask_login import LoginManager

from app import app
from app.models.user import User

# Initialize and apply the LoginManager from flask_login which takes away
# some of the overhead of managing a cookies in a session
login_manager = LoginManager()
login_manager.init_app(app)
# Set the login page of the session manager so that the user is redirected
# to the login page if they are not logged in.
login_manager.login_view = 'index'

@login_manager.user_loader
def load_user(userid):
  """
  Flask-Login user_loader callback.
  The user_loader function asks this function to get a User Object or return
  None based on the userid.
  The userid was stored in the session environment by Flask-Login.
  user_loader stores the returned User object in current_user during every
  flask request.
  """
  return User.get(userid)
