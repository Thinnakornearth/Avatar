let params = {};
let localArray = [];
function makeAjaxQuery() {
    const name1 = document.getElementById('name1').value;
    const dob1 = document.getElementById('dob1').value;
    const address1 = document.getElementById('address1').value;
    const phone1 = document.getElementById('phone1').value;
    const email1 = document.getElementById('email1').value;
    const passport1 = document.getElementById('passport1').value;
    const medicare1 = document.getElementById('medicare1').value;
    const photoid1 = document.getElementById('photoid1').value;

    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/driver-licence-applications';
    if (medicare1) {
        params = {
            "name": name1,
            "dob": dob1,
            "address": address1,
            "phone": phone1,
            "email": email1,
            "medicare_card": medicare1,
            "passport_number": passport1,
    }};
    if (photoid1) {
        params = {
            "name": name1,
            "dob": dob1,
            "address": address1,
            "phone": phone1,
            "email": email1,
            "photo_id": photoid1,
            "passport_number": passport1,
            }
    }
    http.open('POST', url, true);
    
    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/json');
    
    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            localArray.push(http.responseText);
            localStorage.setItem("data", localArray);
            window.location.href = "http://localhost:8888/payment.html";
        }
    }
    http.send(JSON.stringify(params));	


    
}