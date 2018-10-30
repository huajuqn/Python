#e7.2DrawSevenSegDisplay.py
import turtle, datetime
ls=["red","blue","pink","#685632","#eeaeee","yellow","#f1e5e8","#aaf2e5","#7D2BBC","#96A5A2","#E26720"]
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()    
    turtle.right(90)
def colorL(b): #颜色改变
    turtle.pencolor(ls[b])
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20) 
def drawDate(date):
    c=0
    for i in date:
        if i == '-':
            colorL(c)
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.fd(40)
            c+=1
        elif i == '=':
            colorL(c)
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.fd(40)
            c+=1
        elif i == '+':
            colorL(c)
            turtle.write('日',font=("Arial", 18, "normal"))
            c+=1
        else:
            colorL(c)
            drawDigit(eval(i))
            c+=1
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    turtle.hideturtle()
main() 
