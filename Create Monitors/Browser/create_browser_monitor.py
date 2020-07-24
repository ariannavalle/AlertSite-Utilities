import requests 
import json
import sys

baseUrl = 'https://api.alertsite.com/api/v3' 
username = sys.argv[1]
password = sys.argv[2]

def getAccessToken(username,password):
    payload = {'username': username, 'password': password}
    r = requests.post(baseUrl + '/access-tokens', data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    if r.status_code != 200:
        print("Invalid Authentication Request", r)
        exit()

    token = r.json()['access_token']
    return token

def createWebMonitor():
    token = getAccessToken(username,password)
    header = {'Authorization': 'Bearer ' + token}
    payload = {
    "alert_note": "monitor down",
    "billing_plancode": "UBM - A/A",
    "browser_type": sys.argv[3],
    "enabled": True,
    "home_location": 10,
    "interval": 1,
    "locations": [
        {"id": 10}, 
        {"id": 67},
        {"id": 62},
        {"id": 19},
        {"id": 71},
        {"id": 75}
    ],
    "name": "AUT - US-WEST001 ",
    "note": "SaaS Customer - US West (Oregon) Region",
    "type": "dejaclick",
    "url": "http://the-internet.herokuapp.com/",
    "transaction_steps": 1,
    "step_timeout":30
}

    r = requests.post(baseUrl + '/monitors/dejaclick', data=json.dumps(payload), headers=header)
    r = r.json()
    if "errors" in r:
       print("Invalid Request", r)
    else: 
        print(r)

createWebMonitor()