let params = {};
let localArray = [];
function tcheck() {
    const id = document.getElementById('id').value;

    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/travel-exemption-applications/'+id;
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            console.log(http.responseText);
            let obj =  JSON.parse(http.responseText);
            document.getElementById("d-id").innerText =obj.id;
            document.getElementById("d-name").innerText =obj.name;
            document.getElementById("d-dob").innerText =obj.dob;
            document.getElementById("d-reason").innerText =obj.reason;
            document.getElementById("d-phone").innerText =obj.tel;
            document.getElementById("d-sub").innerText =obj.sub_date;
            document.getElementById("d-status").innerText =obj.status;
        }
    }
    http.open("GET",url);
    http.send(null);
}

function approve() {
    const tid = document.getElementById('aid').value;

    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/travel-exemption-applications/'+tid+'/approve' ;
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            console.log(http.responseText);
            let obj =  JSON.parse(http.responseText);
            document.getElementById("d-id").innerText =obj.id;
            document.getElementById("d-name").innerText =obj.name;
            document.getElementById("d-dob").innerText =obj.dob;
            document.getElementById("d-reason").innerText =obj.reason;
            document.getElementById("d-phone").innerText =obj.tel;
            document.getElementById("d-sub").innerText =obj.sub_date;
            document.getElementById("d-status").innerText =obj.status;
        }
    }
    http.open("PATCH",url);
    http.send(null);
}

function reject() {
    const tid = document.getElementById('rid').value;

    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/travel-exemption-applications/'+tid+'/reject' ;
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            console.log(http.responseText);
            let obj =  JSON.parse(http.responseText);
            document.getElementById("d-id").innerText =obj.id;
            document.getElementById("d-name").innerText =obj.name;
            document.getElementById("d-dob").innerText =obj.dob;
            document.getElementById("d-reason").innerText =obj.reason;
            document.getElementById("d-phone").innerText =obj.tel;
            document.getElementById("d-sub").innerText =obj.sub_date;
            document.getElementById("d-status").innerText =obj.status;
        }
    }
    http.open("PATCH",url);
    http.send(null);
}
