
# 记账软件

# 1，记账
# 2，查看明细
# 3，计算总金额

import time
def time1():
    str = time.strftime( "%Y-%m-%d %H:%M", time.localtime())
    return str


def record():
    goods = input("请输入商品名称\n")
    price = input("请输入商品价格\n")
    time = time1()
    file = open("C:/Users/jyl/Desktop/账本.txt","a")
    file.write(time+" "+goods+" "+price+"\n")
    file.close()#结束的时候，自动清空缓存
    print("☆☆ 记录成功！ ☆☆")

def show():
    file = open("C:/Users/jyl/Desktop/账本.txt","r")
    str = file.read()
    print("您的消费详单如下：")
    print(str)
    print("====================================")
    file.close()
def sum():
    print("您的消费总额为：")

    file = open("C:/Users/jyl/Desktop/账本.txt", "r")
    rows = file.readlines()
    sum = 0;
    for i in range( len(rows) ):
        list = rows[i].split()
        sum = sum + int(list[3])
    print(sum)

# 界面
print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
print("☆☆☆☆   欢迎使用姜老师记账软件   ☆☆☆☆☆☆☆")
print("☆☆☆☆☆☆☆   V1.0版本   ☆☆☆☆☆☆☆☆☆☆☆")
print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")

cmd = input("请输入指令   1.记账    2.查看    3.总额\n")
if(cmd == "1"):
    record()
elif(cmd=="2"):
    show()
elif(cmd == "3"):
    sum()

# 解决一个问题：运行一次，反复操作