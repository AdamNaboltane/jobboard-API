from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt 
import sys
import os

#Init app 

app = Flask(__name__);
basedir = os.path.abspath(os.path.dirname(__file__))

#DB

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

#Init db 
db = SQLAlchemy(app)

#Init ma
ma = Marshmallow(app)