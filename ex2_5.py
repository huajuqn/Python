from turtle import  *
while True:
    fd(300)
    left(120)
    if abs(pos())<1:
        break
seth(60)
fd(150)
seth(0)
i=0
while i <3:
    fd(150)
    right(120)
    i+=1
