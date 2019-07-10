import mysql.connector
class mysqlconn:
    cursor = None
    mydb = None
    def __init__(self):#  构造方法：创建对象自动调用1次，
        print(123)
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database="python",
            port="3308"
        )
        self.cursor = self.mydb.cursor()

    def query(self, sql ,val=[] ):
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()

    def update(self,sql,val):
        self.cursor.execute(sql, val)
        self.mydb.commit()

t = mysqlconn()