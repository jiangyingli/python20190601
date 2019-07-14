from bs4 import BeautifulSoup
import requests
url='https://movie.douban.com/top250'
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
grid_view = soup.find("ol",class_= "grid_view")
print(grid_view.text.replace(" ",""))