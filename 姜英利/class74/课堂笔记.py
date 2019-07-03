import mysql.connector

#连接数据库
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="mysql",  # 数据库密码
    database="python",
    port="3308"
)
mycursor = mydb.cursor()
# 执行增删改
sql = "INSERT INTO student (number,name,sex,birthday,address,height) VALUES (%s,%s,%s,%s,%s,%s)"
val = ("1004","王五","男","2000-02-02","吉林长春","180")
mycursor.execute(sql, val)

mydb.commit()

# 执行查询

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)

