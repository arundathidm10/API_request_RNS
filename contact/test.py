import requests
from faker import Faker
def generateEmail():
    faker = Faker()
    return faker.email()

emailgen = generateEmail()
#Add user
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


# #login user which is already added
# url="https://thinking-tester-contact-list.herokuapp.com/users/login"
# data= {"email":emailgen,"password":"pswdgen"}
# headers ={'Authorization':token}
# response=requests.post(url,json=data,headers=headers)
# print(response.status_code)
# print(response.text)
# print(response.headers)

#Add contact 1
url="https://thinking-tester-contact-list.herokuapp.com/contacts"
data={"firstName": "Mac","lastName": "Street","birthdate": "1996-01-01","email": "mac@test.com","phone": "8005555678","street1": "2 Main St.",
    "street2": "Apartment A",}
headers={"Authorization":token}
response=requests.post(url,json=data,headers=headers)
print(response.status_code)

#Add another contact
url="https://thinking-tester-contact-list.herokuapp.com/contacts"
data={"firstName": "Tom","lastName": "Joe","birthdate": "1996-04-01","email": "tomj@test.com","phone": "8005555690","street1": "3 Main St.",
    "street2": "Apartment B",}
headers={"Authorization":token}
response=requests.post(url,json=data,headers=headers)
print(response.status_code)

# #Update contact
# url="https://thinking-tester-contact-list.herokuapp.com/contacts/"
# data={ "firstName": "Lilly"}
# headers ={'Authorization':token}
# response=requests.patch(url,json=data,headers=headers)
# print(response.status_code)
# print(response.headers)
#
# #Update contact
# url="https://thinking-tester-contact-list.herokuapp.com/contacts/"
# data={"firstName": "Henry","lastName": "Joe","birthdate": "1996-04-01","email": "tomj@test.com","phone": "8005555690","street1": "3 Main St.",
#     "street2": "Apartment B",}
# headers ={'Authorization':token}
# response=requests.put(url,json=data,headers=headers)
# print(response.status_code)
# print(response.text)
# print(response.headers)

#delete contact
"""
url="https://thinking-tester-contact-list.herokuapp.com/contacts/"
headers ={'Authorization':token}
response=requests.delete(url,headers=headers)
print(response.status_code)
print(response.text)
print(response.headers)
"""

#get contactlist
url="https://thinking-tester-contact-list.herokuapp.com/contacts"
headers ={'Authorization':token}
response=requests.get(url,headers=headers)
print(response.status_code)
print(response.text)
print(response.headers)