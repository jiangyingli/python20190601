


#正则表达式

import re

v = re.match(r"([1-9]+[0-9]*\.[0-9]*[1-9]$|[0-9]\.[0-9]*[1-9])", "02.04")
print(v)


v = re.match(r"^[a-zA-Z\u4e00-\u9fa5][0-9a-zA-Z\u4e00-\u9fa5]*","4ac5")
print(v)

v = re.match(r"8[0-9]{7}","80000353")
print(v)

v = re.match(r"[0-9]{18}","220106200110241018")
print(v)