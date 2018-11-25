file=input("请输入文件路径")
fo = open(file, "r")
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
fo.close()
#求总分
sum=[0,0,0,0,0]
for i in range(1,6):
    for b in range(1,4):
         sum[i-1]=sum[i-1]+eval(ls[i][b])
    sum[i-1]=str(sum[i-1])
#求最大值，最小值，平均分
max=[0,0,0,""]
min=[100,100,100,""]
avg=[0,0,0,""]
for k in range(1,4):
    for c in range(1,6):
        if eval(ls[c][k])>=max[k-1]:
            max[k-1]=eval(ls[c][k])
        if eval(ls[c][k])<=min[k-1]:
            min[k-1]=eval(ls[c][k])
        avg[k-1]=avg[k-1]+eval(ls[c][k])/(len(ls)-1)
    max[k-1]=str(max[k-1])
    min[k-1]=str(min[k-1])
    avg[k-1]='%.2f'%(avg[k-1])
#把总分写入列表
ls[0].append("总分")
for s in range(1,6):
    ls[s].append(sum[s-1])
#把最大值，最小值，平均分写入列表
fls=["最高分","最低分","平均分"]
max.insert(0,fls[0])
min.insert(0,fls[1])
avg.insert(0,fls[2])
lt=[max,min,avg]
for i in range(3):
    ls.append(lt[i])
#输出csv文件
output = open('score.csv','w',encoding='gbk')
for row in ls:
    rowtxt = '{},{},{},{},{}'.format(row[0],row[1],row[2],row[3],row[4])
    output.write(rowtxt)
    output.write('\n')
output.close()

    

