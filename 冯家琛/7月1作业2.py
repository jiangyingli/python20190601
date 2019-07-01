#随机提问系统 随机两人
import random
list=[]
def pick():
    rand = random.randint(0, 8)
    file = open("C:/Users/DREAM/Desktop/点名册.txt", "r+")
    lines = file.readlines()
    list.append(rand)

times = int(input("请输入要选择几个人，范围是1--2"))
for i in range(times+1):
    rand = random.randint(0, 8)
    file = open("C:/Users/DREAM/Desktop/点名册.txt", "r+")
    lines = file.readlines()
    list.append(rand)
    if (list[i-1]==list[i]):
        pick()

    else:
        print(lines[rand])
