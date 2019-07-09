#菲波那切数列
a = int(input("你需要几项？"))
n1 = 0
n2 = 1
count = 2
if (a==1):
    print("菲波那切数列"+str(n1))
else:
    print("菲波那切数列"+str(n1)+","+str(n2),end=",")
    while(count<=a):
        n = n1 + n2
        print(str(n),end=",")
        n1 = n2
        n2 = n
        count = count +1


#杨辉三角


    

