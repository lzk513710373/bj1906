from flask import Flask
from flask_migrate import Migrate, MigrateCommand

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

#数据库连接
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:123@127.0.0.1:3306/day06"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PER_PAGE"] = 10  #每页显示的记录个数


#manager
manager = Manager(app)
manager.add_command('db',MigrateCommand)

app.register_blueprint(qdq)

#初始化第三方
init_apps(app)

if __name__ == '__main__':
    manager.run()
