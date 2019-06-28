from flask import Flask, request
import os, hashlib, re, json
from os.path import join
from model.building import *
from cerberus import Validator

app = Flask(__name__)
app.config.from_pyfile('./config.py')

req_param_schema = {"name": {"type": "string", "required": True}, "address": { "type": "string", "required": True},"landmarks": {"type": "string", "required": True},'rooms': {'type': 'list','schema': {'type': 'dict', 'schema': { "flat_number": {"type": "integer", "required": True}, "name": {"type": "string", "required": True}, "square_feet_area":{"type": "float", "required": True}, "type":{"type": "string", "required": True},"no_of_bathrooms" :  {"type": "integer", "required": True},           "maintenance" : {"type": "string", "required": True},  "electricity_account_number":  {"type": "integer", "required": True} } }}}

req_parm_validator = Validator(req_param_schema)

@app.route('/addBuilding',methods = ['POST', 'GET'])
def addBuilding():
    if request.method == 'POST':
        building_details_req = json.loads(request.data.decode('utf-8'))
        valid_req = req_parm_validator.validate(building_details_req)
        if valid_req:
            old = db.session.query(Building).filter(Building.name ==  building_details_req['name'], Building.address == building_details_req['address'], Building.landmarks == building_details_req['landmarks']).first()
            print(old)
            if old is None:
                building = Building()
                building.name = building_details_req['name']
                building.address = building_details_req['address']
                building.landmarks = building_details_req['landmarks']
                db.session.add(building)
                db.session.commit()
                latest_obj_id = db.session.query(Building).order_by(Building.id.desc()).first()
                for room in building_details_req['rooms']:
                    room_obj = Room()
                    room_obj.flat_number = room['flat_number']
                    room_obj.name = room['name']
                    room_obj.square_feet_area = room['square_feet_area']
                    room_obj.type = room['type']
                    room_obj.no_of_bathrooms = room['no_of_bathrooms']
                    room_obj.maintenance = room['maintenance']
                    room_obj.electricity_account_number = room['electricity_account_number']
                    room_obj.owner_id = latest_obj_id.id
                    db.session.add(room_obj)
                    db.session.commit()
                return json.dumps({"message":"success", "building": building_details_req}), 201, {'ContentType':'application/json'}
            else:
                return json.dumps({"message":"Building already exits", "building": building_details_req}), 409, {'ContentType':'application/json'}
        else:
            return json.dumps({"message":"invalid parameters", "building": building_details_req}), 422, {'ContentType':'application/json'}

if __name__ == '__main__':
    init_db()
    app.run()
