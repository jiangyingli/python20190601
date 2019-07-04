from 张佳源 import 数据库函数 as kt
#code=input("code")
#name=input("name")
#sex=input("sex")
#dep=input("dep")
#val =[code,name,sex,dep]
#rows = kt.query("select * from reader where r_code like %s ",val)
#print(rows)
#kt.update("insert into reader (r_code ,r_name,r_sex,r_dep) values('r_012','刘文刀','男','技术部') ")
#kt.update("delete from reader where r_code='r_012' ")
val=["a","a","a","a"]
kt.update("insert into reader  values (%s,%s,%s,%s) ",val)

'''
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="zjy1",
    port="3308"
)
cursor=mydb.cursor()
cursor.execute("select * from reader")
rows=cursor.fetchall()

a=len(rows)
for i in range(a):
    for j in range(4):
        print(rows[i][j],end="    ")
    print()

for one in rows:
    for prop in one:
        print(prop,end="   ")
    print()


code="r_010"
name="王乌昂"
sex="女"
dep="财务部"
sql="insert into reader (r_code ,r_name,r_sex,r_dep) values (%s,%s,%s,%s)"
val=(code,name,sex,dep)
cursor.execute(sql,val)

mydb.commit()
'''