from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#数据库对象
db = SQLAlchemy()

#数据迁移对象
migrate = Migrate()

#生成邮件发送对象
mail = Mail()

#自定义初始化函数，初始化所有第三方应用对象
def init_apps(app):
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app=app,db=db)