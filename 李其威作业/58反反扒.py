import re
import base64
from fontTools.ttLib import TTFont
import requests
from bs4 import BeautifulSoup
# 根据
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


url = 'https://cc.58.com/chuzu/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0013-f616-c21b-fa761cdaebbd&ClickID=2'
html = requests.get( url )# 把链接所在页面数据获取到

html.encoding = html.apparent_encoding    #设置编码
# print(r.text)
soup = BeautifulSoup( html.text ,'html.parser')

map = get_dict(html.text)

# for row in map :
#     print(row , map.get(row))
grid_view = soup.findAll("div", class_="des")

for i in range(len(grid_view)):
    ss = grid_view[i].get_text()
    for row in map:
        ss = ss.replace(row , str(map.get(row)))

    print(ss)