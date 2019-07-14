from bs4 import BeautifulSoup
import requests
#for i in range(10):
url="http://www.techweb.com.cn/roll/list_1.shtml"
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
n=soup.find("div",class_="newslist")
print(n.get_text())