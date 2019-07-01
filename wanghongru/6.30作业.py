import random
a = random.randint( 1,10 )

c = 1
while( True ):

    if c > 2:
        print("亲，失败了哦，要不要再试一次。")
        break
    b = int(input("亲，猜猜这个数是几？ 你有两次机会哦"))
    if b == a:
        print("亲， 猜对了呢，真的好厉害哦！！！")
        break
    elif b > a:
        print("亲， 大了呢，再试一试哦")
        c = c+1
    elif b < a:
        print("亲， 小了哦，再试一下啦")
        c = c+1