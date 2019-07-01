def sum():
    print("总额")
    file = open("C:\\Users\\jkq\\Desktop\\记账本.txt","r")
    str=file.readlines()
    sum=0
    for i in range(len(str)):
        list=str[i].split()
        sum=sum+int(list[3])
    print(sum)
    file.close()
sum()

