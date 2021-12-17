let params = {};
let localArray = [];

function makeAjaxQuery() {
    const name = document.getElementById('name').value;
    const dob = document.getElementById('dob').value;
    const tel = document.getElementById('tel').value;
    const visa_num = document.getElementById('visa_num').value;
    const email = document.getElementById('email').value;
    const passport_num = document.getElementById('passport_num').value;
    const reason = document.getElementById('reason').value;
    const attachment = document.getElementById('attachment').value;
    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/travel-exemption-applications';

    params = {
        "name" : name,
        "dob" : dob,
        "tel":tel, 
        "visa_num" : visa_num,
        "email": email,
        "passport_num": passport_num,
        "reason": reason,
        "attachment": attachment 
            }
            
    http.open('POST', url, true);
    
    http.setRequestHeader('Content-type', 'application/json');
    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {

            window.location.href = "http://localhost:8888/travelExemptionSuccess.html"
            
            
        }
    }
    console.log(JSON.stringify(params))
    console.log(http)
    http.send(JSON.stringify(params));	
    
    

}


    