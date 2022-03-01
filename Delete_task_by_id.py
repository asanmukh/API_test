import requests
from requests.structures import CaseInsensitiveDict


def test_update_task_by_id():
    endpoint = requests.delete("https://api-nodejs-todolist.herokuapp.com/task/5ddcd1566b55da0017597239")
    # headers = CaseInsensitiveDict()
    # headers["Accept"] = "application/json"
    # headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjFkYjJkOGVjNjkzNTAwMTdhYTU1ZWEiLCJpYXQiOjE2NDYxMTM0OTZ9.5ve-spc5wb7JIvIpyIkxC7SeWutQ6oIGuXAMZMunSTY"
    # response = requests.delete(url=endpoint, headers=headers)
    # response_body = response.json()
    # assert response.headers["content-type"] == "application/json; charset=utf-8"
    # assert response.status_code == 200
    print(endpoint.status_code)
    print(endpoint.text)