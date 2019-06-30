import time
def record():
    result=time.strftime("%Y-%m-%d %H:%M",time.localtime())
    print(result)
    g=input("输入商品名称\n")
    p=input("输入商品价格\n")
    file = open("C:/Users/apple/Desktop/账本.txt", "a")
    file.write(result+" "+g+" "+p+"\n")
    file.close()
    print("记录成功！")


def show():
    print("您的消费详情如下：")
    file=open("C:/Users/apple/Desktop/账本.txt","r")
    str = file.read()
    print(str)
    file.close()


def sum():
    print("您的消费总额为：")
    sum=0
    file=open("C:/Users/apple/Desktop/账本.txt","r")
    rows=file.readlines()
    for i in range(len(rows)):
        list=rows[i].split()
    sum=sum+int(list[3])
    print(sum)



cmd=int(input("请输入指令    1.记账  2.查看  3.总额 \n"))
if(cmd==1):
    record()
elif(cmd==2):
    show()
elif(cmd==3):
    sum()
