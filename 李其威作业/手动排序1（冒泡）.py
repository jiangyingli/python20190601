list=[3,95,1,6,1,7,85,7,456,2]
for j in range (len(list)-1):
    for i in range (len(list)-1):
        if (list[i]>list[i+1]):
            list[i] , list[i+1] =list[i+1] , list[i]
print(list)