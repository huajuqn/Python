import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
ls=["blue","red","yellow","gold"]
for i in ls:
    turtle.pencolor(i)
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.pencolor("#eeaeee")
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.pencolor("#f8e1e5")
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
