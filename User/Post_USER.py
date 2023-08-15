import requests
baseURl = "https://thinking-tester-contact-list.herokuapp.com"
endpoint = "/users/login"
cred = {"email": "tom@testmail.com", "password": "Password@123"}

headers = {'Content-Type': 'application/json'}  # Replace 'application/json' with your desired content-type string
# request_json =  json.loads(cred)
# Make a POST request with the specified content-type
response = requests.post(url= baseURl+endpoint, headers={'Content-Type': 'application/json'}, data='{"email": "tom@testmail.com", "password": "Password@123"}')
# x.token

json_data = response.json()
token = json_data["token"]

userprofile = "https://thinking-tester-contact-list.herokuapp.com/users/me"
headers = {'Authorization': token}
resp = requests.get(url=userprofile,headers=headers)

print(resp.text)