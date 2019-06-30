import time
def time1():
    result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return result




def funrecord():
    str = input("输入需要记录的内容，请输入形式为  空格，物品，空格，价格，空格")
    file = open("C:/Users/apple/Desktop/zhangben.txt","a")
    file.write( time1()+str + "\n" )
    file.close()
    print("记录成功✔")




def funread():
    file = open("C:/Users/apple/Desktop/zhangben.txt","r")
    str = file.read()
    print(str)
    file.close()
    print("________________________________________________________________________________________________")










def funsum():
    file = open("C:/Users/apple/Desktop/zhangben.txt", "r+")
    list = file.readlines()
    i = 0
    a = 0
    for i in range(len(list)):
        str = list[i]
        list1 = str.split()
        a = a+int(list1[3])
    print(a)
    file.close()











com = 0
while ( True ):
    com = int(input("记账请输入 1 查找账单输入 2 求和请输入 3 结束请输入 4 "))
    if com == 1:
        funrecord()
    elif com == 2:
        funread()
    elif com == 3:
        funsum()
    elif com == 4:
        break








