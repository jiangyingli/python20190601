import random
num=int(input("请投币\n"))
start=int(input("开始游戏请按0\n"))

def fun():
    a=random.randint(1,10)
    b = int(input("你猜是几\n"))
    global num
    num=num-2
    n=0
    while (n>=0):
        if (b>a):
            print("大了")
            b=int(input("再猜\n"))
            num=num-2
        elif(b<a):
            print("小了")
            b = int(input("再猜\n"))
            num=num-2
        elif(b==a):
            print("恭喜你！对了！")
            num=num+6
            break
        n=n+1
    game=int(input("继续下一轮请按1，结束游戏请按2 \n"))
    if(game==1):
        fun()
    elif(game==2):
        print("剩余钱币为"+str(num))
        print("结束游戏，欢迎再来！")

if (start==0):
    fun()


