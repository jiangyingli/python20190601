from bs4 import BeautifulSoup
import requests
url='https://cc.58.com/chuzu/?utm_source=market&spm=b-31580022738699-pe-f-833.daohangqq_101&PGTID=0d100000-0013-fcc8-9e21-ecaf2be42ac7&ClickID=2'
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
grid_view = soup.findAll("div",class_= "des")
for i in range( len(grid_view)) :

    print(grid_view[i].get_text())