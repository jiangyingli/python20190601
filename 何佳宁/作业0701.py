import random
list=["j k q","w h r","f j c","w x y","w s t","z j y","l q w","h j n","l c c"]
def fun():
    while (True):
        a=random.randint(0,8)
        list1 = list[a].split()
        firstname = list1[0]
        if (firstname != "w" and firstname!= "z"):
            print("第一位同学是" + str(list[a]))
            break
    while (True):
        b=random.randint(0,8)
        list2 = list[b].split()
        firstname = list2[0]
        if (b!=a and firstname != "w" and firstname!= "z"):
            print("第二位同学是" + str(list[b]))
            break
    person1=a
    person2=b

fun()
go=int(input("再来一次请code0\n"))
while(go==0):
    fun()
    go = int(input("再来一次请code0\n"))










