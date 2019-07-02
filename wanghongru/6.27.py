x = int(input("你想要几行的棋盘"))+1
y = int(input("你想要几列的棋盘"))+1
list = []
a = 0
while (a<=x):
    list.extend(["[]"])
    a = len(list)

table = []
a = 0
while (a <= y):
    table.extend([list.copy()])
    a = len(table)
print(table)




def funtable():
    for i in range(y-1):
        for j in range(x-1):
            print(table[i][j], end="")
        print()
funtable()


def funplayer1():
    while ( True ):
        a = int(input("黑子你要下的列"))
        b = int(input("黑子你要下的行"))
        if table[b][a] == "[]":
            break;
        elif table[b][a] != "[]":
            print("错误")
    table[b][a] = "●"
    funtable()

def win():
    x = len(list)
    y = len(table)
    for i in range(x-4):
        for j in range(y):
            if table[i][j] == table[i+1][j] == table[i+2][j] == table[i+3][j] == table[i+4][j] == "●":
                print("player1 win!")
                False
            elif  table[i][j] == table[i+1][j] == table[i+2][j] == table[i+3][j] == table[i+4][j] =="○":
                print("player2 win!")
                False
    for i in range(x):
        for j in range(y-4):
            if table[i][j+1] == table[i][j+2] == table[i][j+3] == table[i][j+4] == table[i][j] == "●":
                print("player1 win!")
                False
            elif  table[i][j] == table[i][j+1] == table[i][j+2] == table[i][j+3] == table[i][j+4] =="○":
                print("player2 win!")
                False
    for i in range(x-4):
        for j in range(y-4):
            if table[i][j] == table[i+1][j+1] == table[i+2][j+2] == table[i+3][j+3] == table[i+4][j+4] == "●":
                print("player1 win!")
                False
            elif  table[i][j] == table[i+1][j+1] == table[i+2][j+2] == table[i+3][j+3] == table[i+4][j+4] =="○":
                print("player2 win!")
                False
    for i in range(x-4):
        for j in range(4, y):
            if table[i][j] == table[i+1][j-1] == table[i+2][j-2] == table[i+3][j-3] == table[i+4][j-4] == "●":
                print("player1 win!")
                False
            elif  table[i][j] == table[i+1][j-1] == table[i+2][j-2] == table[i+3][j-3] == table[i+4][j-4] =="○":
                print("player2 win!")
                False







def funplayer2():
    while ( True ):
        a = int(input("白子你要下的列"))
        b = int(input("白子你要下的行"))
        if table[b][a] == "[]":
            break;
        elif table[b][a] != "[]":
            print("错误")
    table[b][a] = "○"
    funtable()








q = int(input("如果执黑，请输入1，执白输入2，执黑先手。"))
if q == 1:
    funplayer1()
    while( True ):
        funplayer2()
        win()
        if False:
            break
        funplayer1()
        win()
        if False:
            break
elif q == 2:
    funplayer2()
    while( True ):
        funplayer1()
        win()
        if False:
            break
        funplayer2()
        win()
        if False:
            break