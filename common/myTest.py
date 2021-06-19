'''
功能描述：继承unittest.TestCase，提前定义setupclass类方法，将driver启动封装到该类中，让testcase子类继承，降低代码重复
实现逻辑：
    1-导包unittest
    2-继承unittest。testcase
    3-封装setupclass类方法
'''
import unittest,time
from common.driver import Driver
from common.logs import logger

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        #启动driver
        d = Driver()
        cls.driver = d.startUp()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        cls.driver.quit()
        logger.debug('退出')

if __name__ == '__main__':
    unittest.main()