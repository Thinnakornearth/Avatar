from flask import Flask, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:12345@localhost:3306/travel_exemption"
applications = []
migrate = Migrate(app,db)


class Application(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),nullable = False )
    visa_num = db.Column(db.String(15), nullable = False)
    passport_num = db.Column(db.String(15), nullable = False)
    reason = db.Column(db.String(200), nullable = False)
    dob = db.Column(db.DateTime, nullable = False)
    tel = db.Column(db.String(12),nullable = False)
    attachment = db.Column(db.String(50),nullable = True)
    sub_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    status = db.Column(db.String(15),nullable = False, default = "submitted")



@app.post("/createapp")  
def addApplication():
    newForm = request.get_json()
    newApplication = Application(**newForm)
    db.session.add(newApplication)
    db.session.commit()
    return {
        "id": newApplication.id,
        "submitted at": newApplication.sub_date
    }



@app.get("/checkstatus/<a_id>")
def checkStatus(a_id):
    for each in applications:
        if each["application_id"] == a_id:
            return each
    return "not exist"


@app.get("/retrieveall")
def test():
    return {
        "applications" : applications
    }



