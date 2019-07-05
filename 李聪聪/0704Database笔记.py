import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", #localhost或127.0.0.1表示本机，设置数据库的IP地址
    user="root", #账号，root是超级管理员
    passwd="mysql", #密码
    database="lcccccc", #链接的数据库实例
    port="3308" #端口
)
'''
print(mydb)

cursor=mydb.cursor()  #数据库操作对象
code=input("输入code")
name=input("输入name")
sex=input("输入sex")
dep=input("输入dep")
sql="insert into reader(r_code,r_name,r_sex,r_dep) values(%s,%s,%s,%s)"
val=(code,name,sex,dep)
cursor.execute(sql,val)
mydb.commit()  #提交生效
'''
'''
#查询
cursor=mydb.cursor()
cursor.execute("select * from reader" )
rows=cursor.fetchall() #列表套元祖
for i in range(len(rows)):
    one=rows[i]  #得到元祖
    for j in range(len(one)):
        print(one[j],end=" ")
    print()
for one in rows:
    for prop in one:
        print(prop,end=" ")
    print()
'''
'''
#查询
def query(sql,val=[]):
    mydb = mysql.connector.connect(
        host="localhost",  # localhost或127.0.0.1表示本机，设置数据库的IP地址
        user="root",  # 账号，root是超级管理员
        passwd="mysql",  # 密码
        database="lcccccc",  # 链接的数据库实例
        port="3308"  # 端口
    )
    cursor = mydb.cursor()
    cursor.execute(sql,val)   #val是列表或者[val]，val是字符串
    return cursor.fetchall()

#from 李聪聪 import 0704 as kt
#rows=kt.query("")

val=["1001"]
rows=query("select * from reader where r_code=%s ",val)
rows=query("select * from reader ")
print(rows)
'''

#更新：增删改
def update(sql,val=[]):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="lcccccc",
        port="3308"
    )
    cursor = mydb.cursor()
    cursor.execute(sql,val)
    mydb.commit()

#update("update reader set r_name='张四' where r_code='1001'")
#val=['1005','小明','男','财务部']
#update("insert into reader(r_code,r_name,r_sex,r_dep) values(%s,%s,%s,%s)",val)

code=input("输入code")
name=input("输入name")
sex=input("输入sex")
dep=input("输入dep")
val=[code,name,sex,dep]
update("insert into reader(r_code,r_name,r_sex,r_dep) values(%s,%s,%s,%s)",val)
