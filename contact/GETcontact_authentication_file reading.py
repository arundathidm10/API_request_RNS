import json

import requests

#Deserialize
response = requests.get("https://thinking-tester-contact-list.herokuapp.com/contacts")
print(response.status_code)
print(response)
print(response.json())

