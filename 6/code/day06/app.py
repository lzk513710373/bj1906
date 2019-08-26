from flask import Flask
from App.extens import init_apps
# from App.views import qdq
from flask_script import Manager

from App.views import qdq

app = Flask(__name__)


#邮件配置
app.config['MAIL_SERVER'] = "smtp.126.com"
#发送帐号
app.config['MAIL_USERNAME'] = 'landmark_csl@126.com'
#授权码
app.config['MAIL_PASSWORD'] = 'land123'


#manager
manager = Manager(app)
app.register_blueprint(qdq)

#初始化第三方
init_apps(app)

if __name__ == '__main__':
    manager.run()
