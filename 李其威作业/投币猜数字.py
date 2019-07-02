import random
rand =random.randint(1,10)
coin=int(input("请投币（个）\n"))
def fun():
    for i in range(100):
        global coin
        a = int(input("你猜是几\n"))
        if (a>rand):
            print("大了")
            coin=coin-2
            continue
        elif (a<rand):
            print("小了")
            coin=coin-2
            continue
        elif(a==rand):
            print("真聪明猜对了")
            coin=coin+6
            print("您剩余游戏币" + str(coin) + "个")
            break


for i in range(1000):
    b = int(input("是否进行游戏,请输入1.是或2.否\n"))
    if (coin>=2) :
        if (b == 1):
            fun()
        elif (b == 2):
            print("游戏结束")
            print("剩余游戏币"+str(coin)+"个，欢迎充值")
            break
    else:
        print("余额不足，请充值")
        break
