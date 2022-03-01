import requests
from requests.structures import CaseInsensitiveDict


def test_delete_image():
    endpoint = ("https://api-nodejs-todolist.herokuapp.com/user/me/avatar")
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjFkYjJkOGVjNjkzNTAwMTdhYTU1ZWEiLCJpYXQiOjE2NDYxMTM0OTZ9.5ve-spc5wb7JIvIpyIkxC7SeWutQ6oIGuXAMZMunSTY"
    response = requests.get(url=endpoint, headers=headers)
    response = requests.delete(url=endpoint, headers=headers)
    response_body = response.json()
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.status_code == 200
    print(response.status_code)
    print(response_body)
    if response.ok:
        print("image deleted successfully!")
        print(response.text)
    else:
        print("Something went wrong!")