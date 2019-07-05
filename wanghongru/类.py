class mysqlconn:
    cursor = None
    mydb = None
    def _inti_(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database="whr123",
            port="3308"
        )
        cursor = mydb.cursor()


    def query(self,sql,val=[]):
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    def update(self,sql,val=[]):
        self.cursor.execute(sql, val)
        self.mydb.commit()