from 李其威作业 import 数据库 as a
val=["r_001"]
b=a.query("select * from check_out where r_code=%s",val)
print(b)
#删
a.update("delete from check_out where r_code =%s",val)
#增

val=["1","1","200-1-1","1-1-1"]
a.update("insert into check_out values(%s,%s,%s,%s)",val)