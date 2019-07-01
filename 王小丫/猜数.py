num=input("请投币")
coin=int(num)
import random
a=random.randint(1,10)

while(coin>2):
    c=input("你猜是几")
    if(c=="0"):
        print('退您'+str(num))
        break
    c=int(c)
    coin = int(coin) - 2
    if(c>a):
        print("大了")
        print(coin)

    elif(c<a):
        print("小了")
        print(coin)

    elif(c==a):
        print("对了")
        coin=int(num)+4
        num=coin
        print(coin)
