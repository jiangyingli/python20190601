# 1，做一个界面，1，新增图书    2，查看已有图书     3，查看特定图书（模糊查询）    4，修改图书信息

import mysql.connector
class mysqlconn:
        cursor=None
        mydb=None
        def __init__(self):   #下划线，构造方法，创建对象自动调用一次
                print("构造方法被调用")
                self.mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="mysql",
                        database="lcccccc",
                        port="3308"
                )
                self.cursor = self.mydb.cursor()

        def update(self,sql,val=[]):
                self.cursor.execute(sql, val)
                self.mydb.commit()

        def query(self,sql,val=[]):
                self.cursor.execute(sql, val)
                return self.cursor.fetchall()

def fun1():
        code=input("输入code")
        name=input("输入name")
        author=input("输入author")
        publish=input("输入publish")
        pubdate=input("输入pubdate")
        price=input("输入price")
        val=[code,name,author,publish,pubdate,price]
        db=mysqlconn()
        db.update("insert into book (b_code,b_name,b_author,b_publish,b_pubdate,b_price) values(%s,%s,%s,%s,%s,%s)",val)

def fun2():
        db = mysqlconn()
        rows = db.query("select * from book ")
        for i in range(len(rows)):
                print(rows[i])

def fun3():
        db = mysqlconn()
        val=["%"+input("输入模糊的书名")+"%"]
        rows =db.query("select * from book where b_name like %s",val)
        for i in range(len(rows)):
                print(rows[i])

def fun4():
        cmd1 = input("请输入修改书籍的b_code")
        cmd2 = int(input("请输入修改的编号：1.b_name  2.b_author  3.b_publish  4.b_pubdate 5.b_price"))
        label = ["", "b_name", "b_author", "b_publish", "b_pubdate", "b_price"]
        str = input("请输入修改后的内容")
        db = mysqlconn()
        db.update("update book set " + label[cmd2] + " = " + str + " where b_code=" + cmd1)


cmd=int(input("请输入指令：1.新增图书 2.查看已有图书 3.查看特定图书（模糊查询）4.修改图书信息"))
if(cmd==1):
        fun1()
elif(cmd==2):
        fun2()
elif(cmd==3):
        fun3()
elif(cmd==4):
        fun2()
        fun4()


