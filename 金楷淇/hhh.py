# from 金楷淇 import homework
# homework.fun()
# homework.fun1()
# from 金楷淇 import record
# from 金楷淇 import show
# from 金楷淇 import sum
import time
def time1():
    result=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return result
def record():
    goods = input("所购买的商品")
    price=input("所花费的金额")
    file=open("C:/Users/jkq/Desktop/记账本.txt","a")
    file.write(time1()+" "+goods+" "+price+"\n")
    file.close()
    print("记录成功")
def show():
    file = open("C:\\Users\\jkq\\Desktop\\记账本.txt","r")
    str=file.read()
    print(str)
    file.close()
def sum():
    print("总额")
    file = open("C:\\Users\\jkq\\Desktop\\记账本.txt","r")
    str=file.readlines()
    sum=0
    for i in range(len(str)):
        list=str[i].split()
        sum=sum+int(list[3])
    print(sum)
    file.close()
cmd=input("请输入指令 1.记账 2.查看 3.总额")
if(cmd==1):
    record()
elif(cmd==2):
    show()
elif(cmd==3):
    sum()