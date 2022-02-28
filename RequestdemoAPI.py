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

    headers = {"Authorization": "Bearer Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjQ1Nzg4NDY4LCJqdGkiOiJiYWI4Y2QyNC1hZDU2LTQyNTgtOGNmYi03Y2RiNDg2YmM4ZjMiLCJuYmYiOjE2NDU3ODg0NjgsInR5cGUiOiJhY2Nlc3MiLCJzdWIiOiI2MjE4Yjk0NjllYWY2ZDY4OTg0MWIzYWQiLCJleHAiOjE2NDU3ODkzNjh9.oBUe8WDUa__0mltOeJpQVmQVvawEJaGqfri5qtbIaIE"}
    response = requests.get("https://hbs-ob-stage.herokuapp.com/protected_test")
    print(response.status_code)

