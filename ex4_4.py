from random import *

NzNum=randint(0,100)
a=0
while True:
    WtNum=eval(input("请输入一个0—100之间的整数："))
    if WtNum > NzNum :
        a+=1
        print("遗憾，太大了")
    elif WtNum < NzNum :
        a+=1
        print("遗憾，太小了")
    else:
        a+=1
        print("恭喜第",a,"次答对了")
        break
