# 2，查看已有图书，分页显示，每页显示5条
import mysql.connector
class mysqlconn:
        cursor=None
        mydb=None
        def __init__(self):
                print("构造方法被调用")
                self.mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="mysql",
                        database="lcccccc",
                        port="3308"
                )
                self.cursor = self.mydb.cursor()

        def query(self,sql,val=[]):

                self.cursor.execute(sql, val)
                return self.cursor.fetchall

db=mysqlconn ()
rows=db.query("select * from book limit 0,10")
for i in range(len(rows)):
        print(rows[i])
input=input("请按n显示下一页，按b退出")
while(input=="b"):
        break
while(input=="n"):
        page=1
        start=(page)*10
        sql="select * from book limit "+start+",10"
        rows1=db.query(sql)
        for j in range(len(rows1)):
                print(rows1[j])
        page=page+1