import requests

r = requests.get("https://reqres.in/api/users?page=2")
sc = r.status_code
print(r.json())
print(r.text)
print(r.url)

if r.url == "https://reqres.in/api/users?page=2":
    print("Match")
else:
    print("Do not match")

#assertion of status
assert r.status_code == 200


print(f'The status code is: {sc}.')
print(f'the content expected: {r.content}')
print(f'This is the expected cookies: {r.cookies}')
print(r.headers)
print(r.ok)


