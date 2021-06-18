'''
功能描述：定义通用的操作方法，方便其他方法调用
实现逻辑：
    1-导包-driver
    2-定义类
        2.1-初始化类的driver属性
    3-定义操作方法
'''
from common.driver import Driver

class Public():

    def __init__(self,driver):
        self.driver = driver

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipUp(self, t=1000):
        x, y = self.getSize()
        x1 = x * 0.5
        y1 = y * 0.75
        y2 = y * 0.25
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipDown(self, t=1000):
        x, y = self.getSize()
        x1 = x * 0.5
        y1 = y * 0.25
        y2 = y * 0.75
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipRight(self, t=1000):
        x, y = self.getSize()
        x1 = x * 0.25
        y1 = y * 0.5
        x2 = x * 0.75
        self.driver.swipe(x1, y1, x2, y1, t)

    def swipLeft(self, t=1000):
        x, y = self.getSize()
        x1 = x * 0.75
        y1 = y * 0.5
        x2 = x * 0.25
        self.driver.swipe(x1, y1, x2, y1, t)

if __name__ == '__main__':
    d = Driver()
    driver = d.startUp()
    p = Public(driver)
    print(p.getSize())