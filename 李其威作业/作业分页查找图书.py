from 李其威 import 数据库 as a
i=0
b=a.query("select * from book ")
print(b[i*5:(i+1)*5])
while (i>=0) :
    c=input("1,上一页     2，下一页   3,退出\n")
    if (c=="1"):
        i=i-1
    elif(c=="2"):
        i=i+1
    elif(c=="3"):
        break
    b=a.query("select * from book ")
    print(b[i*5:(i+1)*5])


#page = 2

#start = (page-1)*10

#sql = "select * from book limit "+str(start)+" , 10"

#print(sql)
