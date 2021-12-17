from flask import Flask, request, jsonify, abort
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "mysql+mysqlconnector://root:12345@localhost:3306/visa"
)
migrate = Migrate(app,db)

class VisaStatus(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),nullable = False )
    visa_num = db.Column(db.String(15), nullable = False)
    status = db.Column(db.String(15),nullable = False, default = "valid")


@app.get("/visa-status/<visa_num>")
def get_application(visa_num):
    record = VisaStatus.query.filter_by(visa_num=visa_num).first()
    print(record)
    if not record:
        abort(404)

    return {
        "id": record.id,
        "name": record.name,
        "visa_num": record.visa_num,
        "status": record.status}
