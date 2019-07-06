import mysql.connector
def quary(sql,val=[]):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="12345",
        port="3308"
    )
    cursor = mydb.cursor()
    cursor.execute(sql,val)
    return cursor.fetchall()


#val9=["1001"]
#row = quary("select * from reader where r_code=%s",val9)
#print(row)
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
    update("insert into reader()values")



