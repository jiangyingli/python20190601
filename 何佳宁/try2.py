import time
def record():
    buytime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    goods=input("买了什么")
    price=input("价钱")
    file = open("C:/Users/apple/Desktop/账本.txt", "a")
    file.write(buytime+" "+goods+" "+price+"\n")
    print("记录成功")
