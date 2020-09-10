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

    driver.switch_to_frame(0)   # 切换到层上

    # 写入真实 账号 密码 豆瓣

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div/input').send_keys('账号')
    driver.find_element_by_xpath('//*[@id="code"]').send_keys('密码')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[6]/a').click()

    driver.close()

    driver.quit()

