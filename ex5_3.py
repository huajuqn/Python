def isNum():
    try:
        a=eval(input("请输入一个字符串："))
        return True
    except:
        return False
