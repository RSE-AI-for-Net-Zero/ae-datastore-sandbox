import requests

BASEURL = "https://127.0.0.1:5000/api"

r = requests.post(f"{BASEURL}/login",
                  json = {"username": "user_1",
                          "password": "secret123"},
                  verify = False)

csrf_token = r.cookies["csrftoken"]

r = requests.post(f"{BASEURL}/logout",
                  headers = {"X-CSRF-Token": csrf_token},
                  verify = False)
