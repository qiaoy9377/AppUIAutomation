'''
功能描述：准备启动的app的driver，进行相关配置，提供给testCase使用
实现逻辑：
    1-配置启动参数
    2-启动app
    3-返回driver
'''
from appium import webdriver

class Driver():

    def __init__(self):
        self.desire_caps = {
            'deviceName':'127.0.0.1:21503',
            'platformName':'Android',
            'platformVersion':'5.1.1',
            'appPackage':'com.ss.android.article.news',
            'appActivity':'com.ss.android.article.news.activity.MainActivity',
            'noReset':True,
            'unicodeKeyboard':True
        }

    def startUp(self):
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.desire_caps)
        return driver

if __name__ == '__main__':
    dr = Driver()
    driver = dr.startUp()