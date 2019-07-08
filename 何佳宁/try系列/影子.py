list=[]
for i in range (20):
    list.append(i)
a=1
b=1
n=0
while (0<=n<=19):
    c=b
    b=a
    a=b+c
    list[n]=c
    n=n+1
print(list)
a=1
b=1
sum=0
for i in range(20):
    c=b
    b=a
    a=b+c
    sum=sum+c
    print(sum,end=" ")
