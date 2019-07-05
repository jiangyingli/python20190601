import mysql.connector
class mysqlcon:
    cursor= None
    mydb= None
    def _init_(self):
        self.mydb = mysql.connector.connect(
            host="localhost",  # 设置数据库的ip地址，localhost,或127.0.0.1表示本机
            user="root ",  # 账号，root 是超级管理员
            passwd="mysql",  # 密码
            database="python01",  # 连接的数据库实例
            port="3308"
        )
        cursor = self.mydb.cursor()
    def query(self,sql,val=[]):
        self.cursor.execute(sql,val)
        return self.cursor.fetchall()
    def update(self,sql,val=[]):
        self.cursor.execute(sql,val)
        self.mydb.commit()
