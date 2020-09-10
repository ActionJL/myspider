"""
注意, 因为网页中存在中文, 为了正常显示中文, read() 完以后, 我们要对读出来的文字进行转换, decode() 成可以正常显示中文的形式.
"""


# 用 Python 登录网页

from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen(
    "https://mofanpy.com/static/scraping/basic-structure.html"
).read().decode('utf-8')

print(html)


# 匹配网页内容  >   合理的利用 tag 的名字

# 找到这个网页的 title,
import re
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

# 找到中间的那个段落 <p>

# Python的正则表达式模块re，有一个re.DOTALL的参数。
# 默认情况下，正则表达式中的dot（.），表示所有除了换行的字符，加上re.DOTALL参数后，就是真正的所有字符了，包括换行符（\n）。
res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])


# 找所有的链接
res = re.findall(r'href="(.*?)"', html)
print("\n所有链接: ", res)