import time
def now():
    localtime = time.strftime("%Y-%m-%d%H:%M:%S",time.localtime())
    return localtime

def rec():
    t=now()
    g=input("名称")
    p=input("价格")
    file=open("C:\\Users\\apple\\Desktop\\账本.txt","a")
    file.write(t+" "+g+" "+p+"\n")
    file.close()
    print("记账成功")

def show():
    file=open("C:\\Users\\apple\\Desktop\\账本.txt","r")
    str=file.read()
    print("您的消费账单如下：")
    print(str)
    file.close()
def sum():
    print("求和")
    file = open("C:\\Users\\apple\\Desktop\\账本.txt", "r")
    row=file.readlines()
    sum=0
    for i in range(len(row)):
        list=row[i].split()
        sum=sum+int(list[2])
        print(sum)
    file.close
end =input("请输入指令 1. 记账  2.查看   3.总额")
if (end=="1"):
    rec ()
elif(end=="2"):
    show()
elif(end=="3"):
    sum()