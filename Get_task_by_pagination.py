import requests
from requests.structures import CaseInsensitiveDict


def test_get_task_by_pagination():
    endpoint = "https://api-nodejs-todolist.herokuapp.com/task?limit=12&skip=10"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjFkYTVhZGViZmQ2MTAwMTc0NTE5NmUiLCJpYXQiOjE2NDYxMTY5MDJ9.LyMvlZjexcYq_bUPDdFxZO93LVxlmZa4HAIssP8dfds"
    response = requests.get(url=endpoint, headers=headers)
    response_body = response.json()
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    print(response_body)
    if response.ok:
        print("Task printed based on pagination successfully!")
        print(response.text)
    else:
        print("Something went wrong!")
