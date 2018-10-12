MoneyStr= input("请输入带有符号的金钱数(人民币用R或r表示)：")
if  MoneyStr[-1] in ['$'] :
    R = eval(MoneyStr[0:-1])*6.928
    print("转换后的温度是{:.2f}¥".format(R))
elif    MoneyStr[-1] in ['R','r']:
    D=eval(MoneyStr[0:-1])/6.928
    print("转换后的温度是{:.2f}$".format(D))
else:
    print("输入格式错误")
