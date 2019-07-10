print( ord('A') )
print( chr(65) )
print( ord('中') )
print( chr(25529) )
result="abcd".capitalize()
print(result)
str="中国牛逼中国优秀中国牛逼"
count=str.count("中国")
print(count)
print("zzjynb".endswith("nb"))
print("zzjynb".find("n"))
print("ukyjtdhrewED比较快casjrehguifsdjkaetrhyi土洋结合瑞特给我发的".isalpha())
print("765432".isdigit())
print("6543Grfed".isalnum())
print("juyhe23rffrrefrgegererg在一tgr".islower())
print("A123啊啊啊".isupper())
print("htgrfedTGRFEDWSQ".lower())
print("htgrfedTGRFEDWSQ".upper())
print(" as df f  g er  3 f er".lstrip())
print(" as df f  g er  3 f er".rstrip())
print(" as df f  g er  3 f er".strip())
print(" as df f  g er  3 f er".replace(" ",""))
import re
#result=re.match(r"a","abc")
#result=re.findall(r"a","ashuwuveywbaaadratfayguahijaoe")
#print("\n")
#print(result)
q=re.match(r"[0-9A-Za-z]+","aweasrdtfyguhijovgchdfjbkggc")
print(q)
if(q):
    print("ok")

# 允许2位小数
q=re.match("[1-9][0-9]*\.[0-9][1-9]","1000.11")
print(q)
# 允许汉字英文和数字，数字不能再最前（汉字：^[\u4e00-\u9fa5]{0,}$）
w=re.match("^([\u4e00-\u9fa5]|[a-z]|[A-Z])([\u4e00-\u9fa5]|[a-z]|[A-Z]|[0-9])*","在rgtfrudgnuegu67834dfwnkwerbg没给你买啥地方JHGHFXSD")
print(w)
# 固定电话
e=re.match("^8[0-9]{7}$","85746140")
print(e)
# 身份证号
r=e=re.match("^[0-9]{17}([0-9]|X)$","22010623456780348X")
print(r)
