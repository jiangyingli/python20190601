import random

num = input("insert coins")
coin = int(num)
rand = random.randint(1,10)
def guess():
    global coin
    while (coin>=2):
        userinput = input("please guess a number，range in (1-10).Press 0 to exit.")
        if (userinput=="0"):
            end()
            break
        a = int(userinput)
        if (a>rand):
            print("too big")
            coin = coin-2
        elif(a<rand):
            print("too small")
            coin = coin-2
        elif(a==rand):
            print("correct,congratulation!")
            coin= coin-2
            coin= coin+6


def end():
    print(coin,end="")
    print(" is your coin's number. Successfully exit!")

while(4>2):
    cmd = input("1.play 2.exit")
    if (cmd == "1"):
        guess()
        cmd2 = input("1.replay 2.exit")
        if (cmd2 == "1"):
            b = int(input("You coin is not enough,please import more."))
            coin = coin + b
        elif (cmd2 == "2"):
            end()
            break

    elif (cmd == "2"):
        end()
        break



