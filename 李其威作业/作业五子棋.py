list=[]
for i in range(10):
        
    list.append([ ] )

list2=[]
for j in range(10)   :
    list2.append(list.copy())


for i in range(10):
    
    for j in range(10):
        print(list2[i][j],end="")
    print()
print()


def fun1():
    def fun2(a,b):
        for i in range(10):
    
            for j in range(10):
                list2[a-1][b-1]="●"
                print(list2[i][j],end="")
        
            print()
    def fun3(c,d):
        for i in range(10):
    
            for j in range(10):
                list2[c-1][d-1]="○"
                print(list2[i][j],end="")
            print()
    a = int(input("请黑子下：行："))
    b = int(input("          列："))
    fun2 (a,b)
    c= int (input("请白子下：行："))
    d= int (input("          列："))
    
    fun3(c,d)
for i in range (5000):
    fun1()



















    
