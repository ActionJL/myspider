
# Python 外部模块 requests，解决向网页发送信息, 上传图片等问题

import requests


# post请求
data = {'firstname': '莫烦', 'lastname': '周'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
print(r.text)

# 上传图片
file = {'uploadFile': open('./image.png', 'rb')}
r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
print(r.text)


# 登录
payload = {'username': 'Morvan', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)

# 使用Session登录
session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

r = session.get("http://pythonscraping.com/pages/cookies/profile.php")    # 这里没有传递cookies
print(r.text)