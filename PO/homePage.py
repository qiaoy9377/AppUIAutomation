'''
功能描述：将首页封装为一个页面类，页面上的元素的定位方式就是属性，该元素的操作就是方法
实现逻辑：
    1-类
    2-初始化方法
    3-元素的操作方法
'''
from selenium.webdriver.common.by import By
from PO.basePage import BasePage
from common.logs import logger
from common.driver import Driver


class HomePage(BasePage):
    #类属性
    publish = (By.ID,'com.ss.android.article.news:id/bov')
    little_message = (By.CLASS_NAME,'android.widget.TextView')
    message = (By.ID,'com.ss.android.article.news:id/blh')
    message_publish = (By.ID,'com.ss.android.article.news:id/a8n')

    def clickPublish(self):
        self.by_find_element(*self.publish).click()

    def clickLittleMessage(self):
        self.driver.find_elements(*self.little_message)[0].click()

    def writeMessage(self,data):
        self.by_find_element(*self.message).send_keys(data)

    def clickMessagePublish(self):
        self.by_find_element(*self.message_publish).click()

    def sendLittleMessage(self,data):
        self.clickPublish()
        self.clickLittleMessage()
        self.writeMessage(data)
        self.clickMessagePublish()

if __name__ == '__main__':
    d = Driver()
    driver = d.startUp()
    hp = HomePage(driver)
    hp.clickPublish()
    # hp.clickLittleMessage()
    # hp.writeMessage('111')
    # hp.clickMessagePublish()
