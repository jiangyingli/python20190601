#斐波那契数列
a=1
b=1
sum=0
for i in range(20):
    c=b
    b=a
    a=b+c
    sum=sum+c
    print(sum,end=" ")

#杨辉三角
n=int(input("请输入要打的行数\n"))
list1 =[]
for i in range(n):
    list1.append(i)
list=[]
for j in range(n):
    list.append(list1.copy())


for j in range(n):
    for i in range(j+1):
        if(j==0):
            list[0][0]=1
        elif(j!=0):
            if(i==0):
                list[j][0]=1
            elif(i!=0):
                if ((i+1)<=(j+2)/2):
                    list[j][i]=list[j-1][i-1]+list[j-1][i]
                elif((i+1)>(j+1)/2):
                    list[j][i]=list[j][j-i]
        print(str(list[j][i])+str(" "),end="")
    print()
