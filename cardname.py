import os
import sys
import json
import time
import base64
import getpass
import sqlite3
import datetime
import requests

if  sys.argv[1] == "fabiobaiao":
    MyVodafoneUsername = "fabiobaiao7@hotmail.com"
    MyVodafonePassword = ""
elif sys.argv[1] == "tacotaco":
    MyVodafoneUsername = ""
    MyVodafonePassword = ""
elif sys.argv[1] == "lfernandes":
    MyVodafoneUsername = ""
    MyVodafonePassword = ""
else:
    MyVodafoneUsername = input("Email/Nº telemóvel: ")
    MyVodafonePassword = getpass.getpass()


response = requests.post("https://mw.my.vodafone.pt/RESTv2/authcredentials.json", data={"MyVodafoneUsername": MyVodafoneUsername, "MyVodafonePassword": MyVodafonePassword})

sessionId = json.loads(response.text)["sessionId"]

requests.get("https://mw.my.vodafone.pt/RESTv2/retrievemainuserdata.json", headers={"X-mCare-Session": sessionId, "x-mcare-device": "android"})

response = requests.get("https://mw.my.vodafone.pt/MSSOLogin.get", headers={"X-mCare-Session": sessionId})

headersToSend = json.loads(response.text)["headersToSend"]

for headerToSend in headersToSend:
    if headerToSend["key"] == "Set-Cookie":
        if "x-sm-identity" in headerToSend["value"]:
            x_sm_identity = {}
            for pair in headerToSend["value"].split("; "):
                pair = pair.split("=")
                if "x-sm-identity" in pair[0]:
                    x_sm_identity["value"] = pair[1]
                elif "Domain" in pair[0]:
                    x_sm_identity["host"] = pair[1]
                elif "Expires" in pair[0]:
                    x_sm_identity["expiry"] = int((datetime.datetime.strptime(pair[1], "%a, %d-%b-%Y %H:%M:%S %Z") - datetime.datetime.utcfromtimestamp(0)).total_seconds())
                elif "Path" in pair[0]:
                    x_sm_identity["path"] = pair[1]
        elif "ObSSOCookie" in headerToSend["value"]:
            ObSSOCookie = {}
            for pair in headerToSend["value"].split("; "):
                pair = pair.split("=")
                if "ObSSOCookie" in pair[0]:
                    ObSSOCookie["value"] = pair[1]
                elif "Domain" in pair[0]:
                    ObSSOCookie["host"] = pair[1]
                elif "Path" in pair[0]:
                    ObSSOCookie["path"] = pair[1]

# response = requests.get("https://yornshakeit.vodafone.pt/rest/cards/exchange/initialize", cookies={'x-sm-identity': x_sm_identity["value"], "ObSSOCookie": ObSSOCookie["value"]})
# print(response.text)

# response = requests.get("https://yornshakeit.vodafone.pt/rest/cards/exchange/friend/info", cookies={'x-sm-identity': x_sm_identity["value"], "ObSSOCookie": ObSSOCookie["value"]})
# print(response.text)

while(True):
    msisdn = input("Escolhe o amigo com quem queres trocar cartas: ")

    if msisdn == "fabiobaiao":
        msisdn = "918587695"
    elif msisdn == "tacotaco":
        msisdn = "912625318"
    elif msisdn == "lfernandes":
        msisdn = "916441719"

    receivedCardId = 1306
    receivedCardName = "SUMO"

    response = requests.post("https://yornshakeit.vodafone.pt/rest/cards/guessname", cookies={'x-sm-identity': x_sm_identity["value"], "ObSSOCookie": ObSSOCookie["value"]}, json={"cardId": receivedCardId, "cardName": receivedCardName, "time": 10})
    print(response.text)