StaMat=float(input("请输入初始质量："))
for i in range(1,10):
     ErthMat=StaMat+i*0.5
     MoonMat=ErthMat*0.165
     print("第{}年地球的体重为{:.2f}，月球的体重为{:.2f}".format(i,ErthMat,MoonMat))
