list=["王鸿儒","王小丫","王松涛","冯家琛","李聪聪","何佳宁","张佳源","李其威","金楷淇"]
def fun(c,d):
    import random
    a=random.randint(c,d)
    b=random.randint(c,d)
    if (a == b):
        b = random.randint(c,d)
        while (a != b):
            print(list[a], list[b])
            break
    elif(a!=b):
        print(list[a], list[b])
    return
c=input("排除的姓氏")
if(c=="王"):
    list.remove("王鸿儒")
    list.remove("王小丫")
    list.remove("王松涛")
    f=fun(0,5)
if(c=="张"):
    list.remove("张佳源")
    fun(0,7)
if (c == "李"):
    list.remove("李聪聪")
    list.remove("李其威")
    fun(0,6)
if (c == "金"):
    list.remove("金楷淇")
    fun(0,7)
if (c == "冯"):
    list.remove("冯家琛")
    fun(0,7)

if (c== "何"):
    list.remove("何佳宁")
    fun(0,7)





