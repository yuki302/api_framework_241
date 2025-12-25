import requests
import json

g_var = {}

def test_get_token():
    resp = requests.request(
        method = 'GET',
        url = 'https://api.weixin.qq.com/cgi-bin/token',
        params={
            "grant_type": "client_credential",
            "appid": "wx4816c558b344167f",
            "secret": "0a8733805147ac4d5d550fd8746394df"
        }
    )
    assert resp.status_code == 200
    access_token = resp.json()['access_token']
    assert access_token !=""
    g_var['access_token'] = access_token
    print('access_token:', g_var)

def test_get_tags():
    resp = requests.request(
        method='GET',
        url='https://api.weixin.qq.com/cgi-bin/tags/get',
        params = {
            "access_token":g_var['access_token'],
        }
    )
    print('access_token:', g_var)

    assert resp.status_code == 200

    # tags = resp.json()['tags']
    #
    # tag_id = tags[0]['id']
    #
    # assert tag_id == 2

def test_create_tags():
    resp = requests.request(
        method='POST',
        url='https://api.weixin.qq.com/cgi-bin/tags/create',
        params = {
            "access_token":g_var['access_token'],
        },
        json={"tag":{"name":"广西"}}
    )

    assert resp.status_code == 200

    # tag = resp.json()['tag']

    # assert tag
    #
    # tag_id = tag[0]['id']
    #
    # assert tag_id == 2