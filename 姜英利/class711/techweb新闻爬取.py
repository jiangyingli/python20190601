'''
techweb网站滚动新闻爬取
孙健
2018年8月9日

'''
import requests
from bs4 import BeautifulSoup
for i in range (1,10):
    url = "http://www.techweb.com.cn/roll/list_"+str(i)+".shtml"
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html_doc = r.text

    soup = BeautifulSoup(html_doc,"html.parser")

    li_list=soup.find("div",attrs={'class':'newslist'}).find("ul").find_all("li")
    # print(li_list)
    for li in li_list:
        span_list = li.find_all("span")
        newsType = ['标题','分类','来源','时间']
        # for span_num in range(len(span_list)):
            #print(newsType[span_num],":",span_list[span_num].get_text("|", strip=True))
    print("第"+str(i)+"页完毕","-"*50)
