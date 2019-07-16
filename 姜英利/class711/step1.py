from bs4 import BeautifulSoup
import bs4
"""
你说我是字符串，不输出的话，我就是注释
"""
html = """
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
   and
   <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>
   ; and they lived at the bottom of a well.
  </p>
  <p class="story1">
   ...<a>123</a>
  </p>
  <span><!--我是注释--></span>
  <div class="sister">
    <div>
        <p>111</p>
        <p>222</p>
    </div>
    <div>
        <div>孙div</div>
    </div>
  </div>
 </body>
</html>
"""
# html:<!--fdsafdsafdsafdsa-->
# python:#''' '''  """  """
#javascript:    //   /*  */
#css : #
#sql : #

# 调用BeautifulSoup函数，
# 参数1，解析的HTML内容，汤的原料
# 参数2，解析器，做汤的方式
soup = BeautifulSoup( html ,"html.parser")

# print( type(soup.span.string) )
# print( type(soup.b.string) )

# if(isinstance( soup.span.string , bs4.Comment )):
#     print("是注释")

# 获取标签，取标签名，属性

# div = soup.find("div")
# children = div.children #生成器
# i=0
# for li in children :
#     if( isinstance( li , bs4.Tag ) ):
#         pass
#     else:
#         del children[i]
#     i+=1
#
# print(children)


# div = soup.div.contents
# i=0
# for li in div:
#     if(isinstance( li ,bs4.Tag )):
#         pass
#     else:
#         del div[i]
#     i+=1
# print(div)

# contents = soup.div.contents
# sibling = contents[0].next_sibling.next_sibling.next_sibling
# print(sibling)
# [
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>,
# <a >123</a>
# ]

# aas = soup.findAll("a", class_="sister")
#
# print(aas)


# who = soup.div.find_all("div",recursive=False)
# print(who)
# print(soup.findAll("p"))
# res = soup.select("p:nth-of-type(3)")
# print(res)

soup.find_all(class_="sister")

soup.select(".sister")

soup.find("body").find("")


