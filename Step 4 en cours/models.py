from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from settings import app, db
import os 

"""#Init app 

app = Flask(__name__);
basedir = os.path.abspath(os.path.dirname(__file__))

#DB

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

#Init db 
db = SQLAlchemy(app)
"""

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255))
    domain=db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))


    def __init__(self, name, domain, email, phone):
        self.name = name
        self.domain = domain 
        self.email = email 
        self.phone = phone 



class Ad(db.Model):
    __tablename__ = 'ads'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    desc=db.Column(db.String(255))
    wage = db.Column(db.String(255))
    place = db.Column(db.String(255))
    work_time = db.Column(db.String(255))
    id_company = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)

    def __init__(self, title, desc, wage, place, work_time, id_company):
        self.title = title
        self.desc = desc
        self.wage = wage
        self.place = place 
        self.work_time = work_time
        self.id_company = id_company



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    f_name=db.Column(db.String(255))
    l_name = db.Column(db.String(255))
    password = db.Column(db.String(60))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    def __init__(self, f_name, l_name, password, email, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.password = password
        self.email = email
        self.phone = phone
        




class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_ad = db.Column(db.Integer, db.ForeignKey('ads.id'), nullable=False)

    def __init__(self, id_user, id_ad): 
        self.id_user = id_user
        self.id_ad = id_ad