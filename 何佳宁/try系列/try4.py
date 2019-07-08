import mysql.connector
class mysqlconn:
    cursor = None
    mydb=None
    def __init__(self):
        self.mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database="python",
            port="3308"
        )
        self.cursor=self.mydb.cursor()

    def query(self,sql,val=[]):
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()


    def update(self,sql,val):
        self.cursor.execute(sql, val)
        self.mydb.commit()

#修改

cmd1=input("请输入修改的图书id")
print("1书名 2价格 3出版社 4作者")
label=["","b_name","b_price","b_publish","b_author"]
cmd2=input("请输入要修改的数字")
val=input("请输入修改后的信息")

sql="update book set "+label[int(cmd2)]+"=%s where b_code=%s"
db=mysqlconn()
db.update(sql , [val,cmd1])



#查询，分页查询
#默认显示第一页
input=input("请按n显示下一页，按b退出")
page=1

start=(page-1)*10

sql="select*from book limit"+str(start)+",10"