import mysql.connector
def query(sql,val=[]):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="zjy1",
    port="3308"
    )
    cursor=mydb.cursor()
    cursor.execute(sql,val)
    return cursor.fetchall()


def update(sql,val=[]):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="zjy1",
        port="3308"
    )
    cursor=mydb.cursor()
    cursor.execute(sql,val)
    mydb.commit ()