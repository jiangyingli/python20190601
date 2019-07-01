# 扩展名，后缀名
# 操作系统明确文件类型用的，选择用啥工具打开



# IO，读写操作（文件，网络）
# 参数1：文件路径+文件名
# 参数2：模式（只读，读写，二进制）
# file = open("c:/test/a.txt","r")#以只读方式打开文件，文本方式
# str = file.read()
# print(str)

# file = open("c:/test/a.txt", "w")#以写的模式打开
# file.write("我是写入的内容")

# file = open("c:/test/a.txt", "a")#以追加写的模式打开
# file.write("重新写入内容")

# file = open("c:/test/a.txt", "a")#以追加写的模式打开
# file.write("指定位置写入")

# file.seek( 6 )
# a=file.tell()


# file = open("c:/test/a.txt","r")#以只读方式打开文件
#
# while( True ):
#     str = file.read(6)   #读取6个字符
#     if(str == ""):
#         break
#     print(str)
# print(str)
# 换行符
# file = open("c:/test/a.txt","r")#以只读方式打开文件
# while(True):
#     str = file.readline()
#     if(str == ""):
#         break;
#     print(str,end="")

# file = open("c:/test/a.txt","r")#以只读方式打开文件
# lines = file.readlines()
#
# for p in lines :
#     print(p,end="")
#
# file.close()



