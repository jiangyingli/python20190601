
def time1():
    import time
    localtime = time.localtime()
    result=str(localtime[0])+"-"+str(localtime[1])+"-"+str(localtime[2])
    return result




def record():
    li = open("C:/Users/DELL/Desktop/记事本.txt", "a+")

    b = input("名称\n")
    c = int(input("价格\n"))



    li.write(time1()+" "+str(b)+" "+str(c)+"\n")
    li.close()

def show():
    li = open("C:/Users/DELL/Desktop/记事本.txt", "r")
    d=li.read()
    print(d)
    li.close()
def sum():
    li = open("C:/Users/DELL/Desktop/记事本.txt", "r")
    list=li.readlines()
    g=0
    for i in range(len(list)):
        list1=list[i].split()
        j=list1[2]
        g=g+int(j)
    print(g)
def zong():
    cmd=input("请输入指令   1.  2.  3.")

    if (cmd=="1"):
        record()
    elif(cmd=="2"):
        show()
    elif(cmd=="3"):
        sum()

for i in range(10000):
    zong()