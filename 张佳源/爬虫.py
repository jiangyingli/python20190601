from bs4 import BeautifulSoup
import requests
url='https://so.gushiwen.org/authors/authorvsw.aspx?page=1&id=b90660e3e492'
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
sons_divs = soup.find_all("div",class_= "sons")
#source_p = soup.find_all("p",class_= "source")
#print(sons_divs[0])
#print(sons_divs[0].find("b").string)
#print(sons_divs[0].find_all("a")[1].text,end="  ")
#print(sons_divs[0].find_all("a")[2].text)
#list=sons_divs[0].find("div",class_="contson").contents
#for i in range(len(list)):
#    if(i%2==0):
#        print(list[i])
#print(str(sons_divs[0].find("div",class_="contson")).replace("<br/>","\n"))
for i in range( len(sons_divs)):
    print(sons_divs[i].find("b").string)
    print(sons_divs[i].find_all("a")[1].text, end="  ")
    print(sons_divs[i].find_all("a")[2].text)
    #list = sons_divs[i].find("div", class_="contson").contents
    #for j in range(len(list)):
    #    if (j % 2 == 0):
    #        print(list[j])
    print(sons_divs[i].find("div", class_="contson").get_text("\n",strip="True"))
    print("—"*30)