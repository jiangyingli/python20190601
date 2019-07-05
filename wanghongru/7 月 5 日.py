import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="whr123",
    port="3308"
)
cursor = mydb.cursor()




'''

#cursor.execute("insert into reader (r_code,r_name,r_sex,r_dep) values('r_008','张三','男','开发部')")
a = input()
b = input()
c = input()
d = input()

sql = "insert into reader (r_code,r_name,r_sex,r_dep) values(%s,%s,%s,%s)"
val = (a, b, c, d)
cursor.execute(sql, val)



mydb.commit()




cursor.execute("select * from reader")
rows = cursor.fetchall()
for i in range(len(rows)):
    list = rows[i]
    for j in range(len(list)):
        print(list[j],end=" ")
    print()
'''
def query(sql,val):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="whr123",
        port="3308"
    )
    cursor = mydb.cursor()

    cursor.execute(sql,val)

    return cursor.fetchall()
'''
val = [ "r_010" ]
rows = query("select * from reader where r_code=%s",val)
for i in range(len(rows)):
    list = rows[i]
    for j in range(len(list)):
        print(list[j],end=" ")
    print()
'''


def update( sql , val=[]):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="whr123",
        port="3308"
    )
    cursor = mydb.cursor()

    cursor.execute( sql ,val)
    mydb.commit()

a = input("r_code")
b = input("r_name")
c = input("r_sex")
d = input("r_dep")
val = [a,b,c,d]
update("insert into reader values(%s,%s,%s,%s)",val)

update("delete from reader where r_code= \"r_008\" ")

update("update reader set r_dep=\"竞赛部\" where r_name=\"魏斌\"")