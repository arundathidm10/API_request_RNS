import requests

def test_get_list_of_user():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200



import json

import requests
def test_post_new_user():
    # reading json data from datajson file
    mydata = open('data.json', 'r').read()
    # Deserialize
    response = requests.post("https://reqres.in/api/users", data=json.loads(mydata))
    print(response.status_code)
    print(response)
    print(response.json())
    # assert data
    assert response.json()['job'] == "Engineer", "Is not matching the job!"