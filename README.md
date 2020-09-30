# jobboard-API

#Use with pipenv 

# Activate venv
$ pipenv shell

# Install dependencies
$ pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy 

# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py
