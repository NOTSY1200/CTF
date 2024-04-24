#this script is to solve PW Crack5 in picoCTF

import hashlib
import string

hash = "0f4238735916dea9bac9b6a79824223b"

filename = "./dictionary.txt"
a =""
#func1 = hashlib.md5(line.strip().encode()).hexdigest()
try:
    file = open(filename)
    lines = file.readlines()
    for line in lines:
        func1 = hashlib.md5(line.strip().encode()).hexdigest()

        print(line.strip() +"="+ func1)
        if hash == func1:
            a += line

except Exception as e:
    print(e)
finally:
    file.close()


print("collect hash is: " + a)
