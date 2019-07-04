from 姜英利.class74 import 课堂笔记2 as kt

val = ["1001"]

# rows = kt.query( "select * from reader where r_code=%s", val )
rows = kt.query( "select * from reader ")

kt.update("delete from reader where r_code=%s",["1001"])

# 1，键盘输入N个值，存入数据库

# 1，做一个界面，1，新增图书    2，查看已有图书     3，查看特定图书（模糊查询）    4，修改图书信息
# 2，选做：查看已有图书，分页显示，每页显示5条，
