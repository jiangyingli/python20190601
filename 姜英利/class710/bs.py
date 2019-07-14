from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>
    <p class="story">
        <span>你好</span>
    </p>
    </body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
tag = soup.find_all("p",class_="story")[-1]
print(tag.get_text(strip="True"))

# 找到第一个a标签, 返回对象
# tag1 = soup.find(name='a')
# 找到所有的a标签，返回对象
# tag2 = soup.find_all(name='a')
# 找到id＝link2的标签，返回对象,css选择器语法
# tag3 = soup.soupselect('#link2')
# print(tag3)
