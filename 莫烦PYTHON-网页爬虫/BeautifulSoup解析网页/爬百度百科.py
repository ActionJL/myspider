# 从 "网页爬虫" 的词条开始爬

# 定义起始链接
# https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin
import urllib

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

from urllib.parse import quote, urlencode
import string

base_url = "https://baike.baidu.com"
his = ['/item/网络爬虫/5162711?fr=aladdin']

# 打印网页内容 + 网页名字
url = quote(base_url + his[-1], safe=string.printable)
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

print(soup.find('h1').get_text(), '    url: ', his[-1])

# 在这个网页上找所有符合要求的 /item/ 网址
# 有时候在sub_urls 中并不能找到合适的网页, 我们就往回跳一个网页, 回到之前的网页中再随机抽一个网页做同样的事.
sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})   # 返回一个列表
# print(sub_urls)

if len(sub_urls) != 0:
    his.append(random.sample(sub_urls, 1)[0]['href'])
else:
    # no valid sub link found
    his.pop()
print(his)




#以上就完成了一次爬取体系了， 接下来加入for循环。

for i in range(20):
    url = quote(base_url + his[-1], safe=string.printable)
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
        print(his)
    else:
        # no valid sub link found
        his.pop()
        print(his)
