#选择排序问题

list = [120,9,15,100,70,33]
for i in range(len(list)):
    min_idx=i
    for j in range(i+1,len(list)):
        if list[min_idx] > list[j]:
            min_idx=j
    list[i],list[min_idx] =list[min_idx],list[i]
print(list)



#不选特定姓氏同学
import random
times = int(input("请输入要选择几个人，范围是1--2"))
a = input("排除哪个姓氏")
c = input("排除哪个姓氏")
file = open("C:/Users/DREAM/Desktop/点名册.txt", "r+")
lines = file.readlines()
file.close()
for j in range(len(lines)):
        str = lines[j]
        list2 = str.split()
        b = list2[0]
if (b == a):
            lines.remove(str)
elif (b == c):
            lines.remove(str)
elif(b!=a and b!=c):
            ran_lines=random.sample(lines,2)
            print(ran_lines)



















