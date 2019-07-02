import random
print("猜数游戏，每次2币。")
coin=int(input("玩家请投币"))
while(coin>1):
    cmd = (input("1,开始游戏  2，退出结算"))
    if(cmd=="1"):
        b=0
        coin-=2
        a = random.randint(1, 10)
        while(b<=1):
            c=int(input("你猜是几"))
            #c = random.randint(1, 10)
            #print(str(c),end="")
            if(c>a):
                print("大了")
                b+=1
                continue
            elif(c<a):
                print("小了")
                b+=1
                continue
            else:
                print("ok,你猜对了,您获得6个币。")
                coin+=6
                break
        continue
    if(cmd=="2"):
        print("游戏结束")
        print("您剩余"+str(coin)+"个币")
        break
while (coin <= 1):
    print("游戏币不足，游戏结束。")
    print("您剩余" + str(coin) + "个币")
    break

