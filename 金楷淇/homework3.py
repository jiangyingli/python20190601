import random
rand=random.randint(1,10)
num=input("请投币")
coin=int(num)
while(coin>=2):
    for i in range(4):
        c = input("猜猜,如退出请输入：退出\n")
        if (c=="退出"):
            print("剩余游戏币",coin)
            break
        a = int(c)
        if (a!=rand):
            if (a>rand):
                print("大了")
                coin=coin-2
                print("剩余游戏币",coin)
            elif (a<rand):
                print("小了")
                coin=coin-2
                print("剩余游戏币" ,coin)
        elif (a==rand):
            print("对了")
            coin=coin+6
            print("剩余游戏币" ,coin)
