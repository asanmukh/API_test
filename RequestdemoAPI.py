import requests

def test_check_status():
    response = requests.get("https://hbs-ob-stage.herokuapp.com/status")
    assert response.headers["content-type"] == "application/json"
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    print(response.json())

def test_create_user():
    payload = {
        "name": "user456567236724",
        "phone": "+91xxxxxxxx",
        "email": "user456567236724@hashedin.com",
        "password": "admin456567236724",
        "otp": 111111
    }
    endpoint ="https://hbs-ob-stage.herokuapp.com/user"
    response = requests.post(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())

def test_get_otp():

    payload = {
        "phone": "+91xxxxxxxx"
    }
    endpoint = ("https://hbs-ob-stage.herokuapp.com/get_register_otp")
    response = requests.post(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())

def test_delete_user():

    payload = {
        "phone": "+91xxxxxxxx",
        "otp": 111111

    }
    endpoint = ("https://hbs-ob-stage.herokuapp.com/user")
    response = requests.delete(url=endpoint, data=payload)
    response_body = response.json()
    print(response.status_code)
    print(response.json())

def test_edit_user():

    payload = {
        "name": "user4565672367",
        "phone": "+91xxxxxxxx",
        "email": "user456567236724@hashedin.com",
        "password": "admin456567236724",
        "otp": 111111
    }
    endpoint = ("https://hbs-ob-stage.herokuapp.com/user")
    response = requests.put(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())

def test_login_otp():

    payload = {
        "phone": "+91xxxxxxxxx"
    }
    endpoint = ("https://hbs-ob-stage.herokuapp.com/get_otp")
    response = requests.post(url=endpoint,data=payload)
    print(response.status_code)
    print(response.json())

def test_authenticate_using_pwd():

    payload = {
        "phone": "+91xxxxxxxx",
        "LoginType": "password",
        "password": "admin456567236724"
    }
    endpoint = ("https://hbs-ob-stage.herokuapp.com/authenticate")
    response = requests.post(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())

def test_authenticate_using_otp():

    payload = {
        "phone": "+91xxxxxxxx",
        "LoginType": "OTP",
        "otp": 111111
    }
    endpoint = ("https://hbs-ob-stage.herokuapp.com/authenticat")
    response = requests.post(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())

def test_login():

    response = requests.get("https://hbs-ob-stage.herokuapp.com/protected_test")
    print(response.status_code)

