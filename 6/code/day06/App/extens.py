from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

#生成邮件发送对象
mail = Mail()

#自定义初始化函数，初始化所有第三方应用对象
def init_apps(app):
    mail.init_app(app)
    # db.init_app(app)