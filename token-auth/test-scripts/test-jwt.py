import jwt
from datetime import datetime
from datetime import timedelta

# ----------------------------------------------------------
# This is simply a test script that I used to test the jwt
# library to try out encoding and decoding a token generated
# by the library.
# ----------------------------------------------------------

payload = {
  'sub': 'piotr257', # subject
  'iat': datetime.utcnow(), # issued at
  'exp': datetime.utcnow() + timedelta(days=1) # expiration
}

secret_key = 'my_ultra_secret_key'

token = jwt.encode(payload, secret_key, algorithm='HS256')

print 'encoded payload'
print token

print token.decode('unicode_escape')


print 'decoding'
decoded = jwt.decode(token, secret_key, algorithm='HS256')
print decoded
