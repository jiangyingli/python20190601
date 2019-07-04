import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="whr123",
    port="3308"
)
cursor = mydb.cursor()



def query(sql,val=[]):
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




while( True ):
    com = int(input("1，新增图书    2，查看已有图书     3，查看特定图书（模糊查询）    4，修改图书信息   5，退出"))
    if com==1:
        a = input("code")
        b = input("name")
        c = input("author")
        d = input("publish")
        f = input("date")
        g = input("price")
        val = [a, b, c, d, f, g]
        update("insert into book values(%s,%s,%s,%s,%s,%s)", val)
    elif com==2:
        rows = query("select * from book ")
        for i in range(len(rows)):
            list = rows[i]
            for j in range(len(list)):
                print(list[j], end=" ")
            print()
    elif com==3:
        str = input("模糊查询，输入书名中任意字")
        val = ["《"+"%"+str+"%"+"》"]
        rows = query("select * from book where b_name like %s", val)
        for i in range(len(rows)):
            list = rows[i]
            for j in range(len(list)):
                print(list[j], end=" ")
            print()
    elif com==4:
        a = input("欲修改的图书编号")
        b = int(input("欲修改的项目 1,name 2,author 3,publish 4,date 5,price  "))
        c = input("更正后的信息")
        if b==1:
            update("update book set b_name=\"c\" where b_code=\"a\"")
        elif b==2:
            update("update book set b_author=\"c\" where b_code=\"a\"")
        elif b==3:
            update("update book set b_publish=\"c\" where b_code=\"a\"")
        elif b==4:
            update("update book set b_date=\"c\" where b_code=\"a\"")
        elif b==5:
            update("update book set b_price=\"c\" where b_code=\"a\"")
        mydb.commit()
    elif com==5:
        break;