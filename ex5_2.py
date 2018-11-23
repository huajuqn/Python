def isOdd(a):
    if a % 2 ==0 :
        return False
    else:
        return True
def main():
    while True:
        b= eval(input("请输入一个整数："))
        if isOdd(b):
            print(b,"是奇数")
        else:
            print(b,"是偶数")
main()
