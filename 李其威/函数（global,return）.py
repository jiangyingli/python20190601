
def fun2( a, b=1 ):#默认值你不给我值的时候，我使用默认值
    print( a*b )

fun2( 4 ,8 )

def fun3():#计算发射一颗火箭，需要多少燃料
    #略
    result = 100
    return result
#值不是输出就行的，提供给下一步运算使用，使用返回值

r = fun3()
print("需要使用",r,"请下一位继续计算")

#返回值是不同函数，不同开发者之间传递信息的方式

# str = input()

x = 10 # 文件的顶级，全局变量，成员变量，有效范围是定义之后部分

def fun4():
    y = 20 #局部变量，只能在函数内使用，
    print(x)

print(x)
# print(y),y是局部变量，函数外无法使用


# 有一种情况比较特殊

z = 100
def fun5():
    global z
    z=z+100
    print(z)
#全局的和局部的发生冲突，局部的生效
fun5()

# 1，使用控制台下五子棋
list = [ ["[]","[]","[]"] , ["[]","[]","[]"] , ["[]","[]","[]"]]

for i in range(len(list)):
    for j in range(len(list)):
        row = list[i]
        print(row[j],end="")
    print()

x = int(input("x"))
y = int(input("y"))
list[x][y] = "●"

for i in range(len(list)):
    for j in range(len(list)):
        row = list[i]
        print(row[j],end="")
    print()


