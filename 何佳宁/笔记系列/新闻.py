from bs4 import BeautifulSoup
import requests

url ='http://www.techweb.com.cn/roll/'
r = requests.get(url)
r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.text,'html.parser')
lis=soup.find("div",class_="newslist")


title=lis.find_all("span",class_="tit").get_text(strip="True")
#column=lis.find_all("span",class_="column").get_text(strip="True")
#source=lis.find_all("span",class_="source").get_text(strip="True")
#time=lis.find_all("span",class_="time").get_text(strip="True")


for i in range(len(title)):
    print(title(i))
