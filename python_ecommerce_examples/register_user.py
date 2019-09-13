import requests
import ipdb

response = requests.post(
  "http://localhost:3000/v1/user",
  data={
    "name": "Phoenix",
    "login": "fenix",
    "password": "password"
  },
)

print(response.status_code)
print(response.text)