import requests
resp = requests.get("https://reqres.in/api/users?page=2")
json_response = resp.json()
print(json_response['total'])
assert (json_response['total']) == 12,"Does not match the total"
print(json_response['page'])
assert (json_response['page']) == 2,"Does not match the total page"
print(json_response['data'][2]['email'])
assert (json_response['data'][2]['email']) !="abc@gmail.com"
print(json_response['data'][2]['email'])
assert (json_response['data'][4]['email']).endswith("@reqres.in")
assert (json_response['data'][4]['email']).startswith("george")
print(json_response['data'][1]['first_name'])
assert (json_response['data'][1]['first_name']) != None