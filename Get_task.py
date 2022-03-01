import requests
from requests.structures import CaseInsensitiveDict


def test_add_task():
    payload = {
        "description": "reading book"
    }
    endpoint = "https://api-nodejs-todolist.herokuapp.com/task"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjFkYTVhZGViZmQ2MTAwMTc0NTE5NmUiLCJpYXQiOjE2NDYxMTY5MDJ9.LyMvlZjexcYq_bUPDdFxZO93LVxlmZa4HAIssP8dfds"
    response = requests.get(url=endpoint, json=payload,headers=headers)
    response_body = response.json()
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    print(response_body)
    if response.ok:
        print("Task added successfully!")
        print(response.text)
    else:
        print("Something went wrong!")