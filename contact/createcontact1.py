import requests
from faker import Faker

def generateEmail():
    fake = Faker()
    return fake.email()

emailgen = generateEmail()
#add user
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
#capturing a token
logintoken = response.json().get('token')
print(f'token add user:{logintoken}')


#add contact
url = "https://thinking-tester-contact-list.herokuapp.com/contacts"
data = {
    "firstName": "purple",
    "lastName": "pink",
    "birthdate": "1971-10-10",
    "email": emailgen,
    "phone": "8086955525",
    "street1": "1 Main St.",
    "street2": "Apartment A",
    "city": "town",
    "stateProvince": "KS",
    "postalCode": "123452",
    "country": "india"
}
headers = {'Authorization':logintoken}
response = requests.post(url,json=data,headers=headers)
#print the response
print(response.status_code)
response_json = response.json()
print(response_json)





