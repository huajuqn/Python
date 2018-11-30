ch=[]
c="A"
while c<="Z":
    ch.append(c)
    c=chr(ord(c)+1)
c="a"
while c<="z":
    ch.append(c)
    c=chr(ord(c)+1)
c=0
while c<=9:
    ch.append(c)
    c+=1
c=0
from random import *
for i in range(10):
    passWord=[]
    c+=1
    b=0
    while b<8:
        b+=1
        passWord.append(choice(ch))
    
    print("{}{}{}{}{}{}{}{}".format(passWord[0],passWord[1],passWord[2],passWord[3],passWord[4],passWord[5],passWord[6],passWord[7]))
