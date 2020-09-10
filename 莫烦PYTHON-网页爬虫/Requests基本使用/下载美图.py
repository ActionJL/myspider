# 每次的爬虫, 都是先分析一下这个网页要找的东西的位置, 然后怎么索引上这个位置, 最后用 python 找到它
# http://www.ngchina.com.cn/animals/

from bs4 import BeautifulSoup
import requests

# 定义爬取的 url.
url = 'http://www.ngchina.com.cn/animals/photo/6339.html###'

# 用 BeautifulSoup 找到带有 img_list 的这种 <ul>,
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('div', {"class": "recommend add_style"})

print(img_ul[0].find_all('img'))

imgs = img_ul[0].find_all('img')

for img in imgs:
    url = img['src']
    r = requests.get(url, stream=True)
    image_name = url.split('/')[-1]
    with open('./img/%s' % image_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)
    print('Saved %s' % image_name)
