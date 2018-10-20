def dayUP(res):
    dayup=1
    a=0
    b=0
    for i in range(1,366):
        a=a+1
        b=b+1
        if  b%(res+1) !=0:
    
           if a <=3 :
                dayup=dayup
           else:
                dayup=dayup*(1+0.01)
                if a == 7:
                    a=0
        elif b%(res+1) ==0:
            b=0
            a=0
        #print(dayup,i,a,b)
    return dayup

print("每第50天休息：",dayUP(49))
