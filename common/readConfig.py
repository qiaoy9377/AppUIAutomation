'''
功能描述：定义读取config.ini的类和方法，提供给其他模块读取配置为使用
实现逻辑：
    1-导包
    2-打开config.ini文件
    3-读取指定section下的options
    4-返回读取到的数据
'''

import os
from configparser import ConfigParser

class ReadConfig():

    def __init__(self):
        cur_path = os.path.dirname(__file__)
        file_path = os.path.dirname(cur_path)+'/config.ini'
        #实例化configParser对象-这个对象可以打开文件，可以读取文件option
        self.rc = ConfigParser()
        #打开文件
        self.rc.read(file_path,encoding='utf-8')

    def getOption(self,section,option='all'):
        try:
            if option == 'all':
                #读取option键值对
                option = self.rc.items(section)
                return option
            else:
                option = self.rc.get(section,option)
                return option
        except Exception as msg:
            print('执行错误',msg)

if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.getOption('App','deviceName'))