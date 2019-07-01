print("卍卍卍卍卍欢迎进行疯狂猜数字游戏卐卐卐卐卐")


coin = int(input("请投入游戏代币,2代币一次"))


while ( True ):
    import random
    a = random.randint( 1,10 )
    while( True ):
        c = int(input("如果不想继续，请输入1,继续游戏输入0"))
        if c == 1:
            print("您剩余的游戏币为",coin)
            break
        if coin < 2:
            print("您的游戏币不足")
            print("游戏币剩余",coin)
            break
        coin = coin-2
        b = int(input("猜猜这是几，请输入1到10中的一个数，猜对奖励六游戏币"))
        if b == a:
            print("亲， 猜对了呢，真的好厉害哦！！！奖励6游戏币")
            coin = coin+6
            break
        elif b > a:
            print("亲， 大了呢，再试一试哦")
        elif b < a:
            print("亲， 小了哦，再试一下啦")

    if c == 1:
        break;
    elif coin < 2:
        q = int(input("如果继续游戏，请输入1进行继续投币，不想进行输入0"))
        if q == 1:
            r = int(input("请继续投入代币"))
            coin = coin+r
        elif q == 0:
            break;





print("欢迎下次进行本游戏☺☺☺")








'''



#账本





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















'''






