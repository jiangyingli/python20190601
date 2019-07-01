
list = [11, 2, 334, 5, 67, 8, 1, 46, 3, 109]
for i in range(len(list)):
    a = i
    for j in range(i+1,len(list)):
        if list[a]>list[j]:
            a = j
    list[i],list[a]=list[a],list[i]
for i in range(len(list)):
    print(list[i],"",end = "")
print("\n")
print(list)







namelist = ["冯 家 琛","金 楷 淇","李 聪 聪","何 佳 宁","李 其 威","张 佳 源","王 松 涛","王 小 丫","王 鸿 儒"]
str1 = input("不想要的姓1")
str2 = input("不想要的姓2")
import random
while ( True ):
    a = random.randint(0, 8)
    str = namelist[a]
    list = str.split()
    if list[0] != str1:
        if list[0] != str2:
            print("第一个同学是",str)
            break
while (True):
    b = random.randint(0, 8)
    str0 = namelist[b]
    list1 = str0.split()
    if list1[0] != str1:
        if list1[0] != str2:
            if str0 != str:
                print("第二个同学是", str0)
                break