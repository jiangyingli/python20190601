from bs4 import BeautifulSoup
import requests

url = 'https://so.gushiwen.org/authors/authorvsw.aspx?page=1&id=b90660e3e492'
r = requests.get(url)
r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.text,'html.parser')
son_divs = soup.find_all("div",class_="sons")

for sdiv in son_divs:
    count_div = sdiv.find("div",class_="cont")
    title = count_div.find_all("p")[0].a.b.string
    dynasty = count_div.find_all("p")[1].find_all("a")[0].string
    author = count_div.find_all("p")[1].find_all("a")[1].string
    content = count_div.find_all("div")[-1].get_text()
    

    print(title,'\t',author,'\t',dynasty)
    print(content)
    print("-"*50)
    
