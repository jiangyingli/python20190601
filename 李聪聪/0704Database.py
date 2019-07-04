import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="lcccccc",
        port="3308"
    )
cursor = mydb.cursor()
