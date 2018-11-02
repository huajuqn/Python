from turtle import *
a=0
l=3
seth(90)
fd(l)
seth(180)
while True:
    l+=3
    fd(l)
    left(90)
    fd(l)
    left(90)
    a+=1
    if a==51:
        break
    
