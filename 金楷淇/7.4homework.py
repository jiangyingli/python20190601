
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="python",
    port="3308"
)
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

def yiyou():
    cursor = mydb.cursor()
    cursor.execute("select*from book")
    rows = cursor.fetchall()
    for i in range(len(rows)):
        one = rows[i]
        for j in range(len(one)):
            print(one[j], end=" ")
        print()
def xinzeng():
    a=input("请输入code")
    b=input("请输入name")
    f = input("作者")
    c=input("请输入出版社")
    d=input("请输入日期")
    e=input("请输入价格")

    cursor = mydb.cursor()
    code = a
    name = b
    author=f
    pub = c
    date = d
    price=e
    sql = "insert into book(b_code,b_name,b_author,b_publish,b_pubdate,b_price) values(%s,%s,%s,%s,%s,%s)"
    val = (code, name, author, pub, date,price)
    cursor.execute(sql, val)
    mydb.commit()

def teding():
    shuming=input("请大致输入书本的名字")
    val=[shuming]
    a=query("select * from book where b_name like %s % ",val)
    for i in range(len(a)):
        for j in range(i):
            print(a[i][j], end=" ")
            print()
cmd=str(input("请输入指令 1.新增图书 2.查看已有图书 3.查看特定图书\n"))
if(cmd=="1"):
     xinzeng()
elif(cmd=="2"):
     yiyou()
elif(cmd=="3"):
     teding()