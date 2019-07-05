#作业2,投币猜数，一次2币，猜对加6币


num=input("请投币")
coin=int(num)

import random
rand=random.randint(1,10)

while(coin>=2):

    a=int(input("请您输入猜想的数字,范围（1——10），退出请输入0："))
    if (a==0):
        print("退出", coin, "币")
        break;

    coin=coin-2
    if(a==rand):
        print("您猜对啦！")
        coin=coin+6
        print("剩余",coin,"币")
        rand = random.randint(1, 10)

    elif(a>rand):
        print("您猜大了")
        print("剩余", coin,"币")
    elif(a<rand):
        print("您猜小了")
        print("剩余", coin,"币")
