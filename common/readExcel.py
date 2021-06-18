'''
功能描述：读取excel，提供对外读取数据的方法，根据提供的类名和方法名获取目标数据
实现逻辑：
    1-导包xlrd
    2-定义类：
        2.1-初始化目标文件
        2.2-确定sheet页
        2.3-确定测试数据的所有行和列
    3-定义对外方法，通过接受类名和方法名读取目标测试数据
        3.1遍历判断所有的行中的类名和方法名
            3.1.1匹配则获取该行的第三列data
            3.1.2不匹配则继续continue
'''
import xlrd,os
from common.logs import logger

class ReadExcel():
    def __init__(self):
        cur_path = os.path.dirname(__file__)
        file_path = os.path.dirname(cur_path)+'/testData/data.xls'
        self.rf = xlrd.open_workbook(file_path,'utf-8')
        self.rf_sheet = self.rf.sheet_by_index(0)
        self.rows = self.rf_sheet.nrows
        self.cols = self.rf_sheet.ncols

    def getTestData(self,className,methodName):
        for row in range(self.rows):
            class_name = self.rf_sheet.cell(row,0).value
            method_name = self.rf_sheet.cell(row,1).value
            if  class_name == className and method_name == methodName:
                    return self.rf_sheet.cell(row,2).value
            else:
                continue
        else:
            logger.info('未找到对应的数据')

if __name__ == '__main__':
    re = ReadExcel()
    print(re.getTestData('LittleMessageTest','testLittleMessagNormal'))