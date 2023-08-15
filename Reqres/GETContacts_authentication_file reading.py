import json
import requests
#reading json data from datajson file
mydata =open('data.json','r').read()
#Deserialize
response = requests.get("https://thinking-tester-contact-list.herokuapp.com/contacts")
print(response.status_code)
print(response)
print(response.json())
#assert data
assert response.json()['job'] == "Accountant","Is not matching the job!"





