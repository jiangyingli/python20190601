
from 姜英利.class75.DB import mysqlconn


# 新增，删除

#修改


# print("ss", end="")

# 修改，
# val = input("请输入修改的图书id")
# # 显示
# print("1书名    2价格    3出版社    4地址")
# label = ["","name","price","publish","address"]
# input = input("请输入要修改的编号")
# 2
# val = input("请输入修改后的值")
#
# sql =  "update book set "+label[input]+" = "+val+" where book_id=xx""

# 查询，分页查询

# 默认显示第一页
# input = input("请按n显示下一页，按b退出")
page = 2

start = (page-1)*10

sql = "select * from book limit "+str(start)+" , 10"

print(sql)
