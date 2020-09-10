from selenium import webdriver

#
if __name__ == '__main__':
    # 1. 创建浏览器对象
    driver = webdriver.Chrome()    # 需要下载与谷歌浏览器对应的版本

    # 2. 请求页面
    driver.get('https://www.douban.com/')

    # 3.1通过标签的id获取标签
    ret1 = driver.find_element_by_id('anony-nav')    # 标签对象
    print(ret1)

    # 3.2通过id值获取多个标签
    ret2 = driver.find_elements_by_id('anony-nav')  # 标签对象
    print(ret2)

    # 3.3通过标签的class属性值获取标签
    ret3 = driver.find_element_by_class_name('anony-nav-links')
    print(ret3)

    # 3.4通过xpath获取左上角豆瓣图片的<a>标签
    ret4 = driver.find_element_by_xpath('//*[@id="anony-sns"]/div/div[3]/div/div[1]/ul/li[1]/div/a')
    print(ret4)

    # 3.5 通过标签包裹的文本  下载豆瓣app 获取元素列表 (精确定位)
    ret5 = driver.find_element_by_link_text('下载豆瓣 App')
    print(ret5)

    # 3.6 通过标签包裹的文本 '豆瓣' ， 获取元素的列表(模糊定位)
    ret6 = driver.find_element_by_partial_link_text('豆瓣')
    print(ret6)

    # 3.7 通过标签名 获取元素列表
    ret7 = driver.find_elements_by_tag_name('div')
    print(len(ret7), ret7)

    # 3.8 获取 h1 标签包裹的文本内容
    ret8 = driver.find_element_by_tag_name('h1')
    print(ret8.text)

    # 3.9 通过标签包裹的文本  下载豆瓣app 获取属性值
    ret9 = driver.find_element_by_link_text('下载豆瓣app')
    print(ret9.get_attribute('href'))

    driver.close()
    driver.quit()
