import random
rand =random.randint(1,10)
i=0
while(i<3):
    i = i + 1
    a = int(input("你猜是几\n"))
    if(i<3):
        if (a>rand):
            print("大了")
            continue
        elif (a<rand):
            print("小了")
            continue
        elif(a==rand):
            print("真聪明猜对了")
        break
    elif(i==3):
        if(a!=rand):
            print("游戏结束再见")
            break
        elif(a==rand):
            print("终于猜对了")
            break