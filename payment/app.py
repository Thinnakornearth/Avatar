from flask import Flask, request, jsonify, abort, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import sys


app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://payment:payment@payment-db/paymentservice'



class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key = True)
    service_name = db.Column(db.String(50), nullable = False)
    application_id = db.Column(db.Integer, nullable = False)
    pay_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    status = db.Column(db.String(50), nullable = False, default = "Payment Successful")


@app.route("/payment", methods = ["POST"])
def add_payment():
    newForm = request.get_json()
    newPayment = Payment(**newForm)
    db.session.add(newPayment)
    db.session.commit()
    return {
        "id": newPayment.payment_id,
        "application_id": newPayment.application_id,
        "pay_date": newPayment.pay_date
    }
@app.route("/payment/<payment_id>")
def get_payment(payment_id):
    record = Payment.query.filter_by(payment_id=payment_id).first()
    print(record)
    if not record:
        abort(404)

    return {
        "payment_id": record.payment_id,
        "service_name": record.service_name,
        "application_id": record.application_id,
        "pay_date": record.pay_date,
        "status": record.status}


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)

