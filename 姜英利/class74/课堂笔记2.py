import mysql.connector
#查询，执行所有查询命令，返回查询结果
#1，命令本身（SQL语句）
# 2，值，给SQL语句替换占位符的
def query( sql ,val=[] ):
    mydb = mysql.connector.connect(
        host="localhost",  # 设置数据库的IP地址，localhost，127.0.0.1表示本机，
        user="root",  # 账号，root是超级管理员
        passwd="mysql",  # 密码
        database="python",  # 连接的数据库实例
        port="3308"  # 端口
    )
    cursor = mydb.cursor()
    cursor.execute(sql,val)#execute方法是python语言自带的，要求2参数，1sql，2占位符的值
    return cursor.fetchall()

#增删改，更新
def update(sql,val):
    mydb = mysql.connector.connect(
        host="localhost",  # 设置数据库的IP地址，localhost，127.0.0.1表示本机，
        user="root",  # 账号，root是超级管理员
        passwd="mysql",  # 密码
        database="python",  # 连接的数据库实例
        port="3308"  # 端口
    )
    cursor = mydb.cursor()
    cursor.execute(sql, val)  # execute方法是python语言自带的，要求2参数，1sql，2占位符的值
    mydb.commit()

