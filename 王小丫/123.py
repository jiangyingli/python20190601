#control a 全选
#control c 复制
#control v 粘贴
num=input("请投币")
coin=0
import random
a=random.randint(1,10)

while(coin>2):
    c=input("你猜是几","范围在(1-10)","退出按0")
    if(c=="0"):
        print('退您'+str(num))
        break
    c=int(c)

    if(c>a):
        print("大了")
        coin=int(num)-2
        num=coin
        print(coin)
    elif(c<a):
        print("小了")
        coin =int(num)-2
        num=coin
        print(coin)
    elif(c==a):
        print("对了")
        coin=int(num)+4
        num=coin
        print(coin)




