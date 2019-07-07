import mysql.connector

mydb=mysql.connector.connect(
        host="localhost",#localhost,127.0.0.1
        user="root",#账号，
        passwd="mysql",
        database="12345",
        port="3308"
)
#操作对象
#cursor=mydb.cursor()
#code="1009"
#name="王文英"
#sex="女"
#dep="财务部"
#sql="insert into reader(r_code,r_name,r_sex,r_dep)values(%s,%s,%s,%s)"
#val=(code,name,sex,dep)
#cursor.execute(sql,val)
#mydb.commit()
#查询
#cursor=mydb.cursor()

#cursor.execute("select*from reader")
#rows=cursor.fetchall()
#for i in range(len(rows)):
 #   one=rows[i]
  #  for j in range(len(one)):
   #     print(one[j],end="")
    #print()


#for one in rows:
    #for prop in one:
     #   print(prop,end="")
    #print("")




def quary(sql):

        mydb = mysql.connector.connect(
            host="localhost",  # localhost,127.0.0.1
            user="root",  # 账号，
            passwd="mysql",
            database="12345",
            port="3308"
        )
        cursor=mydb.cursor()
        cursor.execute(sql)
        return cursor
row=quary("select*from reader")
print(row)









