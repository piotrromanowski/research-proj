from functools import wraps
from flask import request, Response
import base64

def check_auth(username, password):
    # Check if the uesrname and password are valid
    # In a real world example the password would not be stored in
    # plain text and instead encrypted and stored in a database
    return username == 'admin' and password == 'blah'

def authenticate():
    # Respond with 'WWW-Authenticate' to prompt user for credentials
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
    but is not actually being used.
'''
def getAuth(headers):
    authHeader = headers.get("Authorization")
    auth = { 'username': '', 'password': ''}
    # Check if Authorization header exists
    if authHeader:
        # retrieve Authorization header data
        authCoded = authHeader.split(' ', 1)[1]
        # Decode the authorization header data
        decoded = base64.b64decode(authCoded)
        # Split the decoded data on :
        userData = decoded.split(':', 1)
        # the first element of the array is the username
        auth['username'] = userData[0]
        # the second element of the array is the password
        auth['password'] = userData[1]
    return auth
