'''
功能描述：准备启动的app的driver，进行相关配置，提供给testCase使用
实现逻辑：
    1-配置启动参数
    2-启动app
    3-返回driver
'''
from appium import webdriver
from common.readConfig import ReadConfig
from common.logs import logger

class Driver():

    def __init__(self):
        rc = ReadConfig()
        #这个读出来是option键值对的列表
        option_list = rc.getOption('App')
        #通过下标取，不灵活
        # self.desire_caps = {
        #     'deviceName':option_list[0][1],
        #     'platformName':option_list[1][1],
        #     'platformVersion':option_list[2][1],
        #     'appPackage':option_list[3][1],
        #     'appActivity':option_list[4][1],
        #     'noReset':eval(option_list[5][1]),
        #     'unicodeKeyboard':eval(option_list[6][1])
        # }

        #改造readConfig方法，通过section+option拿到具体的option值
        self.desire_caps = {
            'deviceName':rc.getOption('App','deviceName'),
            'platformName':rc.getOption('App','platformName'),
            'platformVersion':rc.getOption('App','platformVersion'),
            'appPackage':rc.getOption('App','appPackage'),
            'appActivity':rc.getOption('App','appActivity'),
            'noReset':bool(rc.getOption('App','noReset')),
            'unicodeKeyboard':bool(rc.getOption('App','unicodeKeyboard'))
        }

        #key会变成小写，行不通，包做了小写处理，需要改包的源码，也不够灵活，
        # 如果不是用全部的option就会出现多余的数据，而且无法转换个别不符合要求的数据类型
        # self.desire_caps = {option[0]:option[1] for option in option_list}
        # logger.debug(self.desire_caps)

    def startUp(self):
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.desire_caps)
        return driver

if __name__ == '__main__':
    dr = Driver()
    driver = dr.startUp()