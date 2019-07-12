from bs4 import BeautifulSoup
import requests
for i in range(2):
    url='http://www.techweb.com.cn/roll/list_'+str(i+1)+'.shtml'
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,'html.parser')
    newslist_divs = soup.find("div",class_= "newslist")
    li=newslist_divs.find_all("li")
    print(str(newslist_divs.text).replace(" ",""))
    #print(newslist_divs.get_text("\n",strip="True"))