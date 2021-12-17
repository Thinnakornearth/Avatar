from flask import Flask, jsonify, request, abort, render_template, redirect
import os
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import datetime
import sys

from werkzeug.utils import redirect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://drive:drive@db/driver'


db = SQLAlchemy(app)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    dob = db.Column(db.DateTime, nullable = False)
    address = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(10), nullable = False)
    photo_id = db.Column(db.String(10), nullable = True)
    passport_number = db.Column(db.String(8), nullable = False)
    medicare_card = db.Column(db.String(7), nullable = True)
    attachment = db.Column(db.String(8), nullable = True)
    submit_date = db.Column(db.DateTime, nullable = False, default = datetime.datetime.utcnow)
    status = db.Column(db.String(100), nullable = False, default = "waiting for payment confirmation")

    UniqueConstraint('photo_id', 'passport_number', 'medicare_card', 'email', name='user_application_unique')


@app.route('/', methods=['POST'])
def addApplication():
    newApp = request.get_json()
    print("THE RECORD" + str(newApp), file=sys.stderr)
    newApplication = Application(**newApp)
    db.session.add(newApplication)
    try:
        db.session.commit()

    except Exception as e:
        print("FAIL to SAVE NEW APP"+str(e), file=sys.stderr)
        abort(400)
        # return 'Please fill up all the required (*) point'
    return {"id": newApplication.id,
            "name": newApplication.name,
            "submit_date": newApplication.submit_date,
            "email": newApplication.email}
    
@app.route('/applications/<id>/paymentSuccess', methods=['PATCH'])
def paymentSuccess(id):
    record = Application.query.filter_by(id=id).first()
    if not record:
        abort(404)
    record.status = 'submitted successfully'
    db.session.commit()
    if record.photo_id and record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "email": record.email,
        "phone": record.phone,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.photo_id:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }



@app.route('/applications/<id>')
def getApplication(id):
    record = Application.query.filter_by(id=id).first()
    if not record:
        abort(404)
    if record.photo_id and record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.photo_id:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }

@app.route('/applications/<id>/inProcess', methods=['PATCH'])
def update_application(id):
    record = Application.query.filter_by(id=id).first()
    if not record:
        abort(404)
    record.status = 'In Process'
    db.session.commit()
    if record.photo_id and record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.photo_id:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }

@app.route('/applications/<id>/approved', methods=['PATCH'])
def approve_application(id):
    record = Application.query.filter_by(id=id).first()
    if not record:
        abort(404)
    record.status = 'Approved'
    db.session.commit()
    if record.photo_id and record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.photo_id:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }

@app.route('/applications/<id>/rejected', methods=['PATCH'])
def reject_application(id):
    record = Application.query.filter_by(id=id).first()
    if not record:
        abort(404)
    record.status = 'Rejected'
    db.session.commit()
    if record.photo_id and record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.photo_id:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "photo_id": record.photo_id,
        "submit_date": record.submit_date,
        "status": record.status
        }
    if record.medicare_card:
        return {
        "id": record.id,
        "name": record.name,
        "dob": record.dob,
        "address": record.address,
        "phone": record.phone,
        "email": record.email,
        "passport_number": record.passport_number,
        "medicare_card": record.medicare_card,
        "submit_date": record.submit_date,
        "status": record.status
        }

    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')