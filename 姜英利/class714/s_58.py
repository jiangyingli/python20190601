import re
import base64
from fontTools.ttLib import TTFont
from 姜英利.class714.fanpa import  get_dict
import requests
from bs4 import BeautifulSoup
# 根据


def replacestr(map,str1):
    for row in map:
        str1=str1.replace(row, str(map.get(row)))
    return str1

url = 'https://cc.58.com/chuzu/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0013-f616-c21b-fa761cdaebbd&ClickID=2'
html = requests.get( url )# 把链接所在页面数据获取到

html.encoding = html.apparent_encoding    #设置编码
# print(r.text)
soup = BeautifulSoup( html.text ,'html.parser')
map = get_dict(html.text)
# for key in map :
#     print(key,map.get(key))

lis = soup.find_all("li",class_="house-cell")

for li in lis :
    roomp = li.find("p",class_="room")
    room = replacestr( map  , str( roomp.get_text() ))
    room1 = room.split()[0]
    room2 = room.split()[1]
    print("户型:",room1)
    print("面积:",room2)

    titlep = li.find("h2").find("a").get_text().strip()
    titlep = replacestr(map,titlep)

    type = titlep.split("|")[0]
    title = titlep.split("|")[1]
    print("出租类型：",type.strip())
    print("主题：",title.strip())

    money = li.find("b",class_="strongbox").string

    money = replacestr(map,money)
    print("价格：",money)
    break;


