let dataObj = new Array()
function makeAjaxQuery() {
    const newData = localStorage.getItem("newdata");
    console.log(newData);
    if (newData != null) {
    dataObj = JSON.parse(newData);
    console.log(dataObj);
    console.log(typeof dataObj);
    let aID = dataObj.application_id;
    Number(aID);
    let http = new XMLHttpRequest();
    const url = 'http://localhost:8080/driver-licence-applications/' + aID + '/paymentSuccess';
    
    http.open('PATCH', url, true);
    
    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/json');
    
    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            console.log("success");
        }
    }
    http.send();	
}
    }
    
