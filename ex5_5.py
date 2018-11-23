def isPrime(n):
    try:
        for k in range(2,n):
           if n%k == 0:
               return False
        return True
    except:
        print("输入错误，请输入整数")
