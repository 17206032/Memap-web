// validate input
var dob = document.getElementById('dobinput');
dob.onblur = function(){
    var dobdata = document.getElementById('dobinput').value;
    var str = /^((?:19|20)\d\d)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/;
    var error1 = "Format is wrong";
    var error2 = "Need enter date of birth"
    if (dobdata == ""){
        document.getElementById('doberror').innerText=error2;
        setTimeout("getdobfocus();",100)
    }else{
        if (!str.test(dobdata)) {
            document.getElementById('doberror').innerText=error1;
            setTimeout("getdobfocus();",100)
           }else{
            document.getElementById('doberror').innerText="";
        }
    }
}

function getdobfocus() {
    document.getElementById('dobinput').focus();
}
