import requests

def test_user_login():
    payload = {
        "email": "aka.nurali43@gmail.com",
        "password": "12345678",
    }
    endpoint = ("https://api-nodejs-todolist.herokuapp.com/user/login")
    response = requests.post(url=endpoint, json=payload)
    response_body = response.json()
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    print(response_body)
