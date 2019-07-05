# 作业1
# *
# * *
# *  *
# *   *

print("*")
for i in range(3):
    print("*",end="")
    for j in range(i+1):
        print(" ",end="")
    print("*") 



# 作业2
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(4):
    for j in range (i+1):
        print(str(j+1)+" ",end="")
    print()



# 作业3
# 输出乘法口诀表
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9


for i in range(9):
    for j in range(i+1):
        print(str(j+1)+"*"+str(i+1)+"="+str((i+1)*(j+1))+" ",end="")
    print()






















