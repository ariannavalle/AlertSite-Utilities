import requests
import json
import sys

baseUrl = 'https://api.alertsite.com/api/v3'
username = sys.argv[1]
password = sys.argv[2]


def getAccessToken(username, password):
    payload = {'username': username, 'password': password}
    r = requests.post(baseUrl + '/access-tokens', data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    if r.status_code != 200:
        print("Invalid Authentication Request", r)
        exit()

    token = r.json()['access_token']
    return token

def createWebMonitor():
    token = getAccessToken(username, password)
    header = {'Authorization': 'Bearer ' + token}
    payload = {
        "billing_plancode": "UBM - A/A",
        "name": "AUT - US-WEST001",
        "site_type": "website",
        "url": "http://the-internet.herokuapp.com/",
        "interval": 15,
        "locations": [{
            "id": 20 
        }],
        "mode": "Primary"
    }

    r = requests.post(baseUrl + '/monitors/website',
                      data=json.dumps(payload), headers=header)
    r = r.json()
    if "errors" in r:
        print("Invalid Request", r)
    else:
        print(r)


createWebMonitor()