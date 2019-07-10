'''
s = "aaaa".capitalize()
print(s)

s = "abcabcd".count("a",1,9)
print(s)

print("abcde".endswith("def"))

print("abcde".find("bc"))

print("abcdecf".rfind("c"))

print("aaa是".isalpha())

print("123①②".isdigit())

print("aaa是123①".isalnum())

print("aa".upper())

print("  aa  ".lstrip())
print("  aa  ".rstrip())
print("  aa  ".strip())
'''

import re
print(re.match("^[-]?\d*.\d{2}$","-1.12"))

test = '用户输入的字符串'
print(re.match(r'正则表达式', test))



