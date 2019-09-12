import jwt

SECRET = 'secret-seed'

payload = {
  "iss": "Homero Simpsons",
  "sub": "Bart Simpsons",
  'exp': 1371720939
}

encoded_jwt = jwt.encode(payload, SECRET, algorithm='HS256')

print(encoded_jwt)
