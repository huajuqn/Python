
from random import *
def yandoor():#改变的概率为
    sum=0
    c=0
    while True:
            a = randint(1,3)#选的门
            b = randint(1,3)#羊所在的位置
            while True : #主持人选一个有羊的门
                    hu=choice(range(1,4))
                    if hu not in [a,b] :
                            break
            while True:#互动者改变选择
                    i=choice(range(1,4))
                    if i not in [b,hu]:
                            b=i
                            break
            c+=1
            if b==a:#选中的次数
                    sum+=1
            if c==10000:
                    break
	#print(a,b)
    return sum/c
def yandoor2():#不改变的概率为
    sum=0
    c=0
    while True:
            a = randint(1,3)
            b = randint(1,3)
            c+=1
            if a==b:
                    sum+=1
            if c==10000:
                    break
    return sum/c
print("不改变的概率为:",yandoor2(),",改变的概率为:",yandoor(),yandoor2()+yandoor())

