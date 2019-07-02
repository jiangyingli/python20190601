import random
# 投币，无限次玩游戏，每猜猜一次扣2币，猜对奖励6币
# 可以随时退出，退出的时候退币
num = input("请投币")
coin = int(num)
rand = random.randint( 1,10 )
#疑问，投币数量和游戏次数有无关系
while(coin >= 2):
    cmd = input("请输入一个值，范围（1-10），退出请按0！")
    if(cmd=="0"):
        print("退您"+str(coin)+"个游戏币，请收好！")
        break;
    coin = coin - 2
    userinput = int(cmd)
    if(userinput>rand):
        print("大大大大了")
    elif(userinput<rand):
        print("小了")
    elif(userinput==rand):
        coin = coin + 6
        print("对了")
print("退出游戏！欢迎再来")
# ctrl+c   ctrl+v   ctrl+a      tab     shift+tab