import mysql.connector
class mysqlconn:
    cursor = None
    mydb=None
    def __init__(self):
        mydb=mysql.connector.connet(
            host="localhost",
            user="root",
            passwd="mysql",
            database="python",
            port="3308"
        )
        cursor=mydb.cursor()

    def query(self,sql,val=[]):
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()


    def update(self,sql,val):
        self.cursor.execute(sql, val)
        self.mydb.commit()

#修改

val=input("请输入修改的图书id")
print("1书名 2价格 3出版社 4地址")
label=["","name","price","publish","address"]
input=input("请输入要修改的编号")
val=input("请输入修改后的值")

sql="update book set"+label[input]+"="+val+"where book id=xx""


#查询，分页查询
#默认显示第一页
input=input("请按n显示下一页，按b退出")
page=1

start=(page-1)*10

sql="select*from book limit"+"start"+",10"