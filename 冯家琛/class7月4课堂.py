import mysql.connector
def query( sql , val):
    mydb = mysql.connector.connect(
        host="localhost",  # 设置数据库IP地址，localhost表示本机 127.0.0.1 表示本机
        user="root",  # 连接MySQL数据库的账号，root是最高管理员
        passwd="mysql",
        database="jintian",  # 连接的数据库实例
        port="3308"  # 端口
    )
    cursor = mydb.cursor()
    cursor.execute(sql,val)
    return cursor.fetchall()


def add( sql , val):
    mydb = mysql.connector.connect(
        host="localhost",  # 设置数据库IP地址，localhost表示本机 127.0.0.1 表示本机
        user="root",  # 连接MySQL数据库的账号，root是最高管理员
        passwd="mysql",
        database="jintian",  # 连接的数据库实例
        port="3308"  # 端口
    )
    cursor = mydb.cursor()
    cursor.execute(sql,val)
