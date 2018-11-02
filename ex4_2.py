a=input("")
zm,kg,sz,other=0,0,0,0
for i in a:
    if "a"<=i<="z" or "A"<=i<="Z":
        zm+=1
    elif i == " ":
        kg+=1
    elif "0"<=i<="9":
        sz+=1
    else:
        other+=1
print("字母有",zm,"数字有",sz,"空格有",kg,"其他字符有",other)
        
        
    
