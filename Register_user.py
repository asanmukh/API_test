import requests

def test_user_register():
    payload = {
        "name": "Muhammad Nur",
        "email": "aka.nurali43@gmail.com",
        "password": "12345678",
        "age": 20
    }
    endpoint = ("https://api-nodejs-todolist.herokuapp.com/user/register")
    response = requests.post(url=endpoint, json=payload)
    response_body = response.json()
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.status_code == 201
    print(response.status_code)
    print(response.text)
    print(response_body)

    #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjFkYjJkOGVjNjkzNTAwMTdhYTU1ZWEiLCJpYXQiOjE2NDYxMTM0OTZ9.5ve-spc5wb7JIvIpyIkxC7SeWutQ6oIGuXAMZMunSTY