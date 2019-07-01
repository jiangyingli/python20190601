import random            #导入随机数模块
list1=[]                 #建立一个list等会输入被排除的同学
print("欢迎使用ZJY上课点名系统")
file=open('D:\点名册.txt', 'a+')#打开点名册
file.seek(0,0)                  #光标恢复到第一位
rows = file.readlines()         #读取点名册
if(len(rows)==0):
    print("本程序首次使用")
if(len(rows)==1):                #因为程序可能刚开始使用，所以分类讨论(这是第二次)
    name = rows[0].split()
    list1.append(name[0])
    list1.append(name[1])
    print("以下同学在保护阶段" + str(list1))#输出被保护同学
if(len(rows)>=2):               #这是两次之后
    for i in range(len(rows)-2,len(rows)):
        name = rows[i].split()
        list1.append(name[0])
        list1.append(name[1])
    print("以下同学在保护阶段"+str(list1))#输出被保护同学

trial=1
while(trial>0):     #这里做成了循环，是因为可能最后没有两个同学可以提问，所以循环
    list = ["金楷淇", "王鸿儒", "冯家琛", "王小丫", "王松涛", "李聪聪", "何佳宁", "李其威", "张佳源"]
    cmd1=int(input("请输入排除几个姓氏"))
    for i in range (cmd1):
        姓氏=input("请输入要排除的姓氏")
        if ( 姓氏=="王"):
            list.remove("王鸿儒")
            list.remove("王小丫")
            list.remove("王松涛")
        if ( 姓氏=="李"):
            list.remove("李聪聪")
            list.remove("李其威")
        if ( 姓氏=="金"):
            list.remove("金楷淇")
        if ( 姓氏=="冯"):
            list.remove("冯家琛")
        if ( 姓氏=="何"):
            list.remove("何佳宁")
        if ( 姓氏=="张"):
            list.remove("张佳源")
    #print(list)
    if(len(list1)>0):
        if(list1[0] in list):        #这个部分是在排除姓氏后，排除提问过的同学
            list.remove(list1[0])
        if(list1[1] in list):
            list.remove(list1[1])
    if(len(list1)>2):
        if(list1[2] in list):
            list.remove(list1[2])
        if(list1[3] in list):
            list.remove(list1[3])
    #print(list)
    a=len(list)              #以下部分是随机同学的部分
    if(a>=2):
        b=random.randint(0, a-1)
        c=random.randint(0, a-1)
        if(b==c):
            c=random.randint(0,a-1)
        print("本次被提问的同学为"+"   "+list[b]+"   "+list[c])
        print("开始你们的表演")
        file.write(list[b]+"  "+list[c]+"\n")#记录这次被提问的同学
        break
    if(a<2):                      #因为限制条件太多，所以会出现不足的问题，设置了循环
        print("提问人数不足,是否重新选择")
        cmd2=int(input("1，放弃提问  2，重新选择"))
        if(cmd2==1):
            print("over")
            break
        if(cmd2==2):
            continue

file.close()                            #最后关闭文件