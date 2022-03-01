import requests


def test_update_task_by_id():
    payload = {
        "completed": true
    }
    endpoint = ("https://api-nodejs-todolist.herokuapp.com/task/5ddcd1566b55da0017597239")
    response = requests.put(url=endpoint, json=payload)
    response_body = response.json()
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    print(response_body)