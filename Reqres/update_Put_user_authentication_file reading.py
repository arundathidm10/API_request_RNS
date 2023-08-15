import json
import requests
payload = {
    "name": "Satya",
    "job": "Engineer"
}
response = requests.put("https://reqres.in/api/users/2",data=payload)
print(response.status_code)
print(response)
print(response.json())
#assert data
assert response.json()['job'] == "Engineer","Is not matching the job!"
