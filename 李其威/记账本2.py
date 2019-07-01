def time1()  :
    import time
    localtime=time.localtime()
    result=str(localtime[0])+"-"+str(localtime[1])+"-"+str(localtime[2])
    return result
def fun1():
    a=input("名称")
    b=int(input("价格"))
    file=open("C:/Users/DELL/Desktop/记事本.txt", "a+")
    file.write(time1()+" "+a+" "+str(b)+"/n")
    file.close()
    print("记账成功")
def fun2():
    file = open("C:/Users/DELL/Desktop/记事本.txt", "r")
    c=file.show()
    print(c)
def fun3():
    file = open("C:/Users/DELL/Desktop/记事本.txt", "r")
    list=file.readlines()
    d=0
    for i in range(len(list)):
        list1=list[i].split()
        f=list1[2]
        d=d+int(f)
    print(d)
def zong():
    cmd=input("请输入指令   1.记账  2.查看  3.算账")

    if (cmd=="1"):
        fun1()
    elif(cmd=="2"):
        fun2()
    elif(cmd=="3"):
        fun3()

for i in range(10000):
    zong()