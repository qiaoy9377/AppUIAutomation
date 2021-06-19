'''
功能描述：框架运行的入口，实现查找用例，运行用例，生成报告，自动清理报告，发送邮件
实现逻辑：
    1-导包-unittest、os、htmltestrunner
    2-查找用例生成测试套件
        2.1-unittest.testloader内的discover方法，生成suite
    3-运行用例并生成报告
        3.1-htmltestrunner的runner.run（suite）
    4-自动清理报告
        4.1-autoclear（1-全部清除；2-设定报告数量，清除多余的历史报告）
        方案一
            4.1.1-获取report下的全部文件
            4.1.2-遍历删除文件
        方案二
            listdir无序
            1、获取report下的全部文件
            2、判断文件数量
                2.1超过，对文件进行排序
                2.1.1遍历report下的文件
                    1-通过getctime获取文件创建时间形成列表
                    2-将文件名与getctime合并为字典方便查找要删除的文件
                2.1.2-将时间列表进行排序
                2.1.3-找到要删除的文件时间
                2.1.4-遍历要删除的文件时间
                    1-找到文件时间对应的文件进行删除
'''
import unittest,os,time
from HTMLTestRunner import HTMLTestRunner
from common.logs import logger
from common.configEmail import ConfigEmail

cur_path = os.path.dirname(__file__)
now_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())

def creatSuite():
    '''
    使用testloader模块生成测试套件
    :return: 生成的测试套件
    '''
    # 1-获取用例文件路径，加载测试套件
    case_path = cur_path + '/testCase/'
    suite = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='*test.py', top_level_dir=None)
    return suite

def autoClearReport():
    '''
    自动清理旧报告文件
    :return:
    '''
    #方案一
    # report_list = os.listdir(cur_path+'/testReport')
    # for report in report_list:
    #     if report == '__init__.py':
    #         pass
    #     else:
    #         os.remove(cur_path+'/testReport/'+report)

    #方案二
    #获取报告文件夹下的文件数量
    report_list = os.listdir(cur_path+'/testReport')
    logger.debug(report_list)
    #判断文件数量是否大于3个
    if len(report_list) > 3:
        #情况1：获取到的文件自动排序
        #是，则清除时间最早的报告，由于报告命名有时间，所以报告正序排列
        #找到要删除的文件列表
        # for report in report_list[:-3]:
        #     os.remove(cur_path+'/testReport/'+report)

        #情况2：获取到的文件列表是乱序的
        #1-获取每个文件的创建时间
        #创建空列表和字典，用来存储数据
        report_time_list = []
        report_time_dict = {}
        for report in report_list:
            report_time = os.path.getctime(cur_path+'/testReport/'+report)
            #组成创建时间列表
            report_time_list.append(report_time)
            #组成创建时间和文件的对应关系字典
            report_time_dict[report_time]=report
        #对文件时间进行排序
        report_time_list.sort()
        #循环删除需要删除的文件
        for report_remove in report_time_list[:-3]:
            #执行删除文件操作
            os.remove(cur_path+'/testReport/'+report_time_dict[report_remove])



if __name__ == '__main__':
    #获取suite
    suite = creatSuite()
    #2-创建报告
    report = cur_path+f'/testReport/report{now_time}.html'
    #3-以二进制方式写入文件
    rf = open(report,'wb')
    #4-实例化htmltestrunner方法
    runner = HTMLTestRunner(stream=rf,title='AppUIAutomation-test',description='AppUIAutomation用例执行情况如下:')
    runner.run(suite)
    #5-关闭报告
    rf.close()
    # 6-清理报告
    autoClearReport()
    #7-发送邮件
    ce = ConfigEmail()
    ce.sendEmail()