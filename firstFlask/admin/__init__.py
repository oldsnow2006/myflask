from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import jinja2
from flask import Blueprint
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flaskweb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





webadmin = Blueprint('webadmin',__name__)
from . import views
