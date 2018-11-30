a=str(input())
ls=[]
for i in range(len(a)):
    ls.append(a[i])
def f():
    cot=set(ls)
    if len(ls) != len(cot):
        return True
    else:
        return False
if f():
    print("yes")
else:
    print("no")
