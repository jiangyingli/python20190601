list=["金楷淇","王鸿儒","冯家琛","王小丫","王松涛","李聪聪","何佳宁","李其威","张佳源"]
import random
def fun1(x):
    a = random.randint(1, x)
    print(list[a - 1])
    del list[a - 1]
    b = random.randint(1, x)
    print(list[b - 1])

def fun2():
    cmd1=input("请在“金、王、冯、李、何、张”中输入您不想抽到的1个姓氏：")
    cmd2=input("请在“金、王、冯、李、何、张”中输入您不想抽到的另1个姓氏：")
    m=0
    for i in range(len(list)):
        if (list[i][0] == cmd1):
            m = m + 1
        elif (list[i][0] == cmd2):
            m = m + 1
        for j in range(len(list) - 1 - i):
            if (list[j][0]==cmd1):
                list[j], list[j + 1] = list[j + 1], list[j]
            elif (list[j][0]==cmd2):
                list[j], list[j + 1] = list[j + 1], list[j]
    fun1(len(list)-m)

cmd=int(input("请输入指令：1、随机抽签；2、除姓氏抽签"))
if(cmd==1):
    fun1(len(list))
if(cmd==2):
    fun2()


