# 2，查看已有图书，分页显示，每页显示5条
import mysql.connector
class mysqlconn:
        cursor=None
        mydb=None
        def __init__(self):
                mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="mysql",
                        database="lcccccc",
                        port="3308"
                )
                cursor = mydb.cursor()

        def query(self,sql,val=[]):

                self.cursor.execute(sql, val)
                return self.cursor.fetchall

result=mysqlconn.query("select count(*) from book")
if (result<=15):
    mysqlconn.query("select * from book")


input=input("请按n显示下一页，按b退出")
page=1
start=(page-1)*10
sql="select * from book limit "+start+",10"