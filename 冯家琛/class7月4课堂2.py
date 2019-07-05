from 冯家琛 import class7月4课堂 as kt
#val=["1001"]
#rows = kt.query("select * from reader where r_code=%s",val)

val =["1004", "cc", "男", "物理"]
kt.add("insert into reader(r_code,r_name,r_sex,r_dep) values(%s,%s,%s,%s)", val)
val = ["1004"]
kt.update("delete from reader where r_code=%s",val)

