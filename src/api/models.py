from sqlalchemy.sql import func
from sqlalchemy.sql.functions import user
from src import db 
from enum import Enum, unique


# user type for User
class Types(str, Enum):
    veterinarian = 'veterinarian'
    owner = 'owner'

# phone number type for PhoneNumbers
class NumberType(str, Enum):
    home = 'home'
    work = 'work'
    mobile = 'mobile'


# models
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_type = db.Column(db.Enum(Types), nullable=False)
    
    # 1 to 1 relationships
    address = db.relationship('UserAddress', backref='user', uselist=False)
    vet_info = db.relationship('VeterinaryInformation', backref='user', uselist=False)

    # 1 to many relationships
    verifcation_papers = db.relationship('VerificationPapers', backref='user')
    phone_numbers = db.relationship('PhoneNumbers', backref='user')
    cards = db.relationship('Cards', backref='user')
    veterinarian_cards = db.relationship('VeterinarianCards', backref='user')
    applications = db.relationship('Applications', backref='user')
    appointments = db.relationship('Appointments', backref='user')
    

    def __init__(self, name, last_name, email, user_type):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.user_type = user_type


class UserAddress(db.Model):
    __tablename__ = 'user_address'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(30), nullable=False)  
    zip_code = db.Column(db.String(30), nullable=False)
    user_address = db.Column(db.Integer, db.ForeignKey('user.id'))


class VerificationPapers(db.Model):
    __tablename__ = 'verification_papers'

    id = db.Column(db.Integer, primary_key=True)
    document_type = db.Column(db.String(100), nullable=False)
    document_number = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))


class VeterinaryInformation(db.Model):
    __tablename__ = 'veterinary_information'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    verification_status = db.Column(db.Boolean, nullable=False)
    veterinarian = db.Column(db.Integer, db.ForeignKey('user.id'))


class PhoneNumbers(db.Model):
    __tablename__ = 'phone_numbers'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(30), nullable=False)
    number_type = db.Column(db.Enum(NumberType))
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Cards(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(50), nullable=False)
    pet_race = db.Column(db.String(30), nullable=False)
    pet_gender = db.Column(db.String(30), nullable=False)
    birthday = db.Column(db.DateTime)
    notes = db.Column(db.String(500))
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    # 1 to many relationships
    veterinarian = db.relationship('VeterinarianCards', backref='cards')
    applications = db.relationship('Applications', backref='cards')
    appointments = db.relationship('Appointments', backref='cards')


class VeterinarianCards(db.Model):
    __tablename__ = 'veterinarian_cards'

    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(500))
    veterinarian = db.Column(db.Integer, db.ForeignKey('user.id'))
    card = db.Column(db.Integer, db.ForeignKey('cards.id'))


class Applications(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    application_type = db.Column(db.String(200))
    brand = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    code = db.Column(db.String(50))
    notes = db.Column(db.String(500))
    applicator = db.Column(db.Integer, db.ForeignKey('user.id'))
    card = db.Column(db.Integer, db.ForeignKey('cards.id'))


class Appointments(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    appointment_date = db.Column(db.DateTime)
    appointment_notes = db.Column(db.String(500))
    veterinarian = db.Column(db.Integer, db.ForeignKey('user.id'))
    card = db.Column(db.Integer, db.ForeignKey('cards.id'))
