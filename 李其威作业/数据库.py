import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",#设置数据库的ip地址，localhost,或127.0.0.1表示本机
    user="root ",#账号，root 是超级管理员
    passwd="mysql",#密码
    database="python01",#连接的数据库实例
    port="3308"
)
#数据库的操作对象
#增，删，改
'''
cursor = mydb.cursor()
code=int(input("编号"))
name=input("姓名")
sex=input("性别")
dep=input("部门")
sql=("insert into reader (r_code ,r_name,r_sex,r_dep) values (%s,%s,%s,%s)")
val = (code,name,sex,dep)
cursor.execute(sql,val)
mydb.commit()

#查询
cursor = mydb.cursor()
cursor.execute("select * from reader")
rows=cursor.fetchall()
for i in range(len(rows)):
    for j in range(4):
        print(rows[i][j] ,end=" ")
    print()
'''


def query(sql,val=[]):
    mydb = mysql.connector.connect(
        host="localhost",  # 设置数据库的ip地址，localhost,或127.0.0.1表示本机
        user="root ",  # 账号，root 是超级管理员
        passwd="mysql",  # 密码
        database="python01",  # 连接的数据库实例
        port="3308"
    )
    cursor = mydb.cursor()
    cursor.execute(sql,val)
    return cursor.fetchall()
def update(sql,val=[]):
    mydb = mysql.connector.connect(
        host="localhost",  # 设置数据库的ip地址，localhost,或127.0.0.1表示本机
        user="root ",  # 账号，root 是超级管理员
        passwd="mysql",  # 密码
        database="python01",  # 连接的数据库实例
        port="3308"
    )
    cursor = mydb.cursor()
    cursor.execute(sql,val)
    mydb.commit()

