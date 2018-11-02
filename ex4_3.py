a,b=eval(input("请输入第一个数：")),eval(input("请输入第二个数："))
if a<b:
    m,n,=b,a
else:
    m,n=a,b
r=m%n
while True:
    if r !=0:
        m=n
        n=r
        r=m%n
    else:
        print("最大公约数为{}，最小公倍数为{}".format(n,a*b/n))
        break
