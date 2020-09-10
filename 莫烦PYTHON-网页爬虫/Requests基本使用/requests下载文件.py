import os
os.makedirs('./img/', exist_ok=True)

IMAGE_URL = "https://mofanpy.com/static/img/description/learning_step_flowchart.png"

import requests
#
r = requests.get(IMAGE_URL)
with open('./img/image2.png', 'wb') as f:
    f.write(r.content)


# 下载大文件 requests 有高效方式， 它能一个chunk 一个chunk的下载。
# r.iter_content(chunk_size) #来控制每个 chunk 的大小

r = requests.get(IMAGE_URL, stream=True)    # stream loading

with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)