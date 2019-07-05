import mysql.connector
def update(sql,val=[]):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="12345",
        port="3308"
    )
    cursor = mydb.cursor()
    cursor.execute(sql, val)
    mydb.commit()
    update("insert into book(b_number,b_name,b_author,b_price,b_author_address,b_author_message)values(%s,%s,%s,%s,%s,%s)",val)
    val=[input("请输入修改编码\n"),input("请输入修改书名\n"),input("请输入修改作者")]
    update("insert into book(b_number,b_name,b_author)values(%s,%s,%s)",val)




def quary(sql):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="12345",
        port="3308"
    )
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor
row = quary("select * from book")
print(row)



val=[input("请输入书名\n")+"%"]
row2=quary("select*from book where b_name like %s",val)
print(row2)

