import requests
import json

url = "http://api.fbi.com:9225/rest-v2/login/access_token"

payload = json.dumps({
    "email": "bf@qq.com",
    "password": "bf123456"
}
)

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

assert  response.status_code == 200
assert  "access_token" in response.text
