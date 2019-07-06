# 1，做一个界面，1，新增图书    2，查看已有图书     3，查看特定图书（模糊查询）    4，修改图书信息

import mysql.connector
class mysqlconn:
        cursor=None
        mydb=None
        def __init__(self):   #下划线，构造方法，创建对象自动调用一次
                mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="mysql",
                        database="lcccccc",
                        port="3308"
                )
                cursor = mydb.cursor()

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
        mysqlconn.update("insert into book (b_code,b_name,b_author,b_publish,b_pubdate,b_price) values(%s,%s,%s,%s,%s,%s)",val)

def fun2():
        rows = mysqlconn.query("select * from book ")
        for i in range(len(rows)):
                print(rows[i])

def fun3():
        val=[input("输入模糊的书名")]
        rows =mysqlconn.query("select * from book where b_name like '%'%s'%'",val)
        for i in range(len(rows)):
                print(rows[i])

def fun4():
        code=input("欲修改书的编号")
        name=input("修改书名为")
        val=[name,code]
        mysqlconn.update("update book set b_name=%s where b_code=%s",val)

def fun5():
        code = input("欲修改书的编号")
        author = input("修改作者为")
        val = [author, code]
        mysqlconn.update("update book set b_author=%s where b_code=%s", val)

def fun6():
        code = input("欲修改书的编号")
        publish = input("修改出版社为")
        val = [publish, code]
        mysqlconn.update("update book set b_publish=%s where b_code=%s", val)

def fun7():
        code = input("欲修改书的编号")
        pubdate = input("修改出版日期为")
        val = [pubdate, code]
        mysqlconn.update("update book set b_pubdate=%s where b_code=%s", val)


def fun8():
        code = input("欲修改书的编号")
        price = input("修改价格为")
        val = [price, code]
        mysqlconn.update("update book set b_price=%s where b_code=%s", val)

cmd=int(input("请输入指令：1.新增图书 2.查看已有图书 3.查看特定图书（模糊查询）4.修改图书信息"))
if(cmd==1):
        fun1()
elif(cmd==2):
        fun2()
elif(cmd==3):
        fun3()
elif(cmd==4):
        fun2()
        cmd1=int(input("修改：2.b_name  3.b_author  4.b_publish  5.b_pubdate 6.b_price"))
        if(cmd1==2):
                fun4()
        elif (cmd1 == 3):
                fun5()
        elif (cmd1 == 4):
                fun6()
        elif (cmd1 == 5):
                fun7()
        elif (cmd1 == 6):
                fun8()


label=["","","","","",""]
