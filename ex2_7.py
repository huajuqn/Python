from turtle import  *
setup(800,400)
seth(30)
while True:
    fd(300)
    right(120)
    if abs(pos())<1:
        break
penup()
seth(0)
fd(346.4)
pendown()
seth(150)
i=0
while True:
    i+=1
    fd(300)
    left(120)
    if i>2:
        break

