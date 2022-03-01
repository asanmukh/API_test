import requests
from requests.structures import CaseInsensitiveDict


def test_upload_image():

    endpoint = ("https://api-nodejs-todolist.herokuapp.com/user/me/avatar")
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjFkYjJkOGVjNjkzNTAwMTdhYTU1ZWEiLCJpYXQiOjE2NDYxMTc3MzZ9._FO82ygE85RbgN6LdtaW9KOAqH4Fbk75qBP0mFzD208"
    response = requests.put(url=endpoint, headers=headers)
    file = open("/Users/asanmukh/Desktop/Screenshot 2022-01-24 at 4.22.51 PM.png", "rb")
    response = requests.post(endpoint, files={"form_field_name": file})
    if response.ok:
        print("Upload completed successfully!")
        print(response.text)
    else:
        print("Something went wrong!")