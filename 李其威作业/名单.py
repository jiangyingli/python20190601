li = open("C:/Users/DELL/Desktop/记事本2.txt", "r")

list = li.readlines()
a=input("不想选的姓氏1.\n")
b=input("不想选的姓氏2.\n")
list1=[]
list2=[]
line=li.readline()
while(line!=""):
    c=line[0]
    d=line[:len(line)-1]
    if(c!=a ):
        if(c!=b):
            list2.append(c)
            list1.append(d)     #有错误，list1 ,list2元素加不进去，不会改
    line = li.readline()
e=list2.count("a")
f=list2.count("b")
g=len(list)
import random
rand1 =random.randint(0,g-e-f)
rand2 =random.randint(0,g--e-f)
while(rand1==rand2):
    rand1 =random.randint(0,g-e-f)
    rand2 =random.randint(0,g-e-f)

print("你选出的第一位是"+list1[rand1])
print("你选出的第二位是"+list1[rand2])
print("-----------------第一轮结束-----------------")
print("-----------------第二轮开始-----------------")
a2=input("不想选的姓氏1.\n")
b2=input("不想选的姓氏2.\n")
list1=[]
list2=[]
line=li.readline()
while(line!=""):
    c=line[0]
    d=line[:len(line)-1]
    if(c!=a and c!=b and c!=a2 and c!=b2):
        list2.append(c)
        list1.append(d)
    line = li.readline()
e2=list2.count("a2")
f2=list2.count("b2")
import random
rand1 =random.randint(0,g-e-f-e2-f2)
rand2 =random.randint(0,g--e-f-e2-f2)
while(rand1==rand2):
    rand1 =random.randint(0,g-e-f-e2-f2)
    rand2 =random.randint(0,g-e-f-e2-f2)

print("你选出的第一位是"+list1[rand1])
print("你选出的第二位是"+list1[rand2])
print("-----------------第二轮结束-----------------")
print("-----------------第三轮开始-----------------")

a3=input("不想选的姓氏1.\n")
b3=input("不想选的姓氏2.\n")
list1=[]
list2=[]
line=li.readline()
while(line!=""):
    c=line[0]
    d=line[:len(line)-1]
    if(c!=a and c!=b and c!=a2 and c!=b2 and c!=a3 and c!=b3):
        list2.append(c)
        list1.append(d)
    line = li.readline()
e3=list2.count("a3")
f3=list2.count("b3")
import random
rand1 =random.randint(0,g-e-f-e2-f2-e3-f3)
rand2 =random.randint(0,g--e-f-e2-f2-e3-f3)
while(rand1==rand2):
    rand1 =random.randint(0,g-e-f-e2-f2-e3-f3)
    rand2 =random.randint(0,g-e-f-e2-f2-e3-f3)

print("你选出的第一位是"+list1[rand1])
print("你选出的第二位是"+list1[rand2])
