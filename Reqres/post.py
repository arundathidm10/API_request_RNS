# import requests
#
#
# url = "https://reqres.in/api/users"
# data = {
#     "name": "Rakesh",
#     "job": "leader"
# }
# response = requests.post(url,data=data)
#
#
# print(response.status_code)
# print(response.json())
# print(response.cookies)
# print(response.headers)
#
#
# for name in response.headers:
#     value = response.headers[name]
#     print(name, value)
# #assert response.headers["Content-Length"] == 82
