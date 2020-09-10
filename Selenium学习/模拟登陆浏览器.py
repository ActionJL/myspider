from selenium import webdriver

#
if __name__ == '__main__':
    # 1. 创建浏览器对象
    driver = webdriver.Chrome()    # 需要下载与谷歌浏览器对应的版本

    # 2. 请求页面
    driver.get('https://www.baidu.com/')

    # 3. 页面的基本操作（点击， 输入）
    driver.find_element_by_id('kw').send_keys('超能陆战队')
    driver.find_element_by_id('su').click()    #点击

    driver.save_screenshot('baidu.jpg')

    # 获取渲染之后的数据
    print(driver.page_source)

    print(driver.get_cookies())

    print(driver.current_url)

    driver.close()    # 关闭页面

    driver.quit()    # 关闭浏览器

