from . import db


class User(db.Model):
    # 表名
    __tablename__ = 'users'
    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(16))

    def __repr__(self):
        return 'User: %s' % self.name
