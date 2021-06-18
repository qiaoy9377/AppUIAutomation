'''
功能描述：连接手机，打开今日头条app，发布微头条，断言返回结果
实现逻辑：
    1-导包
    2-捕获发布按钮
    3-点击微头条
    4-输入要发布的内容
    5-点击发布
    6-断言结果
'''
import unittest,time
from selenium.webdriver.common.by import By
from common.myTest import MyTest
from common.readExcel import ReadExcel
from common.public import Public

re = ReadExcel()

class LittleMessageTest(MyTest):

    #通过继承的方式减少了这块儿代码的冗余
    # @classmethod
    # def setUpClass(cls) -> None:
    #     dr = Driver()
    #     cls.driver = dr.startUp()

    @unittest.skip
    def testLittleMessagNormal(self):
        case_className = self.__class__.__name__
        case_methodName = self._testMethodName
        testdata = re.getTestData(case_className,case_methodName)
        p = Public(self.driver)
        time.sleep(5)
        p.swipUp()
        try:
            #点击首页的发布
            time.sleep(5)
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/bov').click()
            time.sleep(2)
            #选择微头条点击
            items = self.driver.find_elements(By.CLASS_NAME,'android.widget.TextView')
            items[0].click()
            time.sleep(2)
            #选择微头条文本输入要发布的内容
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/blh').send_keys(testdata)
            #点击发布按钮
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/a8n').click()
            assert self.driver.page_source.find('发布') != -1,print('断言失败')
        except Exception as msg:
            print('系统异常：',msg)
        finally:
            print('用例执行完成')

    @unittest.skip('跳过')
    def test_little_text_abnormal(self):
        try:
            #点击首页的发布
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/bov').click()
            time.sleep(2)
            #选择微头条点击
            items = self.driver.find_elements(By.CLASS_NAME,'android.widget.TextView')
            items[0].click()
            time.sleep(2)
            #选择微头条文本输入要发布的内容
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/blh').send_keys('')
            #点击发布按钮
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/a8n').click()
            assert self.driver.page_source.find('取消') != -1,print('断言失败')
        except Exception as msg:
            print('系统异常：',msg)
        finally:
            print('用例执行完成')

    @unittest.skip('跳过')
    def test_little_text_cancel(self):
        try:
            #点击首页的发布
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/bov').click()
            time.sleep(2)
            #选择微头条点击
            items = self.driver.find_elements(By.CLASS_NAME,'android.widget.TextView')
            items[0].click()
            time.sleep(2)
            #选择微头条文本输入要发布的内容
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/blh').send_keys('')
            #点击发布按钮
            self.driver.find_element(By.ID,'com.ss.android.article.news:id/an6').click()
            assert self.driver.page_source.find('取消') != -1,print('断言失败')
        except Exception as msg:
            print('系统异常：',msg)
        finally:
            print('用例执行完成')

    def testOpration(self):
        p = Public(self.driver)
        print(p.getSize())
        time.sleep(5)
        p.swipUp()
        time.sleep(2)
        p.swipDown()
        time.sleep(2)
        p.swipLeft()
        time.sleep(2)
        p.swipRight()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
