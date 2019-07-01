list=[7,68,28,39,71,93,27,18,938,182,345,87,623,6789,4321,76543,7654,654,6543,432,432,765,987,765,654,343,254,3543,43,23,2,21,32,34,35,45,4]
for j in range (len(list)-1):
    for i in range (len(list)-1):
        if (list[i+1]<list[i]):
            list[i],list[i+1]=list[i+1],list[i]
print(list)