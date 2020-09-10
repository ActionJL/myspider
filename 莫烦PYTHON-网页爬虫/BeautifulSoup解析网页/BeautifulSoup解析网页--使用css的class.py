# html 和 css  可以比喻为人和衣服

from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/list.html").read().decode('utf-8')
print(html)


# 找所有 class=month 的信息,并打印出它们的 tag 内文字.
soup = BeautifulSoup(html, features='lxml')

# 按class匹配
month = soup.find_all('li', {"class": "month"})
for m in month:
    print(m.get_text())    # 打印tag信息


#  找<ul> 下 <ul> 内部的 <li> 信息
jan = soup.find('ul', {"class": 'jan'})
d_jan = jan.find_all('li')              # use jan as a parent
for d in d_jan:
    print(d.get_text())