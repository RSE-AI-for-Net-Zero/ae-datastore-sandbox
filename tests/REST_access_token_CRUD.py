import os
import sys
import requests
from pprint import pprint

BASEURL = "https://127.0.0.1:5000/api"

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", None)
if not ACCESS_TOKEN:
    sys.exit("ACCESS_TOKEN not set")
                    
#1. Create new record
r = requests.post(f"{BASEURL}/records",
                  params = {"access_token": ACCESS_TOKEN},
                  verify = False)

assert r.status_code == 201 #Created
record = r.json()
record_id = record["id"]

#3. Add some invalid domain metadata to record 
record["metadata"] = {"domain_metadata": {"entry_type": {"longitude": 22.0,
                                                         "laaaatitude": 22.0}}}
r = requests.put(f"{BASEURL}/records/{record_id}/draft",
                 params = {"access_token": ACCESS_TOKEN},
                 verify = False,
                 json = record)

assert r.status_code == 500 #Internal Server Error
#assert "jsonschema.exceptions.ValidationError: {\'longitude\': 22.0, \'laaaatitude\': 22.0} is not valid under any of the given schemas" in r.text


'''
#4. Add required metadata & some valid domain metadata to record
record["metadata"] = {"domain_metadata": {"entry_type": {"longitude": 22.0,
                                                         "latitude": 22.0}}}
r = requests.put(f"{BASEURL}/records/{record_id}/draft",
                 cookies = dict(session=session, csrftoken=csrftoken),
                 headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                 verify = False,
                 json = record)

assert r.status_code == 200 #OK
assert r.json()["metadata"] == {"domain_metadata": {"entry_type": {"longitude": 22.0,
                                                                   "latitude": 22.0}}}
record["metadata"]["creators"] = [
    {
        "person_or_org": {
            "family_name": "Star",
            "given_name": "Patrick",
            "type": "personal",
            "identifiers": [
                {
                    "scheme": "orcid",
                    "identifier": "0000-0002-1825-0097"
            }
            ]
        },
        "role": {
            "id": "contactperson"
    },
        "affiliations": []
    }]

record["metadata"]["resource_type"] = {
    "id": "publication-conferencepaper"
}

record["metadata"]["title"] = "Test record!"
record["metadata"]["publication_date"] = "1970/2016-06"

r = requests.put(f"{BASEURL}/records/{record_id}/draft",
                 cookies = dict(session=session, csrftoken=csrftoken),
                 headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                 verify = False,
                 json = record)

#5. Start file upload
data = [{"key": "spongebob.png"}, {"key": "ideal-hash-trees.pdf"}]

r = requests.post(f"{BASEURL}/records/{record_id}/draft/files",
                  cookies = dict(session=session, csrftoken=csrftoken),
                  headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                  verify = False,
                  json = data)

assert r.status_code == 201 #Created

#6. Upload the files
with open("tests/test_files/spongebob.png", "rb") as f:
    filename = "spongebob.png"
    r = requests.put(f"{BASEURL}/records/{record_id}/draft/files/{filename}/content",
                     cookies = dict(session=session, csrftoken=csrftoken),
                     headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                     verify = False,
                     data = f)

assert r.status_code == 200 #OK
    
with open("tests/test_files/idealhashtrees.pdf", "rb") as f:
    filename = "ideal-hash-trees.pdf"
    r = requests.put(f"{BASEURL}/records/{record_id}/draft/files/{filename}/content",
                     cookies = dict(session=session, csrftoken=csrftoken),
                     headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                     verify = False,
                     data = f)

assert r.status_code == 200 #OK

#7. Complete draft file upload
filename = "spongebob.png"
r = requests.post(f"{BASEURL}/records/{record_id}/draft/files/{filename}/commit",
                  cookies = dict(session=session, csrftoken=csrftoken),
                  headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                  verify = False)

assert r.status_code == 200 #OK

filename = "ideal-hash-trees.pdf"
r = requests.post(f"{BASEURL}/records/{record_id}/draft/files/{filename}/commit",
                  cookies = dict(session=session, csrftoken=csrftoken),
                  headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                  verify = False)

assert r.status_code == 200 #OK

#8. Delete a file
filename = "ideal-hash-trees.pdf"
r = requests.delete(f"{BASEURL}/records/{record_id}/draft/files/{filename}",
                    cookies = dict(session=session, csrftoken=csrftoken),
                    headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                    verify = False)

assert r.status_code == 204 #No Content

#9.  Publish record
#  -- first a

r = requests.post(f"{BASEURL}/records/{record_id}/draft/actions/publish",
                  cookies = dict(session=session, csrftoken=csrftoken),
                  headers = {"X-CSRFToken": csrftoken, "Referer": "https://localhost"},
                  verify = False)

assert r.status_code == 202 #Accepted
'''


