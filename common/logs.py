'''
功能描述：自定义log等级和输出格式，方便其他模块调用log调试使用
实例逻辑：
    1-  导入logging模块
    2-重写basicconfig函数定义log等级和输出格式
    3-创建log解释器
    4-返回解释器
'''
import logging

def logs():
    logging.basicConfig(level=logging.DEBUG,format=format('%(name)s-%(asctime)s-%(levelname)s-%(module)s.py-[line:%(lineno)d]-%(message)s'))
    logger = logging.getLogger('AppUIAutomation')
    return logger

logger = logs()
if __name__ == '__main__':
    logger.debug('test')