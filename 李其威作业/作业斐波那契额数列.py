a=1
b=1
c=0
print(a,end=" ")
print(b,end=" ")
for i in range(18):
    c=a+b
    a=b
    b=c
    print(b,end=" ")
