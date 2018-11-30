a=str(input())
cont={}
for v in range(len(a)):
    if a[v] in [" ","，"]:
        continue
    else:
        cont[a[v]]=cont.get(a[v],0)+1
items=list(cont.items())
items.sort(key=lambda x:x[1] ,reverse=True)
for i in range(10):
    str,cont=items[i]
    print("{0:<10}{1:>5}".format(str,cont))
