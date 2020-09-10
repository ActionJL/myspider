import os
os.makedirs('./img/', exist_ok=True)

IMAGE_URL = "https://mofanpy.com/static/img/description/learning_step_flowchart.png"

# 使用urlretrieve
# 输入下载地址 IMAGE_URL 和要存放的位置. 图片就会被自动下载过去了.
from urllib.request import urlretrieve
urlretrieve(IMAGE_URL, './img/image1.png')