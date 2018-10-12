Temp=eval(input("请输入温度的数字部分："))
Str=input("请输入温度符号：")
if  Str[-1] in ['F','f'] :
    C = int((Temp- 32)/1.8)
    print("转换后的温度是{}C".format(C))
elif    Str[-1] in ['C','c']:
    F =int(1.8*Temp + 32)
    print("转换后的温度是{}F".format(F))
else:
    print("输入格式错误")
