let params = {};
let localArray = [];
function check() {
    const tid = document.getElementById('t-id').value;

    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/driver-licence-applications/'+tid;
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            console.log(http.responseText);
            let obj =  JSON.parse(http.responseText);
            document.getElementById("d-id").innerText =obj.id;
            document.getElementById("d-name").innerText =obj.name;
            document.getElementById("d-dob").innerText =obj.dob;
            document.getElementById("d-address").innerText =obj.address;
            document.getElementById("d-phone").innerText =obj.phone;
            document.getElementById("d-sub").innerText =obj.submit_date;
            document.getElementById("d-status").innerText =obj.status;
        }
    }
    http.open("GET",url);
    http.send(null);
}

function approve() {
    const tid = document.getElementById('ta-id').value;

    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/driver-licence-applications/'+tid+'/approved' ;
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            console.log(http.responseText);
            let obj =  JSON.parse(http.responseText);
            document.getElementById("d-id").innerText =obj.id;
            document.getElementById("d-name").innerText =obj.name;
            document.getElementById("d-dob").innerText =obj.dob;
            document.getElementById("d-address").innerText =obj.address;
            document.getElementById("d-phone").innerText =obj.phone;
            document.getElementById("d-sub").innerText =obj.submit_date;
            document.getElementById("d-status").innerText =obj.status;
        }
    }
    http.open("PATCH",url);
    http.send(null);
}

function reject() {
    const tid = document.getElementById('tr-id').value;

    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/driver-licence-applications/'+tid+'/rejected';
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            console.log(http.responseText);
            let obj =  JSON.parse(http.responseText);
            document.getElementById("d-id").innerText =obj.id;
            document.getElementById("d-name").innerText =obj.name;
            document.getElementById("d-dob").innerText =obj.dob;
            document.getElementById("d-address").innerText =obj.address;
            document.getElementById("d-phone").innerText =obj.phone;
            document.getElementById("d-sub").innerText =obj.submit_date;
            document.getElementById("d-status").innerText =obj.status;
        }
    }
    http.open("PATCH",url);
    http.send(null);
}
