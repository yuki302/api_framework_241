import requests

resp = requests.request('get', 'https://www.baidu.com/beifan.html')

print(resp.status_code, resp.reason)

print(resp.headers)




requests.post(
    "https://www.baidu.com/upload",
    params = {
        "dir":"user_home"
    },

    headers = {
        "name":"beifan"
    },
    data = {
        "name":"beifan"
    },
    json = {
        "age":[1,1,2]
    },
    files = {
      "file": open("conftest.py", "rb")
    },
)