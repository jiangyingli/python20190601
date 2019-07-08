
a = 1
b = 1
list = [a,b]
for i in range(21):
    c = list[i]+list[i+1]
    list.append(c)

c = 0
for i in range(1,21):
    c = c+(list[i+1]/list[i])

print(c)

a = int(input("年份"))
b = int(input("月份"))
c = int(input("日子"))
def f(p,q):
    d = 0
    list = [1,3,5,7,8,10,12]
    for i in range(1,p):
        if i in list:
            d = d+31
        elif i == 2:
            d = d+29
        else:
            d = d+30
    d = d+q
    print("闰年")
    print(d)

def g(p,q):
    d = 0
    list = [1,3,5,7,8,10,12]
    for i in range(1,p):
        if i in list:
            d = d+31
        elif i == 2:
            d = d+28
        else:
            d = d+30
    d = d+q
    print("平年")
    print(d)

if a%4 == 0:
    if a%100 != 0:
        f(b,c)
    elif a%400 == 0:
        f(b,c)
    else:
        g(b,c)
else:
    g(b,c)



b = int(input("输入待分解的正整数"))
a = b
list = []
for i in range(2,a):
    for j in range(2,a):
        if a%i == 0:
            c = 0
            for j in range(2,i):
                if i%j == 0:
                    c = c+1
            if c == 0:
                list.append(i)
                a = a//i
print(b,"=",end = "")
for i in range(len(list)):
    if i != len(list)-1:
        print(list[i],"*",end="")
    elif i == len(list)-1:
        print(list[i])

