import requests
from requests.structures import CaseInsensitiveDict

def test_update_user_profile():
    payload = {
        "age": 25
    }
    endpoint = ("https://api-nodejs-todolist.herokuapp.com/user/me")
    response = requests.put(url=endpoint, json=payload)
    response_body = response.json()
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjFkYjJkOGVjNjkzNTAwMTdhYTU1ZWEiLCJpYXQiOjE2NDYxMTc3MzZ9._FO82ygE85RbgN6LdtaW9KOAqH4Fbk75qBP0mFzD208"
    response = requests.put(url=endpoint, headers=headers)
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    print(response_body)