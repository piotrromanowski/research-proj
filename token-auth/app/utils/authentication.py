from flask import g
from flask import jsonify
from flask import request
from functools import wraps
from app.models.user import parse_token


def auth_required(f):
  @wraps(f)
  def auth_required_wrapper(*args, **kwargs):
    if not request.headers.get('Authorization'):
      response = jsonify(message='Missing auth header')
      response.status_code = 401
      return response
    try:
      payload = parse_token(request)
    except DecodeError:
      response = jsonify(message='Invalid Token')
      response.status_code = 401
      return response
    except ExpiredSignature:
      response = jsonify(message='Expired Token')
      response.status_code = 401
      return response
    g.user_id = payload['sub']
    return f(*args, **kwargs)
  return auth_required_wrapper
