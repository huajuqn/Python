from random import *

NzNum=randint(0,100)
a=0
while True:
    try:
        WtNum=int(input("请输入一个0—100之间的整数："))
    except:
        print("输入错误")
        break

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
    
