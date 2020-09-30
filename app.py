from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sys
import os 
import models
import schemas
from settings import app, db

#-------------------INIT---------------------------

#Init app 
"""
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#DB

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

#Init db 
db = SQLAlchemy(app)


#Init ma
ma = Marshmallow(app)
"""
#---------------------------------------------------

#-----------------ROUTES----------------------------

#Create a company 
@app.route('/company', methods=['POST'])
def add_company():
    name = request.json['name']
    domain = request.json['domain']
    email = request.json['email']
    phone = request.json['phone']

    new_company = models.Company(name, domain, email, phone)

    db.session.add(new_company)
    db.session.commit()

    return schemas.company_Schema.jsonify(new_company)


#Get a company 
@app.route('/company/<id>', methods=['GET'])
def get_company(id):
    company = models.Company.query.get(id)
    return schemas.company_Schema.jsonify(company)

#Get all companies
@app.route('/ad', methods=['GET'])
def get_companies():
    all_companies = models.Company.query.all()
    result = schemas.companies_Schema.dump(all_companies)
    return jsonify(result)


#Update a company
@app.route('/company/<id>', methods=['PUT'])
def update_company(id):
    company = models.Company.query.get(id)
    name=request.json['name']
    domain = request.json['domain']
    email = request.json['email']
    phone = request.json['phone']

    company.name = request.json['name']
    company.domain = request.json['domain']
    email = request.json['email']
    phone = request.json['phone']

    #print(ad, file=sys.stderr)

    db.session.commit()

    return schemas.company_Schema.jsonify(company)

#Delete a company
@app.route('/company/<id>', methods=['DELETE'])
def delete_company(id):
    company = models.Company.query.get(id)
    db.session.delete(company)
    db.session.commit()
    return schemas.ad_Schema.jsonify(company)


#Create a user 
@app.route('/user', methods=['POST'])
def add_user():
    f_name = request.json['f_name']
    l_name = request.json['l_name']
    email = request.json['email']
    phone = request.json['phone']

    new_user = models.User(f_name, l_name, email, phone)

    db.session.add(new_user)
    db.session.commit()

    return schemas.user_Schema.jsonify(new_user)

#Get a user
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = models.User.query.get(id)
    return schemas.user_Schema.jsonify(user)

#Get all users
@app.route('/user', methods=['GET'])
def get_users():
    all_users = models.User.query.all()
    result = schemas.users_Schema.dump(all_users)
    return jsonify(result)

#Update a user
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    user = models.User.query.get(id)
    f_name=request.json['f_name']
    l_name = request.json['l_name']
    email = request.json['email']
    phone = request.json['phone']

    user.f_name = f_name
    user.l_name = l_name
    user.email = email
    user.phone = phone 

    #print(ad, file=sys.stderr)

    db.session.commit()

    return schemas.user_Schema.jsonify(user)

#Delete a user 
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = models.User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return schemas.user_Schema.jsonify(user)


#Create an ad 
@app.route('/ad', methods=['POST'])
def add_ad():
    title=request.json['title']
    desc=request.json['desc']
    wage =request.json['wage']
    place=request.json['place']
    work_time=request.json['work_time']
    id_company = request.json['id_company']

    new_ad = models.Ad(title, desc, wage, place, work_time, id_company)

    db.session.add(new_ad)
    db.session.commit()
    
    return schemas.ad_Schema.jsonify(new_ad)

#Get all ads 
@app.route('/ad', methods=['GET'])
def get_ads():
    all_ads = models.Ad.query.all()
    result = schemas.ads_Schema.dump(all_ads)
    return jsonify(result)

#Get an ad 
@app.route('/ad/<id>', methods=['GET'])
def get_ad(id):
    ad = models.Ad.query.get(id)
    return schemas.ad_Schema.jsonify(ad)

#Update an ad 
@app.route('/ad/<id>', methods=['PUT'])
def update_ad(id):
    ad = models.Ad.query.get(id)
    title=request.json['title']
    desc=request.json['desc']
    wage =request.json['wage']
    place=request.json['place']
    work_time=request.json['work_time']
    id_company = request.json['id_company']

    ad.title = title 
    ad.desc = desc 
    ad.wage = wage
    ad.place = place 
    ad.work_time = work_time
    ad.id_company = id_company 

    #print(ad, file=sys.stderr)

    db.session.commit()

    return schemas.ad_Schema.jsonify(ad)


#Delete an ad 
@app.route('/ad/<id>', methods=['DELETE'])
def delete_ad(id):
    ad = models.Ad.query.get(id)
    db.session.delete(ad)
    db.session.commit()
    return schemas.ad_Schema.jsonify(ad)

#Create an application 
@app.route('/app', methods=['POST'])
def add_app():
    id_user = request.json['id_user']
    id_ad = request.json['id_ad']

    new_app = models.Application(id_user, id_ad)

    db.session.add(new_app)
    db.session.commit()

    return schemas.application_Schema.jsonify(new_app)

#Delete an application
@app.route('/app/<id>', methods=['DELETE'])
def delete_app(id):
    app = models.app.query.get(id)
    db.session.delete(app)
    db.session.commit()
    return schemas.application_Schema.jsonify(app)


#Run server 
if __name__ == '__main__': 
    app.run(debug=True)