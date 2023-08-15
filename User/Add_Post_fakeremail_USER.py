import requests
from faker import Faker

def generateEmail():
    faker = Faker()
    return faker.email()


def generatepassword():
    faker = Faker()
    return faker.country()



url="https://thinking-tester-contact-list.herokuapp.com/users"
data= {"firstName": "Gary","lastName": "Test","email":generateEmail(),"password": generatepassword()}
#post request
response=requests.post(url,json=data)
#print statements
print(response.status_code)
print(response.json())
ta = response.json().get('token')
print(f'token add user:{ta}')



