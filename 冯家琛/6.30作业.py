import time

def now():
    localtime =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime

def record():
    t = now()
    g = input("请输入商品")
    p = input("请输入价格")
    file = open("C:/Users/DREAM/Desktop/课堂.txt", "a")
    file.write(t+" "+g+" "+p+"\n")
    print("记录完毕")
    print("==================================================================================")
    file.close()


def show():
    t = now()

    file = open("C:/Users/DREAM/Desktop/课堂.txt", "r")
    str = file.read()
    file.close()
    print("您的账单如下：")
    print(str)
    print("=============================================================================")


def sum():
    t = now()
    file = open("C:/Users/DREAM/Desktop/课堂.txt", "r+")
    lines = file.readlines()
    total = 0
    for i in range(len(lines)):
        str = lines[i]

        list = str.split()
        a = list[3]
        b = int(a)
        total = b + total
    print("您的消费总额如下：")
    print(total)
    file.close()

def end():
    a = 5
    print("安全退出")


def z():
    cmd = input("请输入指令  1.记账  2.查看  3.总额 4.退出")
    if (cmd == "1"):
        record()
    elif(cmd == "2"):
        show()
    elif(cmd == "3"):
        sum()
    elif(cmd == "4"):
        end()





while(4>3):
    cmd = input("请输入指令  1.记账  2.查看  3.总额 4.退出")
    if (cmd == "1"):
        record()
    elif(cmd == "2"):
        show()
    elif(cmd == "3"):
        sum()
    elif(cmd == "4"):
        end()
        break







