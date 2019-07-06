from 李其威作业 import 数据库 as a
caozuoyi=input("请选择你要进行的操作：1：添加图书  2：查看已有图书  3，查看特定图书（模糊查询）    4，修改图书信息\n")

if (caozuoyi=="1"):
    code=input("编号:")
    name=input("名称:")
    auther=input("作者姓名:")
    publish=input("出版社：")
    pubdate=input("出版日期“xx-xx-xx”：")
    price=int(input("价格："))
    val=["code","name","auther","publish","pubdate","price"]
    a.update("insert into book values(%s,%s,%s,%s,%s)",val)
    print("添加成功")
elif(caozuoyi=="2"):
    b=a.query("select * from book ")
    print(b)
elif(caozuoyi=="3"):

    val=[ "《" + input("请输入书名\n") + "%"]

    book = a.query("select * from book where b_name like %s ", val)
    print(book)
elif(caozuoyi=="4"):
    val=["《"+input("请输入修改的书名\n")+"》"]
    book = a.query("select * from book where b_name = %s ", val)
    print(book)
    val = ["《" + input("请输入修改的编号\n") + "》"]
    book = a.update("delete * from book where b_code = %s ", val)
    code = input("请输入修改的编号\n")
    name = input("请输入修改的名称\n")
    auther = input("请输入修改的作者姓名\n")
    publish = input("请输入修改的出版社\n")
    pubdate = input("请输入修改的出版日期“xx-xx-xx”\n")
    price = int(input("请输入修改的价格\n"))
    val = ["code", "name", "auther", "publish", "pubdate", "price"]
    a.update("insert into book values(%s,%s,%s,%s,%s)", val)
    print("修改成功")
    b = a.query("select * from book ")
    print(b)

    #修改，
    # val = input("请输入修改的图书id")
    # # 显示
    # print("1书名    2价格    3出版社    4地址")
    # label = ["","name","price","publish","address"]
    # input = input("请输入要修改的编号")
    # 2
    # val = input("请输入修改后的值")
    #
    # sql =  "update book set "+label[input]+" = "+val+" where book_id=xx""