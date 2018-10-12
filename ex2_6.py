from turtle import  *
penup()
fd(-100)
seth(-90)
fd(100)
pendown()
seth(0)
i = 0
#fillcolor("#eeaeee")
#begin_fill()
while True:
    i+=1
    penup()
    fd(50)
    pendown()
    fd(200)
    penup()
    if i <4:
     fd(50)
    left(90)
    if i >=4:
        seth(-90)
        break
#end_fill()  
