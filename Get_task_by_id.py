import requests
from requests.structures import CaseInsensitiveDict


def test_get_task_by_id():
    endpoint = "https://api-nodejs-todolist.herokuapp.com/task/5ddccf7d6b55da001759722f"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjFkYjJkOGVjNjkzNTAwMTdhYTU1ZWEiLCJpYXQiOjE2NDYxMTM0OTZ9.5ve-spc5wb7JIvIpyIkxC7SeWutQ6oIGuXAMZMunSTY"
    response = requests.get(url=endpoint, headers=headers)
    response_body = response.json()
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    print(response_body)
    if response.ok:
        print("Task printed based on id successfully!")
        print(response.text)
    else:
        print("Something went wrong!")
