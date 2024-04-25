#This script is to solve mus1c in picoCTF

#https://codewithrockstar.com/online
#Run the lyrics file at the link destination.
#After passing the resulting decimal number to "arry", run the script.

arry = [114,114,114,111,99,107,110,114,110,48,49,49,51,114]

for i in arry:
    print(chr(i),end="")
