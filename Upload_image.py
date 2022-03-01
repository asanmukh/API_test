import requests

def test_uploade_image():

    endpoint = ("https://api-nodejs-todolist.herokuapp.com/user/me/avatar")
    test_file = open("/Users/asanmukh/Desktop/Screenshot 2022-01-24 at 4.22.51 PM.png", "rb")
    test_response = requests.post(endpoint, files={"form_field_name": test_file})
    if test_response.ok:
        print("Upload completed successfully!")
        print(test_response.text)
    else:
        print("Something went wrong!")