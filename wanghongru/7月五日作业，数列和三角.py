a = 1
b = 1
print(a)
list = [a,b]
for i in range(18):
    c = list[i]+list[i+1]
    list.append(c)

for j in range(len(list)):
    print(list[j]," ", end="")

print()

a = 1

trangle = [[1],[1,1]]
for i in range(5):
    list = [1]
    for j in range(len(trangle[i+1])-1):
        list.append(trangle[i+1][j]+trangle[i+1][j+1])
    list.append(1)
    trangle.extend([list.copy()])

for i in range(len(trangle)):
    for j in range(len(trangle[i])):
        print(trangle[i][j]," ",end="")
    print()
