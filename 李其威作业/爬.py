from bs4 import BeautifulSoup
import requests
url="https://so.gushiwen.org/authors/authorvsw.aspx?page=1&id=b90660e3e492"
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
v=soup.find_all("div",class_="contson").get_text("\n",strip="True")
n=soup.find_all("a",target="_blank")

g=soup.find_all("p",class_="source")
for i in range(len( v)):
    print(n[i*2+1].text)
    print(g[i].text)
    print(v[i])
    print("--------------------------------------")



