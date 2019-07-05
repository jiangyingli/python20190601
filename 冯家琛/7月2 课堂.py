'''
import mysql.connector
mydb = mysql.connector.connect(
    host= "localhost",#设置数据库IP地址，localhost表示本机 127.0.0.1 表示本机
    user = "root",#连接MySQL数据库的账号，root是最高管理员
    passwd = "mysql",
    database ="jintian",#连接的数据库实例
    port = "3308"#端口
)

cursor = mydb.cursor()#数据库操作
code = input("")
name = input("")
sex = input("")
dep = input("")
sql = "insert into reader(r_code,r_name,r_sex,r_dep) values (%s,%s,%s,%s)"
val = (code, name, sex, dep)
cursor.execute(sql, val)
mydb.commit()
'''
import mysql.connector
mydb = mysql.connector.connect(
        host= "localhost",#设置数据库IP地址，localhost表示本机 127.0.0.1 表示本机
        user = "root",#连接MySQL数据库的账号，root是最高管理员
        passwd = "mysql",
        database ="jintian",#连接的数据库实例
        port = "3308"#端口
)
cursor = mydb.cursor()

cursor.execute("select * from reader")
rows = cursor.fetchall()
print(rows)

for i in range(len(rows)):
    str = rows[i]
    for j in range(len(str)):
        print(str[j],end=" ")
    print()

for str in rows:
    for prop in str:
        print (prop,end=" ")
    print()

