list =[]
for i in range(10):
    list.append([])
list1=[]
for j in range(10):
    list1.append(list.copy())

for i in range(9):
    for j in range(9):
        print(list1[i][j],end="")
    print()

def fun():
    def fun1(x,y):
        list1[x - 1][y - 1] = "●"
        for i in range(10):
            for j in range(10):
                print(list1[i][j],end="")
            print()

    x = int(input("黑子下第几行"))
    y = int(input("      第几列"))
    fun1(x,y)

    def fun2(m,n):
        list1[m - 1][n - 1] = "○"
        for i in range(10):
            for j in range(10):
                print(list1[i][j],end="")
            print()

    m = int(input("白子下第几行"))
    n = int(input("      第几列"))
    fun2(m,n)

for n in range (50):
    fun()





