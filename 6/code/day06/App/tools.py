#工具函数
from flask import render_template, current_app
from flask_mail import Message

from App.extens import mail


def send_mail(subject,templateName,to,**kwargs):
    """
    邮件发送
    :param subject: 邮件标题
    :param templateName: 模板文件名
    :param to: 接收者
    :param sender: 发送者
    :kwargs  模板参数
    :return: 无
    """
    #对接收者进行处理
    if isinstance(to,(tuple,list)):
        receives = to  #邮件接收者
    elif isinstance(to,str):
        receives = to.split(',') #如果接收者是字符串，要求必须以逗号做分隔符
    else:
        raise Exception("无法识别的接收者")
    sender = current_app.config["MAIL_USERNAME"]
    msg = Message(subject=subject,recipients=receives,sender=sender)

    msg.html = render_template(templateName,**kwargs)
    print(msg.html)

    #发送
    mail.send(msg)

