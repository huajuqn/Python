a=str(input())
ls=[]
for i in range(len(a)):
    ls.append(a[i])
def f():
    for i in ls:
        if ls.count(i)>1:
            return True
        else:
            return False
if f():
    print("yes")
else:
    print("no")
    
    
