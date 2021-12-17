from flask import Flask, request,jsonify
from flask_cors import CORS
import requests
import sys
# from flask_restplus import Api, Resource



app = Flask(__name__)
CORS(app)
@app.post("/travel-exemption-applications")  
def add_application():
    input = request.get_json()
    r= requests.post('http://travel-exemption:5000/applications', json=input)
    message = r.json()
    return message


@app.get("/travel-exemption-applications/<id>")
def get_application(id):
    r = requests.get('http://travel-exemption:5000/applications/'+id)
    message = r.json()
    return message
    


@app.get("/travel-exemption-applications")
def get_all_applications():
    r = requests.get('http://travel-exemption:5000/applications')
    message = r.json()
    return jsonify(message)



@app.patch("/travel-exemption-applications/<id>/approve")
def approve_application(id):
    r = requests.patch('http://travel-exemption:5000/applications/'+id+'/approve')
    message = r.json()
    return message


@app.patch("/travel-exemption-applications/<id>/reject")
def reject_application(id):
    r = requests.patch('http://travel-exemption:5000/applications/'+id+'/reject')
    message = r.json()
    return message


@app.post("/driver-licence-applications")
def add_driver_licence_application():
    # print("@@@@!!!!!!!!!@@", file=sys.stderr)
    input = request.get_json()
    r= requests.post('http://driverlicenceservice_backend_1:5000/', json=input)
    # print("@@@@@@@@@@@@@@@@@@@@"+str(r.content), file=sys.stderr)
    # print("@@@@@@@@@@@@@@@@@@@@"+str(r.text), file=sys.stderr)
    # print("@@@@@@@@@@@@@@@@@@@@"+str(r.reason), file=sys.stderr)
    message = r.json()
    return message


@app.post("/payment")
def add_payment():
    input = request.get_json()
    r= requests.post('http://payment_backend_1:3000/payment', json=input)
    message = r.json()
    return message


@app.get("/driver-licence-applications/<id>")
def get_driver_licence_application(id):
    r = requests.get('http://driverlicenceservice_backend_1:5000/applications/'+id)
    message = r.json()
    return message
    

@app.patch("/driver-licence-applications/<id>/inProcess")
def driver_licence_application_inprocess(id):
    r = requests.patch('http://driverlicenceservice_backend_1:5000/applications/'+id+'/inProcess')
    message = r.json()
    return message

@app.patch("/driver-licence-applications/<id>/approved")
def driver_licence_application_approved(id):
    r = requests.patch('http://driverlicenceservice_backend_1:5000/applications/'+id+'/approved')
    message = r.json()
    return message

@app.patch("/driver-licence-applications/<id>/rejected")
def driver_licence_application_rejected(id):
    r = requests.patch('http://driverlicenceservice_backend_1:5000/applications/'+id+'/rejected')
    message = r.json()
    return message


@app.patch("/driver-licence-applications/<id>/paymentSuccess")
def driver_licence_application_paymentsuccess(id):
    r = requests.patch('http://driverlicenceservice_backend_1:5000/applications/'+id+'/paymentSuccess')
    message = r.json()
    return message