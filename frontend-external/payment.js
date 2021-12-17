let dataObj = new Array()
function makeAjaxQuery() {
    const newData = localStorage.getItem("data");
    console.log(newData);
    if (newData != null) {
    dataObj = JSON.parse(newData);
    console.log(dataObj);
    console.log(typeof dataObj);
    const service_name = document.getElementById('service_name1');
    const application_id = document.getElementById('application_id1');
    const applicant = document.getElementById('applicant1');
    const amount = document.getElementById('amount');
    service_name.value = "Driver Licence Service";
    application_id.value = dataObj.id;
    applicant.value = dataObj.name;
    amount.value = "80 AUD"
    }
    
}

let params = {};
let localArray = [];
function sendData() {
    const service_name1 = document.getElementById('service_name1').value;
    const application_id1 = document.getElementById('application_id1').value;
    const card1 = document.getElementById('card_number1').value;
    card1.toString()
    if (card1.length < 16 || card1.length >16) {
        alert("Please enter 16 characters in the Card area")
    } else {


    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/payment';
    params = {
        "service_name": service_name1,
        "application_id": application_id1
                    
    }
    http.open('POST', url, true);
    
    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/json');
    
    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            localArray.push(http.responseText);
            localStorage.setItem("newdata", localArray);
            window.location = "http://localhost:8888/paymentSuccess.html";
        }
    }
    http.send(JSON.stringify(params));	
}
}