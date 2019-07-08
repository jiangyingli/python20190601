# 1，做一个界面，1，新增图书    2，查看已有图书     3，查看特定图书（模糊查询）    4，修改图书信息
cmd=int(input("添加图书请code1,查看图书请code2,查看特定图书（模糊查询）请code3,修改图书信息请code4\n"))
from 何佳宁.try系列 import try2 as kt

if (cmd==1):
    code = input("请输入编号,如b_011")
    name = input("请输入书名,如《XX》")
    author = input("请输入作者姓名")
    publish = input("请输入出版社名称")
    pubdate = input("请输入出版日期,如2000-1-1")
    price = input("请输入图书价格")
    val=["code","name","author","publish","pubdate","price"]
    kt.update("insert into book values (%s,%s,%s,%s,%s,%s) ",val)
    print("添加完成")

elif (cmd==2):
    rows=kt.query("select*from book")

    for i in range(len(rows)):
        one = rows[i]
        for j in range(len(one)):
            print(one[j], end=" ")
        print()

elif(cmd==3):
    name=input("请输入书名")
    val=["《"+name+"%"]
    result=kt.query("select*from book where b_name like %s",val)
    print(result)

elif(cmd==4):
    name = input("请输入书名")
    val=[name]
    kt.update("delete*from book where b_name=%s ", val)
    print("输入更改后的信息")
    code = input("请输入编号,如b_011")
    name = input("请输入书名")
    author = input("请输入作者姓名")
    publish = input("请输入出版社名称")
    pubdate = input("请输入出版日期,如2000-1-1")
    price = input("请输入图书价格")
    val=["code","name","author","publish","pubdate","price"]
    kt.update("insert into book values (%s,%s,%s,%s,%s,%s) ", val)
    print("更改完成")