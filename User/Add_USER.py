import requests

url="https://thinking-tester-contact-list.herokuapp.com/users/login"
data= {"email":"vjuarez@example.net","password": 1}
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NGM5MzUwMDgyYTFjYzAwMTMwNzYxNGUiLCJpYXQiOjE2OTA5MDc5MDR9.dAbZbPIauNeqBT8hGhJd4kwwbEUzq6Xa-OO7kHow0t4"}
#post request
response=requests.post(url,json=data, headers=headers)
#print statements
print(response.status_code)
print(response.json())


