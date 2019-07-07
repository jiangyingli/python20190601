# 1，做一个界面，1，新增图书    2，查看已有图书     3，查看特定图书（模糊查询）    4，修改图书信息
# 2，选做：查看已有图书，分页显示，每页显示5条，
import mysql.connector

def query( sql , val):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="jintian",
        port="3308"
    )
    cursor = mydb.cursor()
    cursor.execute(sql,val)
    return cursor.fetchall()


def update (sql,val):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="jintian",
        port="3308"
    )
    cursor = mydb.cursor()
    cursor.execute(sql, val)
    mydb.commit()
def add():
    a= input("图书编号")
    b= input("图书名字")
    c= input("图书作者")
    d= input("出版社")
    e= input("出版时间")
    f= input("价格")
    val= [a,b,c,d,e,f]
    update("insert into book(b_code,b_name,b_author,b_publish,b_pubdate,b_price) values(%s,%s,%s,%s,%s,%s)", val)

def search():
    rows= query("select * from book",[])
    for i in range(len(rows)):
        str = rows[i]
        for j in range(len(str)):
            print(str[j],end=" ")
    print()

def searchsp():
    n = input("想要查询图书名字")
    val = ['%n%']
    lines = query("select * from book where b_name like %s",val)
    print(lines)

def correct():
    a= input("请输入修改图书编号")
    b= input("请输入修改后价格")
    val = [b,a]
    update("update book set b_price=%s where b_code =%s",val)


while(4>3):
    cmd = input("请输入指令  1.新增  2.查看所有  3.查看特定 4.修改 5.退出")
    if (cmd == "1"):
       add()
    elif(cmd == "2"):
        search()
    elif(cmd == "3"):
        searchsp()
    elif(cmd == "4"):
        correct()
    elif(cmd=="5"):

       break
input("按N下一页.e退出")
page= 1
start = (page-1)*10
sql = "select *from book limit 0,10"


import mysql.connector
class mysqlconn:
    cursor= None
    mydb = None
    def __init_(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database="jintian",
            port="3308"
        )
        cursor = mydb.cursor()

    def query(self,sql, val):
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    def update(self,sql, val):
        self.cursor.execute(sql, val)
        self.mydb.commit()

    input("按N下一页.e退出")
    page = 1
    start = (page - 1) * 10
    sql = "select *from book limit 0,10"
