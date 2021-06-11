'''
功能描述：获取readData的数据，将测试数据填入testCase使用，执行用例，断言结果
实现逻辑：
    1-导包
    2-连接app模拟器
    3-编写测试用例，将excel的测试数据引入用例
    4-断言测试结果
'''
from selenium.webdriver.common.by import By
from common.Driver import Driver
from common.readData import ReadData
import unittest,time
from ddt import ddt,unpack,data

rd = ReadData()
test_data = rd.readData()
data_list = [{'className': 'LittleMessageTest', 'methodName': 'testLittleMessagNormal', 'testdata': 1234.0}, {'className': 'LittleMessageTest', 'methodName': 'test_small_message_normal', 'testdata': 1235.0}, {'className': 'LittleMessageTest', 'methodName': 'test_small_message_normal', 'testdata': 1236.0}, {'className': 'LittleMessageTest', 'methodName': 'test_small_message_normal', 'testdata': 1237.0}, {'className': 'LittleMessageTest', 'methodName': 'test_small_message_normal', 'testdata': 1238.0}]

class LittleMessageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        dr = Driver()
        cls.driver = dr.startUp()


    def testLittleMessagNormal(self):
        case_className = self.__class__.__name__
        case_methodName = self._testMethodName
        for i in range(len(test_data)):
            if test_data[i]['className'] == case_className and test_data[i]['methodName'] == case_methodName:
                testdata = test_data[i]['testdata']
        else:
            print('无符合条件的用例')
        try:
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/bov').click()
            time.sleep(2)
            #选择微头条点击
            items = self.driver.find_elements(By.CLASS_NAME,'android.widget.TextView')
            items[0].click()
            time.sleep(2)
            #选择微头条文本输入要发布的内容
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/blh').send_keys(str(testdata))
            #点击发布按钮
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/a8n').click()
            assert self.driver.page_source.find(str(testdata)) != -1,print('断言失败')
        except Exception as msg:
            print('系统异常：',msg)
            raise
        finally:
            print('用例执行完成')

    @unittest.skip
    def test_small_message_normal(self,testdata):
        try:
            self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bov').click()
            time.sleep(2)
            # 选择微头条点击
            items = self.driver.find_elements(By.CLASS_NAME, 'android.widget.TextView')
            items[0].click()
            time.sleep(2)
            # 选择微头条文本输入要发布的内容
            self.driver.find_element(By.ID, 'com.ss.android.article.news:id/blh').send_keys(testdata)
            # 点击发布按钮
            self.driver.find_element(By.ID, 'com.ss.android.article.news:id/a8n').click()
            assert self.driver.page_source.find('appium-test') != -1, print('断言失败')
        except Exception as msg:
            print('系统异常：', msg)
        finally:
            print('用例执行完成')


if __name__ == '__main__':
    unittest.main()