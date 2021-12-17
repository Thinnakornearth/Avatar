let params = {};
let localArray = [];
function makeAjaxQuery() {
    const name1 = document.getElementById('name1').value;
    const name2 = document.getElementById('name2').value;
    const dob1 = document.getElementById('dob1').value;
    const address1 = document.getElementById('address1').value;
    const phone1 = document.getElementById('phone1').value;
    const email1 = document.getElementById('email1').value;
    const birthplace1 = document.getElementById('birthplace1').value;
    const firstparent1 = document.getElementById('firstparent1').value;
    const secondparent1 = document.getElementById('secondparent1').value;
    const registrationid1 = document.getElementById('registrationid1').value;

    let http = new XMLHttpRequest();
    const url = 'http://localhost:7000/';
    if (registrationid1) {
        params = {
            "family_name": name1,
            "given_name": name2,
            "dob": dob1,
            "address": address1,
            "phone": phone1,
            "email": email1,
            "birth_place": birthplace1,
            "firstparent_name": firstparent1,
            "secondparent_name": secondparent1,
            "registration_id": registrationid1,
        }
    }
    http.open('POST', url, true);

    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/json');

    http.onreadystatechange = function () {//Call a function when the state changes.
        if (http.readyState == 4 && http.status == 200) {
            localArray.push(http.responseText);
            localStorage.setItem("data", localArray);
            window.location = "http://localhost:800/payment.html";
        }
    }
    http.send(JSON.stringify(params));
}