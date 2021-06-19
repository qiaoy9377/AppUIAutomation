'''
功能描述：将元素定位自动等待方法和初始化driver方法，封装为父类，子类继承即可
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logs import logger

class BasePage():

    def __init__(self,driver):
        self.driver = driver

    def by_find_element(self,*item):
        '''
        定位元素延时等待方法
        :param item: 元素定位属性
        :return: 元素定位方法，供定位元素时使用
        '''
        try:
            element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(item))
            return element
        except Exception as msg:
            logger.error('定位元素异常',msg)