list=[11,32,43,66,7,2,18]

for j in range(len(list)):
    for i in range(len(list)-1-j):
        if(list[i]>list[i+1]):
            list[i],list[i+1]=list[i+1],list[i]

for j in range(len(list)):
    print(list[j],' ',end='')