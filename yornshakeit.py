import os
import sys
import json
import time
import base64
import getpass
import sqlite3
import datetime
import requests

log = open("{}.log".format(sys.argv[1]), "a")



if sys.argv[1] == "fabiobaiao":
    MyVodafoneUsername = "fabiobaiao7@hotmail.com"
    MyVodafonePassword = ""
elif sys.argv[1] == "tacotaco":
    MyVodafoneUsername = ""
    MyVodafonePassword = ""
elif sys.argv[1] == "lfernandes":
    MyVodafoneUsername = ""
    MyVodafonePassword = ""
# else:
#     MyVodafoneUsername = input("Email/Nº telemóvel: ")
#     MyVodafonePassword = getpass.getpass()


response = requests.post("https://mw.my.vodafone.pt/RESTv2/authcredentials.json", data={"MyVodafoneUsername": MyVodafoneUsername, "MyVodafonePassword": MyVodafonePassword})
log.write("{},\n".format(json.dumps({"url": "https://mw.my.vodafone.pt/RESTv2/authcredentials.json", "data": {"MyVodafoneUsername": MyVodafoneUsername, "MyVodafonePassword": MyVodafonePassword}, "response": response.text})))

sessionId = json.loads(response.text)["sessionId"]

requests.get("https://mw.my.vodafone.pt/RESTv2/retrievemainuserdata.json", headers={"X-mCare-Session": sessionId, "x-mcare-device": "android"})

response = requests.get("https://mw.my.vodafone.pt/MSSOLogin.get", headers={"X-mCare-Session": sessionId})
log.write("{},\n".format(json.dumps({"url": "https://mw.my.vodafone.pt/MSSOLogin.get", "headers": {"X-mCare-Session": sessionId}, "response": response.text})))

for headerToSend in json.loads(response.text)["headersToSend"]:
    if "x-sm-identity" in headerToSend["value"]:
        x_sm_identity = headerToSend["value"].split("; ")[0].split("=")[1]
    elif "ObSSOCookie" in headerToSend["value"]:
        ObSSOCookie = headerToSend["value"].split("; ")[0].split("=")[1] # + "="

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
    
# response = requests.get("https://yornshakeit.vodafone.pt/rest/user/cat/{}".format(str(base64.b64encode(msisdn.encode("ascii")), "ascii")), cookies={'x-sm-identity': x_sm_identity["value"], "ObSSOCookie": ObSSOCookie["value"]})
# print(response.text)

    response = requests.post("https://yornshakeit.vodafone.pt/rest/cards/exchange/friend/start", cookies={'x-sm-identity': x_sm_identity, "ObSSOCookie": ObSSOCookie}, data={"friend": msisdn})
    result = json.loads(response.text)["result"]
    while result == "ERROR_GENERIC":
        print("ERROR_GENERIC", end="")
        input()
        response = requests.post("https://yornshakeit.vodafone.pt/rest/cards/exchange/friend/start", cookies={'x-sm-identity': x_sm_identity, "ObSSOCookie": ObSSOCookie}, data={"friend": msisdn})
        result = json.loads(response.text)["result"]
    first = True
    while result == "CONNECT_PENDING":
        if first:
            first = False
            print("A emparelhar", end="", flush=True)
        else: 
            print(".", end="", flush=True)
        time.sleep(5)
        response = requests.get("https://yornshakeit.vodafone.pt/rest/cards/exchange/friend/status", cookies={'x-sm-identity': x_sm_identity, "ObSSOCookie": ObSSOCookie}, params={"friend": msisdn})
        result = json.loads(response.text)["result"]
    if not first:
        print()
    if result == "ERROR_NO_CARDS":
        print("Não tens nenhuma carta que possas trocar")
        continue
    # CONNECT_OK
    cards = {}
    for tradeableCard in json.loads(response.text)["tradeableCards"]:
        cards[tradeableCard["cardPosition"]] = {"cardId": tradeableCard["cardId"], "numberOfRepeats": tradeableCard["numberOfRepeats"]}
    print("Cartas que podes trocar: ", end="")
    first = True
    for card in cards:
        if not first:
            print(", ", end="")
        first = False
        if cards[card]["numberOfRepeats"] > 1:
            print("{} (x{})".format(card, cards[card]["numberOfRepeats"]), end="")
        else:
            print("{}".format(card), end="")
    print()
    card = int(input("Seleciona uma: "))
    response = requests.post("https://yornshakeit.vodafone.pt/rest/cards/exchange/friend/selectcard", cookies={'x-sm-identity': x_sm_identity, "ObSSOCookie": ObSSOCookie}, data={"friend": msisdn, "cardId": cards[card]["cardId"]})
    result = json.loads(response.text)["result"]
    while result == "CARD_SELECT_PENDING":
        time.sleep(5)
        response = requests.post("https://yornshakeit.vodafone.pt/rest/cards/exchange/friend/selectcard", cookies={'x-sm-identity': x_sm_identity, "ObSSOCookie": ObSSOCookie}, data={"friend": msisdn, "cardId": cards[card]["cardId"]})
        result = json.loads(response.text)["result"]
    # CARD_SELECT_OK
    input("Confirmar: ")
    receivedCardId = json.loads(response.text)["receivedCard"]["id"]
    receivedCardName = json.loads(response.text)["receivedCard"]["name"]
    response = requests.post("https://yornshakeit.vodafone.pt/rest/cards/exchange/friend/confirm", cookies={'x-sm-identity': x_sm_identity, "ObSSOCookie": ObSSOCookie}, data={"friend": msisdn})
    result = json.loads(response.text)["result"]
    while result == "CARD_TRADE_PENDING":
        time.sleep(5)
        response = requests.get("https://yornshakeit.vodafone.pt/rest/cards/exchange/friend/status", cookies={'x-sm-identity': x_sm_identity, "ObSSOCookie": ObSSOCookie}, params={"friend": msisdn})
        result = json.loads(response.text)["result"]
    # CARD_TRADE_OK
    response = requests.post("https://yornshakeit.vodafone.pt/rest/cards/guessname", cookies={'x-sm-identity': x_sm_identity, "ObSSOCookie": ObSSOCookie}, json={"cardId": receivedCardId, "cardName": receivedCardName, "time": 10})

if (False):
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

    conn = sqlite3.connect("/home/fabiobaiao/.mozilla/firefox/nz74xu23.default-release/cookies.sqlite")

    conn.execute("delete from moz_cookies where name = 'x-sm-identity' and host = '{}' and path = '{}';".format(ObSSOCookie["host"], x_sm_identity["path"]))
    conn.execute("delete from moz_cookies where name = 'ObSSOCookie' and host = '{}' and path = '{}';".format(ObSSOCookie["host"], ObSSOCookie["path"]))

    now = int((datetime.datetime.utcnow() - datetime.datetime.utcfromtimestamp(0)).total_seconds() * 1e6)

    conn.execute("insert into moz_cookies (name, value, host, path, expiry, creationTime) values ('x-sm-identity', '{}', '{}', '{}', {}, {})".format(x_sm_identity["value"], ObSSOCookie["host"], x_sm_identity["path"], x_sm_identity["expiry"], now))
    conn.execute("insert into moz_cookies (name, value, host, path, expiry, creationTime) values ('ObSSOCookie', '{}', '{}', '{}', {}, {})".format(ObSSOCookie["value"], ObSSOCookie["host"], ObSSOCookie["path"], x_sm_identity["expiry"], now))
    conn.commit()
    conn.close()

    os.system("firefox https://yornshakeit.vodafone.pt")
