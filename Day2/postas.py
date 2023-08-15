import requests
url = "https://thinking-tester-contact-list.herokuapp.com/users"
data = {"firstName": "Test","lastName": "User","email": "bestfriend@fake.com","password": "myPassword"}
post_response = requests.post(url,json=data)
#print the response
print(post_response.status_code)
response_json = post_response.json()
print(response_json)

