import re
import base64
from fontTools.ttLib import TTFont
import requests

def get_dict(html):
    base64_str = re.search(r'base64,(.*?)\)', html, re.S).group(1)
    base64_str_decode = base64.b64decode(base64_str)
    filr_name = "58.ttf"
    with open(filr_name, 'wb') as f:
        f.write(base64_str_decode)
    font = TTFont('58.ttf')  # 打开本地的ttf文件
    font.saveXML('58.xml')  # 转换成xml
    cmap = font['cmap'].getBestCmap()
    newdict = {}
    for i in cmap:
        pat = re.compile(r'(\d+)')
        values = int(re.search(pat, cmap[i])[1]) - 1
        keys = chr(i)
        newdict[keys] = values
    return newdict