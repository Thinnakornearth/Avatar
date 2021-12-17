from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)


# init app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://birth:birth@db/birth'

db=SQLAlchemy(app)

db.init_app(app)

class AppUser(db.Model):
    app_id = db.Column(db.Integer, primary_key=True)
    family_name = db.Column(db.String(20), nullable=False)
    given_name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime, nullable = False, default = datetime)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable = False)
    email = db.Column(db.String(50), unique=True, nullable = False)
    birth_place = db.Column(db.String(50), nullable = False)
    firstparent_name = db.Column(db.String(50), nullable=False)
    secondparent_name = db.Column(db.String(50), nullable=False)
    registration_id = db.Column(db.Integer, unique=True, nullable = False)
    status = db.Column(db.String(100), nullable = False, default = "waiting for payment confirmation")
db.create_all()


@app.route('/birthcertificate', methods=['POST'])
def birthcertificate():
    input_data = request.json
    newAppUser= AppUser(**input_data)
    db.session.add(newAppUser) 
    try:
        db.session.commit()
    except:
        result = 'input error'
    return {
    'message':'Application Sucessfully Submitted', 
    'reference id':newAppUser.app_id}   

     
@app.route('/birthcertificate/<app_id>/get_app_details')
def get_app_details(app_id):
    record = AppUser.query.filter_by(app_id=app_id).first()
    print(record)
    if not record:
        return { 'msg':'Application not found'}
    db.session.commit()    
    if record.registration_id:        
        return {
      "app_id": record.app_id,
      "registration_id":record.registration_id,
      "given_name": record.given_name,
      "family_name": record.family_name,
      "address": record.address,
      "firstparent_name": record.firstparent_name,
      "secondparent_name": record.secondparent_name,
      "dob": record.dob,
      "birth_place":record.birth_place,
      "phone": record.phone,
      "email": record.email,
      "status": record.status
  }
    
    
@app.route('/birthcertificate/<app_id>/app_under_verification', methods=['PATCH'])
def app_under_verification(app_id):
    record = AppUser.query.filter_by(app_id=app_id).first()
    print(record)
    if not record:
        return { 'msg':'Application not found'}
    record.status = "Under Verification"
    db.session.commit()    
    if record.registration_id:        
        return {
      "app_id": record.app_id,
      "registration_id":record.registration_id,
      "given_name": record.given_name,
      "family_name": record.family_name,
      "address": record.address,
      "firstparent_name": record.firstparent_name,
      "secondparent_name": record.secondparent_name,
      "dob": record.dob,
      "phone": record.phone,
      "email": record.email,
      "birth_place":record.birth_place,
      "status": record.status
  }

@app.route('/birthcertificate/<app_id>/app_approved', methods=['PATCH'])
def app_approved(app_id):
    record = AppUser.query.filter_by(app_id=app_id).first()
    if not record:
        return { 'msg':'Application not found'}
    record.status = "Application Approved"
    db.session.commit()    
    if record.registration_id:        
        return {
        "app_id": record.app_id,
        "registration_id":record.registration_id,
        "given_name": record.given_name,
        "family_name": record.family_name,
        "address": record.address,
        "firstparent_name": record.firstparent_name,
        "secondparent_name": record.secondparent_name,
        "dob": record.dob,
        "phone": record.phone,
        "email": record.email,
        "birth_place":record.birth_place,
        "status": record.status
              } 
              
@app.route('/birthcertificate/<app_id>/app_rejected', methods=['PATCH'])
def app_rejected(app_id):
    record = AppUser.query.filter_by(app_id=app_id).first()
    if not record:
        return { 'msg':'Application not found'}
    record.status = "Application Rejected"
    db.session.commit()    
    if record.registration_id:        
        return {
        "app_id": record.app_id,
        "registration_id":record.registration_id,
        "given_name": record.given_name,
        "family_name": record.family_name,
        "address": record.address,
        "firstparent_name": record.firstparent_name,
        "secondparent_name": record.secondparent_name,
        "dob": record.dob,
        "birth_place":record.birth_place,
        "phone": record.phone,
        "email": record.email,
        "status": record.status
              }               
  

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, port=9000)