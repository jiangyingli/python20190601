import mysql.connector
class mysqlconn:
    cursor=None
    mydb=None
    def __init__(self):#创建对象自动调用1次
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database="12345",
            port="3308"
        )
        cursor = mydb.cursor()


def quary(self,sql,val=[]):
    self.cursor.execute(sql,val)
    return self.cursor.fetchall()

#print("1 书名   2价格  3出版社")
#label=["","name","price"，"publish"]
#input=input("")
def update(self,sql,val=[]):
    self.cursor.execute(sql, val)
    self.mydb.commit()


#查询
#input=input("请按n显示下一页，按b退出")

page=1
start=(page-1)*10
sql="select * from book limit "+str(start)+",10"

#HTML:超文本标记语言（做网页）
#用文本方式标记编码，效果比文本丰富


