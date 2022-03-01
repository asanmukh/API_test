import requests

def test_user_logout():
    payload = {
        "email": "aka.nurali43@gmail.com",
        "password": "12345678",
    }
    endpoint = ("https://api-nodejs-todolist.herokuapp.com/user/logout")
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjFkYTVhZGViZmQ2MTAwMTc0NTE5NmUiLCJpYXQiOjE2NDYxMTAxMzh9.HR-AQBPLtz4wKEmPgBzINhOrSy7IsLxA0-S7xNG0S0o"}
    response = requests.post(url=endpoint, json=payload)
    response_body = response.json()
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    print(requests.post(endpoint, json=payload, headers=headers).json())
    print(response_body)