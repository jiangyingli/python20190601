import re
# 导入re模块

# 正则表达式强项：明确格式，规则
# 弱项：处理逻辑

# 参数1，规则
# 参数2，带匹配字符串
# 参数3，匹配模式（）
#     re.I	使匹配对大小写不敏感
#     re.L	做本地化识别（locale-aware）匹配
#     re.M	多行匹配，影响 ^ 和 $
#     re.S	使 . 匹配包括换行在内的所有字符
#     re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
#     re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

# re.match #从开始位置开始匹配，如果开头没有则无
# result = re.match( r"a" , "abc" )
# print(result)

# print(r"\n")

# re.search #搜索整个字符串
# result = re.search( r"a" ,"bbabc")
# print(result)
#
# # re.findall #搜索整个字符串，返回一个list
# result = re.findall(r"a" , "bbaccaddad")
# print(result)
#
# # re.I 忽略大小写
# result = re.match(r"a" , "Abb" , re.I)
# print(result)

# 规则表
# ^	匹配字符串的开头
# $	匹配字符串的末尾。

# v=re.match(r"^a$","abc")
# print(v)

# .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# v=re.match(r"^t.m$","tom")
# if(v):
#     print("该名可用")
# else :
#     print("不能用")

# [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# v=re.match(r"^t[aoeiu]m$","tkm")
# print(v)

# [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# v=re.match(r"^t[^aoeiu]m$","tam")
# print(v)

# re*	匹配0个或多个的表达式。
# v=re.match(r"^t[aoeiu]*m$","tm")
# print(v)
# re+	匹配1个或多个的表达式。
# re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# re{ n}
# v=re.match(r"^t[aoeiu]{3}m$","taoim")
# print(v)
# re{ n,}	精确匹配n个前面表达式。
# re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# a| b	匹配a或b
# (re)	G匹配括号内的表达式，也表示一个组

# v=re.match(r"^t(e|al|ea){2}m$","teaem")
# print(v)
#所有英文，中文都可以
# v=re.match(r"[0-9a-zA-Z\u4e00-\u9fa5]+","fdsafdsa")
# print(v)

# print("\u4e00-\u9fa5")
# for i in range(19968,40869):
#     print(chr(i),end=" ")
#     if(i%20==0):
#         print()

# 实例	描述
# python	匹配 "python".
# [Pp]ython	匹配 "Python" 或 "python"
# rub[ye]	匹配 "ruby" 或 "rube"
# [aeiou]	匹配中括号内的任意一个字母
# [0-9]	    匹配任何数字。类似于 [0123456789]
# [a-z]	    匹配任何小写字母
# [A-Z]	    匹配任何大写字母
# [a-zA-Z0-9]	匹配任何字母及数字
# [^aeiou]	除了aeiou字母以外的所有字符
# [^0-9]	匹配除了数字外的字符

# 实例	描述
# .	    匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
# \d	匹配一个数字字符。等价于 [0-9]。
# \D	匹配一个非数字字符。等价于 [^0-9]。
# \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
# v = re.match(r"^\d\s\d$","1 2")

# print(v)
# 练习：
# 校验时间
# t = '19:05:30'
# 时间：

v = re.match("([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]","3:59:34")
print(v)

# 校验邮箱  "^[\w]+@[\w]+\.[\w]+$"
# 非0开头的数[^0][0-9]*
# 允许2位小数

v=re.match("^[1-9][0-9]*\.[0-9][1-9]$","1.11")
print(v)
# 允许汉字英文和数字，数字不能再最前（汉字：^[\u4e00-\u9fa5]{0,}$）
v=re.match("^([\u4e00-\u9fa5]|[a-z]|[A-Z])([\u4e00-\u9fa5]|[a-z]|[A-Z]|[0-9])*$","sfdf65")
print(v)
# 固定电话
v=re.match("^8[0-9]{7}$","81111111")
print(v)
# 身份证号
v=e=re.match("^[0-9]{17}([0-9]|X)$","22010420000000000X")
print(v)
