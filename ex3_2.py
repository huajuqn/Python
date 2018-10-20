dayup=1
a=0
for i in range(1,366):
    a=a+1
    if a <=3 :
        dayup=dayup
    else:
        dayup=dayup*(1+0.01)
        if a == 7:
            a=0
    #print(dayup,i)
print(dayup)

