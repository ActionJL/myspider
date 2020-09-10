from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/table.html").read().decode('utf-8')


# 用 soup 将这些 <img> tag 全部找出来
soup = BeautifulSoup(html, features='lxml')

img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})    # 正则选取图片
for link in img_links:
    print(link['src'])


# 正则选一些课程的链接
course_links = soup.find_all('a', {'href': re.compile('https://morvan.*')})
for link in course_links:
    print(link['href'])