'''
book=open('D:\记账本.txt','a+')
str1=input("时间")
str2=input("事")
str3=input("钱")
book.write(str1+str2+str3+"\n")
book.seek(0,0)
a=book.read()
print(a)
book.close()
'''
list钱=[]
import time
def time1():
    result=time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())
    return result
def record():
    print("开始记账")
    book = open('D:\记账本.txt', 'a+')
    str2 = input("事")
    str3 = input("钱")
    book.write(time1()+"  "+str2+"   "+str(str3)+"   "+"\n")
    book.seek(0, 0)
    book.close()

def show():
    print("查看账本")
    book = open('D:\记账本.txt', 'a+')
    book.seek(0, 0)
    a = book.read()
    print(a)
    book.close()

def sum():
    print("您本月消费")
    book = open('D:\记账本.txt', 'a+')
    book.seek(0, 0)
    rows = book.readlines()
    print(len(rows))
    sum=0
    for i in range(len(rows)):
        list=rows[i].split()
        sum+=int(list[3])
    print(sum)
    book.close()



a=0
while(a<=9999):
    cmd=input("请输入指令1.记账 2.查看 3.总和 4.关闭")
    if (cmd=="1"):
        record()
        a+=1
    elif (cmd=="2"):
        show()
        a+=1
    elif (cmd=="3"):
        sum()
        a+=1
    elif(cmd=="4"):
        break