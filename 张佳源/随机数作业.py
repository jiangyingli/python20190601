import random
a=random.randint(1,10)
b=0
while(b<=4):
    c=int(input("你猜是几"))
    if(c>a):
        print("大了")
        b+=1
    elif(c<a):
        print("小了")
        b+=1
    else:
        print("ok,你猜对了。")
        break
    if(b==4):
        print("你没有机会了，gg")
        break