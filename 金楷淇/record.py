import time
def time1():
    result=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return result
def record():
    goods = input("所购买的商品")
    price=input("所花费的金额")
    file=open("C:/Users/jkq/Desktop/记账本.txt","a")
    file.write(time1()+" "+goods+" "+price+"\n")
    file.close()
    print("记录成功")
record()

