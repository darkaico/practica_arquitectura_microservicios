import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNWI3ZjI0MDI3NTljYjhiMDIyNWY1MmNlIiwidG9rZW5faWQiOiI1YjdmMjQwMjc1OWNiOGIwMjI1ZjUyY2YiLCJpYXQiOjE1MzUwNTg5NDZ9.rnzoC15AVS60qIS7INrZfb37SbOFvAfu-mT_iasLdqU'

headers_data = {'Authorization': 'Bearer ' + token}

response = requests.get(
  "http://localhost:3000/v1/users",
  headers=headers_data
)

print(response.status_code)
print(response.text)