pip install scrapy
scrapy startproject Douyu

cd Douyu/Douyu
scrapy genspider douyu 'douyucdn.cn'

scrapy crawl name > scrapy crawl douyu

# 步骤
定义要爬取的字段 items.py > 提取 分析数据 spider/xxspider.py  > 处理数据 pipelines.py  > 配置，打开管道 settings.py

# 爬取网址
url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=10"

loads 针对字符串   load 针对文件

# 源码 在sitepackage/scrapy文件夹中

# 查看文件夹中的文件数量
ls | wc -l
-l 行数
wc 统计

# 重命名
import os
os.rename(旧名字，新名字)

# pipelines.py
ImagesPipeline >
    get_media_requests 用于处理图片
    item_completed 用于处理图片路径   result > checksum
#
md5 码  文件标志码