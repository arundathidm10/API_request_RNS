import json

import requests

payload = {"name": "Rajeee",
    "job": "Engineer"
}
#Deserialize
response = requests.post("https://reqres.in/api/users",data=payload)
print(response.status_code)
print(response)
print(response.json())
#assert data
assert response.json()['job'] == "Engineer","Is not matching the job!"
