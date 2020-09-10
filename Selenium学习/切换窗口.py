from selenium import webdriver
import time
#
if __name__ == '__main__':
    # 切换窗口
    # 1. 创建浏览器对象
    driver = webdriver.Chrome()  # 需要下载与谷歌浏览器对应的版本

    # 2. 请求页面
    driver.get('https://www.douban.com/')

    #
    driver.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[2]/a').click()

    # 1. 获取当前所有窗口
    current_window = driver.window_handles
    print(current_window)

    driver.switch_to_window(current_window[0])

    driver.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[2]/a').click()

    time.sleep(2)
    driver.back()   # 回退

    time.sleep(2)
    # driver.forward()   #前进




