# 汉字的编码
ord('A')
ord('中')

# 编码的汉字
chr(66)
chr(25991)

# 十六进制也是可以的
s = '\u4e2d\u6587'
print(s)

# 字符串长度
len('ABC')
len('中文')

# capitalize()
# 将字符串的第一个字符转换为大写
#
# count(str, beg= 0,end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
#
# endswith(suffix, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
#
# find(str, beg=0, end=len(string))
# rfind()
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
#
# isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
#
#
# isdigit()
# 如果字符串只包含数字则返回 True 否则返回 False..
#
# isalnum()
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
#
# islower()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
#
# isupper()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
#
# lower()
# 转换字符串中所有大写字符为小写.
#
# upper()
# 转换字符串中的小写字母为大写
#
# strip()前后
# rstrip()后
# lstrip()前
# 删除字符串的空格.
#
# split(str="", num=string.count(str))
# num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串


