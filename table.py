from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///users.db"

db=SQLAlchemy(app)

class users(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(100),nullable=False)
    files=db.relationship('files',backref="users",lazy=True)


class files(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    file_name=db.Column(db.String(225),nullable=False)
    # access_type = db.Column(db.Enum('read-only', 'download', name='access_type_enum'), 
    #                      default='read-only', 
    #                      nullable=False) 
    expiration_date=db.Column(db.Date,nullable=False)
    created_at=db.Column(db.Date,nullable=False)
    shared_link=db.Column(db.String(500),nullable=False)



