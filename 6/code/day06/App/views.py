from flask import Blueprint, Response, current_app
from flask_mail import Message

from App.tools import send_mail
from .extens import mail


qdq = Blueprint('qdq',__name__,url_prefix='/mail')

@qdq.route('/mail/')
def my_send_mail():
    #current_app代表了当前应用(app)
    # print(current_app.config['MAIL_USERNAME'])
    # msg = Message(subject='测试邮件，不用回复',
    #               recipients=['313728420@qq.com'],
    #               sender=current_app.config["MAIL_USERNAME"])
    # msg.html = "<h1>hello，天终于凉快了</h1>"
    # #发送邮件
    # mail.send(msg)
    #自定义函数发送邮件
    send_mail(subject='再发一封',templateName='mail.html',
              to="313728420@qq.com,291590691@qq.com",name='成少雷')

    return Response("hello")