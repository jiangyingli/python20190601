# 汉字的编码
# print( ord('A') )
# print( ord('中') )
# 编码：早期ASCII编码，只有128个字符，UNICODE编码：65535个字符，2字节，
# UTF-8，GBK
# 练习：已知一个字符串“abc”,求他们的编码
# 编码的汉字
# print( chr(66))
# chr(25991)

# 十六进制也是可以的
# s = '\u4e2d\u6587'
# print(s)

# for i in range( 65536 ):65536
# print(55296,chr(55296),end=" ")
    # if(i%50==0):
    #     print()

# 字符串长度
# print(len('ABC'))
# print(len('中文'))

# capitalize()
# 将字符串的第一个字符转换为大写
# result = "abcd".capitalize()
# print(result)

# count(str, beg= 0,end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
# str="我们都有一个家名字叫中国，啊中国是我的祖国，中国最好"
# count = str.count("中国")
# print(count)

# endswith(suffix, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
# print("世界你好".endswith("你好"))


# find(str, beg=0, end=len(string))左-》右
# rfind()右-》左
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
# print("你好a你好b你ca好".rfind("aw"))

# isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
# print( "fdsafdsa少时诵诗书".isalpha() )

# isdigit()
# 如果字符串只包含数字则返回 True 否则返回 False..
# print("12345①②".isdigit())

# isalnum()
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
# print("aa是是是111".isalnum())

# islower()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
# print("abc".islower())
# isupper()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# print("AAA啊".isupper())
# lower()
# 转换字符串中所有大写字符为小写.
# print("AbAe".lower())
if("abCde"=="aBcde"):
    print("相等")
else:
    print("不等")

# upper()
# 转换字符串中的小写字母为大写

# strip()前后
# rstrip()后
# lstrip()前
# 删除字符串的空格.
print("  a   a  a    ".lstrip())
print("  a a  a    ".rstrip())
print("  a a a    ".strip())

print( " a b c d ".replace(" ",""))

# split(str="", num=string.count(str))
# num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串


