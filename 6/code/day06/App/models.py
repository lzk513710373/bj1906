from App.extens import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(30),unique=True,nullable=False)
    password_hash = db.Column(db.String(128),nullable=False)
    gender = db.Column(db.Integer,default=0)

    __tablename__ = "user"
