
s=2
n=12
current=0
previous=0
dict={}
for x in range(s,n):
    bin1=bin(x)
    print(bin1)
    for y in range(2,len(bin1)-1):
        current=bin1[y]
        previous=bin1[y+1]
        if current=="1" and previous=="1":
            dict[x]=True
            break
        else:
            dict[x]=False
print(dict)
