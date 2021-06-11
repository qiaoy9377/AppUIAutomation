'''
功能描述：
实现逻辑：
1-导包
2-创建app相关参数配置
3-调试
'''
from appium import webdriver
import time

from selenium.webdriver.common.by import By


def startUp():
    print('启动中.....')
    #2-启动参数设置成dict数据形式
    desire_caps = {
        'deviceName':'127.0.0.1:21503',
        # 'deviceName':'8KE5T19425002034',
        'platformName':'Android',
        'platformVersion':'5.1.1',
        'appPackage':'com.ss.android.article.news',
        'appActivity':'com.ss.android.article.news.activity.MainActivity',
        'noReset':True,
        'unicodeKeyboard':True
    }
    #3-启动app，第一个参数输入appium server 的服务器地址，服务器的端口号默认4723，第二个参数输入启动参数
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)
    print('启动完成，等待6s')
    return driver

def sendMsg(driver):
    #4-定位目标元素，进行操作
    driver.find_element(By.ID,'com.ss.android.article.news:id/bov').click()
    time.sleep(2)
    items = driver.find_elements(By.CLASS_NAME,'android.widget.TextView')
    items[0].click()
    driver.find_element(By.ID,'com.ss.android.article.news:id/blh').send_keys('12345678')
    driver.find_element(By.ID,'com.ss.android.article.news:id/a8n').click()
    time.sleep(6)
    assert driver.page_source.find('发布')!= -1, print('断言失败')
    driver.quit()
    #5-关闭app

def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

def swipUp(driver,t=1000):
    x,y = getSize(driver)
    x1 = x*0.5
    y1 = y*0.75
    y2 = y*0.25
    driver.swipe(x1,y1,x1,y2,t)

def swipDown(driver,t=1000):
    x,y = getSize(driver)
    x1 = x*0.5
    y1 = y*0.25
    y2 = y*0.75
    driver.swipe(x1,y1,x1,y2,t)

def swipRight(driver,t=1000):
    x,y = getSize(driver)
    x1 = x*0.25
    y1 = y*0.5
    x2 = x*0.75
    driver.swipe(x1,y1,x2,y1,t)

def swipLeft(driver,t=1000):
    x,y = getSize(driver)
    x1 = x*0.75
    y1 = y*0.5
    x2 = x*0.25
    driver.swipe(x1,y1,x2,y1,t)

if __name__ == '__main__':
    driver = startUp()
    # swipUp(driver)
    # swipDown(driver)
    # swipRight(driver)
    # swipLeft(driver)
    sendMsg(driver)