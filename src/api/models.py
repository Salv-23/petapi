from sqlalchemy.sql import func
from sqlalchemy.sql.functions import user
from src import app, db
from enum import Enum, unique


# Enum type
class Types(str, Enum):
    veterinarian = 'veterinarian'
    owner = 'owner'


# models
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    userTypes = db.Column(db.Enum(Types), nullable=False)
    
    # Relationships 1 to 1
    address = db.relationship('UserAddress', backref='user', uselist=False)
    # Relationships 1 to many
    verifcationPapers = db.relationship('VerificationPapers', backref='user')
    

    def __init__(self, name, last_name, email, userTypes):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.userTypes = userTypes


class UserAddress(db.Model):
    __tablename__ = 'user_address'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(30), unique=True, nullable=False)  
    zipCode = db.Column(db.Integer, nullable=False)
    userAdress = db.Column(db.Integer, ForeignKey('user.id'))


class VerificationPapers(db.Model):
    __tablename__ = 'verification_papers'

    id = db.Column(db.Integer, primary_key=True)
    documentType = db.Column(db.String(100), nullable=False)
    documentNumber = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.Integer, ForeignKey('user.id'))


class VeterinaryInformation(db.Model):
    __tablename__ = 'veterinary_information'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    verification_status = db.Column(db.Boolean, nullable=False)
    veterinarian = db.Column(db.Integer, ForeignKey('user.id'))


