from functools import wraps
from flask import request, Response
import base64

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'blah'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

'''
    The following is how request.authorization works under the hood
'''
def getAuth(headers):
    authHeader = headers.get("Authorization")
    auth = { 'username': '', 'password': ''}
    if authHeader:
        authCoded = authHeader.split(' ', 1)[1]
        decoded = base64.b64decode(authCoded)
        userData = decoded.split(':', 1)
        auth['username'] = userData[0]
        auth['password'] = userData[1]
    return auth
