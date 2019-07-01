list=[]
棋盘=[]
a=0
while (a<19):
    list.append("[ ]")
    a+=1
a=0
while(a<19):
    棋盘.append(list.copy())
    a+=1
x=0
y=0
for x in range(19):
    for y in range(19):
        行 = 棋盘[x]
        print(行[y],end="")
    print()
#以上为打印棋盘
回合=0
# 以下是判断输赢的公式
def 判断输赢():
    for e in range(19):
        for f in range(15):
            if (棋盘[e][f]==棋盘[e][f+1]==棋盘[e][f+2]==棋盘[e][f+3]==棋盘[e][f+4]!="[ ]"):
                if (棋盘[e][f] == " ○"):
                    print("白方获胜")
                else:
                    print("黑方获胜")
                global 回合
                回合=400
                break
            if (棋盘[f][e]==棋盘[f+1][e]==棋盘[f+2][e]==棋盘[f+3][e]==棋盘[f+4][e]!="[ ]"):
                if (棋盘[f][e] == " ○"):
                    print("白方获胜")
                else:
                    print("黑方获胜")
                回合=400
                break
#上面那两个是横竖五个子的验证
#下面的是斜着五个子的验证
    for f in range(15):
        for g in range(15):
            if (棋盘[f][g]==棋盘[f+1][g+1]==棋盘[f+2][g+2]==棋盘[f+3][g+3]==棋盘[f+4][g+4]!="[ ]"):
                if (棋盘[f][g] == " ○"):
                    print("白方获胜")
                else:
                    print("黑方获胜")
                回合=400
                break
            if (棋盘[18-f][g]==棋盘[17-f][g+1]==棋盘[16-f][g+2]==棋盘[15-f][g+3]==棋盘[14-f][g+4]!= "[ ]"):
                if (棋盘[18-f][g] == " ○"):
                    print("白方获胜")
                else:
                    print("黑方获胜")
                回合=400
                break



#以下为运行
while(回合<400):
    a = int(input("行(0~18)"))
    b = int(input("列(0~18)"))
    if (棋盘[a][b] != "[ ]"):
        print("已经有子，请重新输入位置。")
        continue
    if (回合 % 2 == 0):
        棋盘[a][b] = " ●"
        回合 += 1
        for x in range(19):
            for y in range(19):
                print(棋盘[x][y], end="")
            print()
        判断输赢()
        continue
    if (回合 % 2 == 1):
        棋盘[a][b] = " ○"
        回合 += 1
        for x in range(19):
            for y in range(19):
                print(棋盘[x][y], end="")
            print()
        判断输赢()
        continue
