import requests
from bs4 import BeautifulSoup


# 豆瓣电影top250


def __getHtml():
    data = []
    pageNum = 1
    pageSize = 0
    try:
        while (pageSize <= 25):
            url = "https://movie.douban.com/top250?start=" + str(pageSize) + "&filter=" + str(pageNum)
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            html_doc = r.text
            data.append(html_doc)
            pageSize += 25
            pageNum += 1
            print(pageSize, pageNum)
    except Exception as e:
        raise e
    return data


def __getData(html):
    title = []  # 电影标题
    rating_num = []  # 评分
    range_num = []   # 排名
    rating_people_num = []  # 评价人数
    data = {}
    # bs4解析html
    soup = BeautifulSoup(html, "html.parser")
    for li in soup.find("ol", attrs={'class': 'grid_view'}).find_all("li"):
        title.append(li.find("span", class_="title").text)
        rating_num.append(li.find("div", class_='star').find("span", class_='rating_num').text)
        range_num.append(li.find("div", class_='pic').find("em").text)
        spans = li.find("div", class_='star').find_all("span")
        for x in range(len(spans)):
            if x <= 2:
                pass
            else:
                rating_people_num.append(spans[x])

    data['title'] = title
    data['rating_num'] = rating_num
    data['range_num'] = range_num
    data['rating_people_num'] = rating_people_num
    return data


def __getMovies(data):
    
    f = open('F://1.html', 'w')
    f.write("<html>")
    f.write("<body>")
    f.write("<table width='800px'>")

    f.write("<thead>")
    f.write("<tr>")
    f.write("<th>电影</th>")
    f.write("<th>排名</th>")
    f.write("<th>评分</th>")
    f.write("<th>评价人数</th>")
    f.write("</tr>")
    f.write("</thead>")

    f.write("<tbody>")
    for data in datas:
        for i in range(0, 25):
            f.write("<tr>")
            f.write("<td style='color:orange;text-align:center'>%s</td>" % data['title'][i])
            f.write("<td style='color:blue;text-align:center'>%s</td>" % data['rating_num'][i])
            f.write("<td style='color:red;text-align:center'>%s</td>" % data['range_num'][i])
            f.write("<td style='color:red;text-align:center'>%s</td>" % data['rating_people_num'][i])

            f.write("</tr>")
    f.write("</tbody>")

    f.write("</thead>")
    f.write("</table>")
    f.write("</body>")
    f.write("</html>")
    f.close()


if __name__ == '__main__':
    datas = []
    htmls = __getHtml()
    for i in range(len(htmls)):
        data = __getData(htmls[i])
        datas.append(data)
    __getMovies(datas)
