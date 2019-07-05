import mysql.connector
def query(sql,val=[]):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="zjy1",
    port="3308"
    )
    cursor=mydb.cursor()
    cursor.execute(sql,val)
    return cursor.fetchall()
def update(sql,val=[]):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="zjy1",
        port="3308"
    )
    cursor=mydb.cursor()
    cursor.execute(sql,val)
    mydb.commit ()
print("欢迎使用ZJY图书阅览")
cmd1=str(input("1,新增图书  2,图书总览  3,查询图书  4,修改图书信息"))
if (cmd1=="1"):
    print("请输入图书信息")
    code=input("请输入图书编号(格式b_000)")
    name=input("请输入图书名(《格式XXX》)")
    author=input("请输入作者姓名")
    publish=input("请输入出版社名称")
    pubdate=input("请输入出版时间(格式0000-00-00)")
    price=input("请输入图书价格")
    val=[code,name,author,publish,pubdate,price]
    update("insert into book values (%s,%s,%s,%s,%s,%s) ",val)
    print("添加成功")
elif(cmd1=="2"):
    print("以下为图书总览")
    rows = query("select * from book ")
    for i in range(len(rows)):
        for j in range(4):
            print(rows[i][j], end=" ")
        print()
elif(cmd1=="3"):
    book1name="《"+input("请大致输入书本的名字")+"%"
    val=[book1name]
    book1=query("select * from book where b_name like %s ",val)
    for i in range(len(book1)):
        for j in range(4):
            print(book1[i][j], end=" ")
        print()
elif(cmd1=="4"):
    book2name="《"+input("请输入选择修改的图书名")+"》"
    val=[book2name]
    book2=query("select * from book where b_name = %s ",val)
    for i in range(len(book2)):
        for j in range(4):
            print(book2[i][j], end=" ")
        print()
    book2code = input("请输入选择修改图书的序号(b_000)")
    val = [book2code]
    book2 = query("delete * from book where b_code = %s ", val)
    print("请输入修改后的图书信息")
    name2 = input("请输入图书名(格式《XXX》)")
    author2 = input("请输入作者姓名")
    publish2 = input("请输入出版社名称")
    pubdate2 = input("请输入出版时间(格式0000-00-00)")
    price2 = input("请输入图书价格")
    val = [book2code, name2, author2, publish2, pubdate2, price2]
    update("insert into book values (%s,%s,%s,%s,%s,%s) ", val)
    print("修改成功")


















