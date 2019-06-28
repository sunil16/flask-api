# from database.db_setup import *
# from model.building import *
from app import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Building(db.Model):
    __tablename__ = 'buildings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(50))
    landmarks = db.Column(db.String(50))
    rooms = db.relationship('Room', backref='owner', lazy='dynamic')

class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    flat_number = db.Column(db.Integer)
    name = db.Column(db.String(20))
    square_feet_area = db.Column(db.Float)
    type = db.Column(db.String(20))
    no_of_bathrooms  = db.Column(db.Integer)
    maintenance = db.Column(db.String(20))
    electricity_account_number = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('buildings.id'))

def init_db():
    db.create_all()
    print("Database created")
