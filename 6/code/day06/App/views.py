import hashlib
from random import randint

from flask import Blueprint, Response, current_app, render_template, request
from flask_mail import Message
from App.models import User
from App.tools import send_mail
from .extens import mail, db

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

@qdq.route("/add/")
def add_user():
    for i in range(23,50):
        user = User()
        user.username = 'test'+str(i)
        password = str(randint(10000,1000000))
        user.password_hash = hashlib.sha1(password.encode('utf8')).hexdigest()
        user.gender = randint(0,1)

        db.session.add(user)
        db.session.commit()

    return Response("ok")

@qdq.route("/list/")
def list_user():
    # page = 1
    #获取查询参数
    #获取的参数都是字符串
    page = int(request.args.get('page'))
    # print(type(request.args.get('page')))
    #分页
    data = User.query.paginate(page=page,per_page=current_app.config['PER_PAGE'])
    print(data)
    print(data.items)
    return render_template("listuser.html",data = data)