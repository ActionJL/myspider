"""
爬网页的流程

1.选着要爬的网址 (url)
2.使用 python 登录上这个网址 (urlopen等)
3.读取网页信息 (read() 出来)
4.将读取的信息放入 BeautifulSoup
5.使用 BeautifulSoup 选取 tag 信息等 (代替正则表达式)
"""

# Python中的包(Package)就是一个目录,里面存放了 .py文件,外加一个 __init__.py。通过目录的方式来组织众多的模块,包就是用来管理和分类模块.


from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

# 加载进 BeautifulSoup,大家都推荐使用lxml的形式加载. 然后 soup 里面就有着这个 HTML 的所有信息. 如果你要输出 <h1> 标题, 可以就直接 soup.h1.
soup = BeautifulSoup(html, features='lxml')
print(soup.h1)
print('\n', soup.p)

# 使用 find_all() 来找到所有的选项.
all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)
