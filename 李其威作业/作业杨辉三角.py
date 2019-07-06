a=int(input("想要打印几行呢"))

list1=[]
list=[]
for i in range(a*3):
    list1.append(0)
for i in range(a*3):

    list.append(list1.copy())

for i in range (a):
    list[i][0]=1
    list[i][i]=1
for i in range(a):
    for j in range(i):
        list[i+1][j+1]=list[i][j]+list[i][j+1]
for i in range (a*2):
    for j in range (a*2):
        if (list[i][j]!=0):
            print(list[i][j],end=" ")
        else:
            break
    print()


