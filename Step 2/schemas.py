from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from settings import app, ma
import os 
"""#Init app 

app = Flask(__name__);
basedir = os.path.abspath(os.path.dirname(__file__))

#Init ma
ma = Marshmallow(app)
"""

#Company Schemas 
class companySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'domain', 'email', 'phone')
company_Schema = companySchema()
companies_Schema = companySchema(many=True)

#Ad Schemas
class adSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'desc', 'wage', 'place', 'work_time', 'id_company')
ad_Schema = adSchema()
ads_Schema = adSchema(many=True)

#User Schema
class userSchema(ma.Schema):
    class Meta:
        fields = ('id', 'f_name', 'l_name', 'email', 'phone')
user_Schema = userSchema()
users_Schema = userSchema(many=True)

#Application Schema
class applicationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_user', 'id_ad')
application_Schema = applicationSchema()
applications_Schema = applicationSchema(many=True)
