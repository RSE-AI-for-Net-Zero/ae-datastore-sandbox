import requests

BASEURL = "https://127.0.0.1:5000/api"

r = requests.post(f"{BASEURL}/login",
                  json = {"username": "user_1",
                          "password": "secret123"},
                  verify = False)

cookies = r.cookies
csrftoken = cookies["csrftoken"]
session = cookies["session"]
                    
#breakpoint()


r = requests.post(f"{BASEURL}/records",
                  cookies = dict(session=session, csrftoken=csrftoken),
                  headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                  verify = False)

#r = requests.get(f"{BASEURL}/records",
#                 headers = {"X-CSRF-Token": csrf_token},
#                 verify = False)


#r = requests.post(f"{BASEURL}/logout",
#                  headers = {"X-CSRF-Token": csrf_token},
#                  verify = False)
