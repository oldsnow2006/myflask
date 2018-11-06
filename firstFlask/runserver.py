# coding:utf-8
from admin import app
from admin import webadmin
app.register_blueprint(webadmin,url_prefix='/admin')

from admin.models import User,db
if __name__ == '__main__':
   app.run()
