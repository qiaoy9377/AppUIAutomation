'''
功能描述：读取data.xls文件的数据信息，存储为列表形式，字典元素，返回数据给testCase使用
实现逻辑
    1-导包
    2-获取文件路径
    3-打开文件，确定sheet页
    4-读取第一行数据作为key列表
    5-循环读取剩余行的数据作为value列表
    6-将每一行的value列表与key列表组成字典
    7-将字典添加到列表
    8-返回文件数据列表
'''
import xlrd,os

class ReadData():
    def __init__(self):
        cur_path =os.path.dirname(os.path.dirname(__file__))
        file_path = cur_path+'/testData/data.xls'
        rf = xlrd.open_workbook(file_path)
        self.rf_sheet = rf.sheet_by_index(0)
        self.rows = self.rf_sheet.nrows

    def readData(self):
        data_list = []
        key_list = self.rf_sheet.row_values(0)
        for i in range(1,self.rows):
            value_list = self.rf_sheet.row_values(i)
            data_dict = {key_list[j]:value_list[j] for j in range(len(key_list))}
            data_list.append(data_dict)

        return data_list

if __name__ == '__main__':
    rd = ReadData()
    print(rd.readData())
