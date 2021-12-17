from flask import Flask, request, jsonify, abort
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
# from flask_restplus import Api, Resource
import os

app = Flask(__name__)
db = SQLAlchemy(app)
# apiapp = Api(app)
# name_space = app.namespace('main', description='Main APIs')

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "mysql+mysqlconnector://root:12345@localhost:3306/travel_exemption"
)
migrate = Migrate(app,db)


class Application(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),nullable = False )
    visa_num = db.Column(db.String(15), nullable = False)
    passport_num = db.Column(db.String(15), nullable = False)
    reason = db.Column(db.String(200), nullable = False)
    dob = db.Column(db.DateTime, nullable = False)
    tel = db.Column(db.String(12),nullable = False)
    email = db.Column(db.String(50),nullable = False)
    attachment = db.Column(db.String(50),nullable = True)
    sub_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    status = db.Column(db.String(15),nullable = False, default = "submitted")
    initial_screen = db.Column(db.String(20),nullable = False, default = "pending for review")



@app.post("/applications")  
def add_application():
    new_form = request.get_json()
    visa_num = new_form['visa_num']
    r= requests.get('http://check-visa-status:5000/visa-status/'+ visa_num )
    if r.status_code == 200:
        new_form['initial_screen'] = 'pass'

    application = Application(**new_form)
    db.session.add(application)
    db.session.commit()
    return {
        "id": application.id,
        "sub_date": application.sub_date
    }



@app.get("/applications/<id>")
def get_application(id):
    record = Application.query.filter_by(id=id).first()
    print(record)
    if not record:
        abort(404)

    return {
        "id": record.id,
        "name": record.name,
        "visa_num": record.visa_num,
        "passport_num": record.passport_num,
        "reason": record.reason,
        "dob":record.dob,
        "tel":record.tel,
        "attachment":record.attachment,
        "initial_screen":record.initial_screen,
        "sub_date": record.sub_date,
        "status": record.status}

    


@app.get("/applications")
def get_all_applications():
    data=[]
    applications = Application.query.all()
    print(applications)
    for each in applications:
        row = {
        "id": each.id,
        "name": each.name,
        "visa_num": each.visa_num,
        "passport_num": each.passport_num,
        "reason": each.reason,
        "dob":each.dob,
        "tel":each.tel,
        "attachment":each.attachment,
        "initial_screen":each.initial_screen,
        "sub_date": each.sub_date,
        "status": each.status
        }
        data.append(row)
    return jsonify(data)



@app.patch("/applications/<id>/approve")
def approve_application(id):
    record = Application.query.filter_by(id=id).first()
    if not record:
        abort(404)
    record.status = "approved"
    db.session.commit()
    return {
        "id": record.id,
        "name": record.name,
        "visa_num": record.visa_num,
        "passport_num": record.passport_num,
        "reason": record.reason,
        "dob":record.dob,
        "tel":record.tel,
        "attachment":record.attachment,
        "initial_screen":record.initial_screen,
        "sub_date": record.sub_date,
        "status": record.status}


@app.patch("/applications/<id>/reject")
def reject_application(id):
    record = Application.query.filter_by(id=id).first()
    if not record:
        abort(404)
    record.status = "rejected"
    db.session.commit()
    return {
        "id": record.id,
        "name": record.name,
        "visa_num": record.visa_num,
        "passport_num": record.passport_num,
        "reason": record.reason,
        "dob":record.dob,
        "tel":record.tel,
        "attachment":record.attachment,
        "initial_screen":record.initial_screen,
        "sub_date": record.sub_date,
        "status": record.status}
