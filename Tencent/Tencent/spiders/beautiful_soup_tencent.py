# python3 urllib 和 urllib2 集成在一个包了
# urllib2 == urllib.request
# import urllib2


import urllib.request
import json
from bs4 import BeautifulSoup


def tencent():
    # https://careers.tencent.com/search.html?index=2
    url = 'https://www.baidu.com'

    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}

    # url 作为Request()方法的参数，构造并返回一个Request对象
    request = urllib.request.Request(url, headers = headers)

    # 向指定的url发送请求，并返回服务器响应的类文件对象
    response = urllib.request.urlopen(request)

    # 可以查看响应状态码
    print(response.code)

    #
    html = response.read()
    # print(html)

    # 通过bs4解析页面数据，使用的是lxml解析器
    soup = BeautifulSoup(html, 'lxml')

    # 通过select 方法提取页面里面 所有的符合class条件的tr标签节点列表
    select1 = soup.select('tr[class="even"]')
    select2 = soup.select('tr[class="odd"]')
    # 将两个列表组合
    select_list = select1 + select2

    # 存储所有职位信息的
    item_list = []

    # 迭代select_list 获取每个节点
    for select in select_list:
        # 取出职位链
        # 存储每个职位信息

        item = {}

        # 提取第一个td标签的a标签的 href属性值
        item['position_link'] = 'http://hr.tencent.com/' + select.select("td a")[0].attrs['href']


        # 突起第一个td标签的a标签的文本内容
        # 职位名称
        item['position_name'] = select.select('td a')[0].get_text()
        # 职位类型
        item['position_type'] = select.select('td a')[1].get_text()
        # 职位数量
        item['position_num'] = select.select('td a')[2].get_text()
        # 工作地点
        item['work_location'] = select.select('td a')[3].get_text()
        # 发布时间
        item['publish_time'] = select.select('td a')[4].get_text()

        # 最后将item职位数据追加到item_list
        item_list.append(item)


    # 把python数据类型的数据，转换为json格式数据类型存储

    # json.dumps() 处理中文默认使用ascii编码, ensure_ascii = False表示禁用ascii编码,使用Unicode编码处理

    # 返回json格式数据
    content = json.dumps(item_list, ensure_ascii=False)

    with open('tencent_zhaopin.json', 'w') as f:
        f.write(content.encode('urf-8'))


if __name__ == '__main__':
    tencent()