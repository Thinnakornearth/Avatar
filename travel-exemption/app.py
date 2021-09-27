from flask import Flask, request



app = Flask(__name__)

applications = []

@app.post("/")  
def addApplication():
    newForm = request.get_json()
    applications.append(newForm)
    return newForm



@app.get("/checkStatus/<a_id>")
def checkStatus(a_id):
    for each in applications:
        if each["application_id"] == a_id:
            return each
    return "not exist"


@app.get("/")
def test():
    return {
        "applications" : applications
    }



