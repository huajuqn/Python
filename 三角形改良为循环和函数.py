import turtle as t
def drawTriangle(e,direct=120):
    t.seth(0)
    for i in range(3):
        t.fd(e)
        t.left(direct)
    t.right(direct)
drawTriangle(200)
t.penup()
t.bk(100)
t.pendown()
drawTriangle(100,240)
t.seth(0)
