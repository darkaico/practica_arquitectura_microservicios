import jwt

SECRET = 'secret-seed'

encoded_jwt = ''

decoded_jwt = jwt.decode(encoded_jwt, SECRET, algorithms=['HS256'])

print(decoded_jwt)
