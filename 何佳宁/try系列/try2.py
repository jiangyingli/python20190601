#SQL语句操作数据
import mysql.connector
def query(sql,val):
    mydb=mysql.connector.connect(
        host="localhost",#设置数据库的IP地址，localhost，127.0.0.1表示本机
        user="root",#账号，root是超级管理员
        passwd="mysql",#密码
        database="python",#连接的数据库实例
        port="3308"#端口
    )
    #mydb.commit()  # 提交生效，不提交不生效
    #数据库的操作对象
    #增，删，改数据都可用
    cursor=mydb.cursor()
    cursor.execute(sql,val)
    return cursor.fetchall()

    '''
    code="1009"
    name="王文英"
    sex="女"
    dep="财务部"
    sql="insert into reader(r_code,r_name,r_sex,r_dep)values(%s,%s,%s,%s)"
    val=(code,name,sex,dep)
    cursor.execute(sql,val)

#sor.execute("insert into reader(r_code,r_name,r_sex,r_dep)values ('1001','张三','男','研发部门')")


#查询
cursor=mydb.cursor()
cursor.execute("select*from reader")
rows=cursor.fetchall()
print(rows)

for i in range(len(rows)):
    one=rows[i]
    for j in range (len(one)):
        print(one[j],end=" ")
    print()

for one in rows:
    for prop in one:
        print(prop)

'''





def update(sql,val):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="python",
        port="3308"
    )
    cursor=mydb.cursor()
    cursor.execute(sql,val)
    mydb.commit()