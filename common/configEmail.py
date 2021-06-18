'''
功能描述：提供发送邮件的方法，供测试用例执行完成后将最新的报告发送给相关人员
实现逻辑：
    1-导包：smtp、email
    2-初始化类配置邮箱参数
        2.1-调用readconfig模块的方法，获取email的配置信息
    3-组装邮件内容
        3.1-配置邮件内容
        3.2-添加主题
        3.3-添加发送者、接收者
    4-登录并发送邮件
        4.1-连接服务器
        4.2-登录邮箱
        4.3-发送邮件
'''
import smtplib,os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from common.readConfig import ReadConfig

class ConfigEmail():

    #配置邮件参数
    def __init__(self):
        rc = ReadConfig()
        self.sender = rc.getOption('Email','sender')
        self.receiver = rc.getOption('Email','receiver')
        self.smtpserver = rc.getOption('Email','smtpserver')
        self.username = rc.getOption('Email','username')
        self.password = rc.getOption('Email','password')
        self.subject = rc.getOption('Email','subject')
        self.content = rc.getOption('Email','content')
    #组装邮件内容和附件
    def __configEmail(self):
        report_path = os.path.dirname(os.path.dirname(__file__))+'/testReport/'
        report = report_path+os.listdir(report_path)[-1]
        with open(report,'rb') as rf:
            f = rf.read()
            msg = MIMEMultipart()
            att = MIMEText(f,'plain','utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = f'attachment;filename={os.listdir(report_path)[-1]}'
            msg.attach(att)
            msg.attach(MIMEText(self.content,'plain','utf-8'))
            msg['Subject'] = Header(self.subject,'utf-8')
            msg['From'] = self.sender
            msg['To'] = self.receiver

        return msg
    #登录并发送邮件
    def sendEmail(self):
        try:
            msg = self.__configEmail()
            se = smtplib.SMTP()
            #连接服务器
            se.connect(self.smtpserver)
            #登录邮箱
            se.login(self.username,self.password)
            #发送邮件
            se.sendmail(self.sender,str(self.receiver).split(','),msg.as_string())
        except Exception as error:
            print('邮件发送失败',error)
        else:
            print('邮件发送成功')
        finally:
            se.close()

if __name__ == '__main__':
    ce = ConfigEmail()
    ce.sendEmail()

