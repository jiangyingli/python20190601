#求斐波那契数列前20项
a1=1
a2=1
print(a1)
print(a2)
for i in range (18):
    a3=a1+a2
    a1=a2
    a2=a3
    print(a3)


