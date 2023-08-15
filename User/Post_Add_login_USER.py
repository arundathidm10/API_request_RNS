#add new user
import requests
from User.Reusable_methods import generateEmail
emailgen = generateEmail()

url="https://thinking-tester-contact-list.herokuapp.com/users"
data= {"firstName": "Gary","lastName": "Test","email":emailgen,"password":"pswdgen"}
#post request
response=requests.post(url,json=data)
#print statements
print(response.status_code)
print(response.json())

#capturing a token
token = response.json().get('token')
print(f'token add user:{token}')


#login user which is already added

url="https://thinking-tester-contact-list.herokuapp.com/users/login"
data= {"email":emailgen,"password":"pswdgen"}
headers ={'Authorization':token}
response=requests.post(url,json=data,headers=headers)
print(response.status_code)
print(response.text)
print(response.headers)

